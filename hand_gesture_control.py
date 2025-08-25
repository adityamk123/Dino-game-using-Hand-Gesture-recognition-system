import cv2
import mediapipe as mp
import pyautogui
import time
import win32gui
import win32con

# Initialize webcam
cap = cv2.VideoCapture(0)
cap.set(3, 640)  # Width
cap.set(4, 480)  # Height

# Initialize Mediapipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
mp_draw = mp.solutions.drawing_utils

# Timer to avoid repeated actions
last_action_time = 0
action_delay = 0.5  # seconds

def bring_window_to_front():
    # Focus on the Chrome window with Dino game
    window_title = "Google Chrome"  # Adjust if needed
    window = win32gui.FindWindow(None, window_title)
    if window != 0:
        win32gui.ShowWindow(window, win32con.SW_RESTORE)
        win32gui.SetForegroundWindow(window)

while True:
    bring_window_to_front()  # Ensure the Dino game window is in focus

    success, img = cap.read()
    if not success:
        break

    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    result = hands.process(img_rgb)

    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            mp_draw.draw_landmarks(img, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            lm_list = []
            for id, lm in enumerate(hand_landmarks.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                lm_list.append((id, cx, cy))

            # Detect gestures
            if len(lm_list) >= 13:
                index_tip = lm_list[8][2]  # Index finger tip
                index_pip = lm_list[6][2]  # Index finger PIP
                middle_tip = lm_list[12][2]  # Middle finger tip
                middle_pip = lm_list[10][2]  # Middle finger PIP

                # Gesture logic: index up, middle down for jump
                index_up = index_tip < index_pip
                middle_up = middle_tip < middle_pip

                current_time = time.time()
                if current_time - last_action_time > action_delay:
                    if index_up and not middle_up:
                        pyautogui.press("space")  # Jump
                        last_action_time = current_time
                    elif index_up and middle_up:
                        pyautogui.press("down")  # Duck
                        last_action_time = current_time

    cv2.imshow("Hand Gesture Control", img)

    # Exit the loop if the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
