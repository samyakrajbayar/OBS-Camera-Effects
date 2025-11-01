import cv2
import numpy as np
from datetime import datetime

# Initialize camera
cap = cv2.VideoCapture(0)

# Effect state
current_effect = 0
effects = ['Normal', 'Edge Detection', 'Cartoonify', 'Color Pop', 'Pixelate', 'Mirror', 'Thermal', 'Glitch']

def apply_edge_detection(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 100, 200)
    return cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)

def apply_cartoonify(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.medianBlur(gray, 5)
    edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)
    color = cv2.bilateralFilter(frame, 9, 300, 300)
    cartoon = cv2.bitwise_and(color, color, mask=edges)
    return cartoon

def apply_color_pop(frame):
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower_red = np.array([0, 120, 70])
    upper_red = np.array([10, 255, 255])
    mask1 = cv2.inRange(hsv, lower_red, upper_red)
    lower_red = np.array([170, 120, 70])
    upper_red = np.array([180, 255, 255])
    mask2 = cv2.inRange(hsv, lower_red, upper_red)
    mask = mask1 + mask2
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray_3channel = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)
    result = np.where(mask[:, :, np.newaxis] != 0, frame, gray_3channel)
    return result

def apply_pixelate(frame, pixel_size=15):
    h, w = frame.shape[:2]
    temp = cv2.resize(frame, (w // pixel_size, h // pixel_size), interpolation=cv2.INTER_LINEAR)
    return cv2.resize(temp, (w, h), interpolation=cv2.INTER_NEAREST)

def apply_mirror(frame):
    h, w = frame.shape[:2]
    left = frame[:, :w//2]
    mirrored = cv2.flip(left, 1)
    return np.hstack([left, mirrored])

def apply_thermal(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    return cv2.applyColorMap(gray, cv2.COLORMAP_JET)

def apply_glitch(frame):
    result = frame.copy()
    h, w = result.shape[:2]
    
    # Random color channel shift
    shift = np.random.randint(-10, 10)
    result[:, :, 0] = np.roll(result[:, :, 0], shift, axis=1)
    
    # Random horizontal lines
    for _ in range(5):
        y = np.random.randint(0, h)
        strip_h = np.random.randint(2, 10)
        result[y:y+strip_h, :] = np.roll(result[y:y+strip_h, :], np.random.randint(-30, 30), axis=1)
    
    return result

print("OBS Camera Effects")
print("==================")
print("Controls:")
print("  SPACE - Cycle through effects")
print("  S - Save screenshot")
print("  Q - Quit")
print("\nStarting camera...")

while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    # Apply current effect
    if current_effect == 1:
        frame = apply_edge_detection(frame)
    elif current_effect == 2:
        frame = apply_cartoonify(frame)
    elif current_effect == 3:
        frame = apply_color_pop(frame)
    elif current_effect == 4:
        frame = apply_pixelate(frame)
    elif current_effect == 5:
        frame = apply_mirror(frame)
    elif current_effect == 6:
        frame = apply_thermal(frame)
    elif current_effect == 7:
        frame = apply_glitch(frame)
    
    # Add effect name overlay
    cv2.putText(frame, f"Effect: {effects[current_effect]}", (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    
    cv2.imshow('OBS Camera Effects', frame)
    
    key = cv2.waitKey(1) & 0xFF
    
    if key == ord('q'):
        break
    elif key == ord(' '):
        current_effect = (current_effect + 1) % len(effects)
        print(f"Switched to: {effects[current_effect]}")
    elif key == ord('s'):
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"screenshot_{timestamp}.png"
        cv2.imwrite(filename, frame)
        print(f"Screenshot saved: {filename}")

cap.release()
cv2.destroyAllWindows()
print("Camera closed. Goodbye!")
