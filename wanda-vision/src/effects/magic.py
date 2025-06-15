import cv2
import numpy as np

class MagicEffect:
    def __init__(self):
        self.effect_active = False

    def display_effect(self, frame, hand_positions):
        if self.effect_active:
            # Logic to render magic effect based on hand positions
            pass

    def update_effect(self, hand_positions):
        if hand_positions:
            self.effect_active = True
        else:
            self.effect_active = False

def draw_magic_effect(frame, hand_landmarks):
    if hand_landmarks:
        h, w, _ = frame.shape
        for handLms in hand_landmarks:
            # Use landmark 0 (wrist) as the center
            cx = int(handLms.landmark[0].x * w)
            cy = int(handLms.landmark[0].y * h)
            # Draw a glowing circle
            overlay = frame.copy()
            cv2.circle(overlay, (cx, cy), 60, (255, 0, 255), -1)
            cv2.circle(overlay, (cx, cy), 90, (255, 0, 255), 2)
            alpha = 0.5
            frame[:] = cv2.addWeighted(overlay, alpha, frame, 1 - alpha, 0)