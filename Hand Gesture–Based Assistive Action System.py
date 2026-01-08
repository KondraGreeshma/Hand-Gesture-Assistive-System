#!/usr/bin/env python
# coding: utf-8

# In[2]:


get_ipython().system('pip install HandTrackingModule')
get_ipython().system('pip install cvzone mediapipe')
get_ipython().system('pip install pygame')
import warnings
warnings.filterwarnings("ignore", category=UserWarning)


# In[2]:


import cv2
import os
import numpy as np
import pygame
from cvzone.HandTrackingModule import HandDetector
import math
import time

# ================= AUDIO INIT =================
pygame.mixer.init(frequency=44100, size=-16, channels=2, buffer=512)

# ================= CAMERA =================
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

# ================= LOAD COUNTER IMAGES (0–5) =================
counterPath = r'D:\FingerImages'
counterList = [None] * 6

for i in range(6):
    for ext in ['png', 'jpg', 'jpeg']:
        imgPath = os.path.join(counterPath, f"{i}.{ext}")
        if os.path.exists(imgPath):
            img = cv2.imread(imgPath)
            counterList[i] = cv2.resize(img, (150, 150))
            break

# ================= LOAD ACTION IMAGES (0–5) =================
actionPath = r'D:\Action images'
actionImages = {}

for i in range(6):
    for ext in ['png', 'jpg', 'jpeg']:
        imgPath = os.path.join(actionPath, f"{i}.{ext}")
        if os.path.exists(imgPath):
            img = cv2.imread(imgPath)
            actionImages[i] = cv2.resize(img, (640, 480))
            break

# ================= LOAD AUDIO =================
audioPath = r'D:\Audio image'
actionAudio = {}

for i in range(6):
    for ext in ['mp3', 'wav', 'ogg']:
        path = os.path.join(audioPath, f"{i}.{ext}")
        if os.path.exists(path):
            actionAudio[i] = pygame.mixer.Sound(path)
            break

# ================= HAND DETECTOR =================
detector = HandDetector(maxHands=1, detectionCon=0.8)

# ================= STATE VARIABLES =================
lastFingers = -1
lastPlayTime = 0
AUDIO_DELAY = 1.0  # seconds

# ================= HELPER =================
def getGesture(hand):
    fingers = detector.fingersUp(hand)
    return f"{fingers.count(1)} Fingers"

# ================= MAIN LOOP =================
while True:
    success, img = cap.read()
    if not success:
        break

    hands, img = detector.findHands(img)
    totalFingers = 0
    gesture = ""

    if hands:
        hand = hands[0]
        totalFingers = detector.fingersUp(hand).count(1)
        gesture = getGesture(hand)

    # ---------- DISPLAY COUNTER ----------
    if totalFingers < len(counterList) and counterList[totalFingers] is not None:
        img[0:150, 0:150] = counterList[totalFingers]

    cv2.putText(img, gesture, (10, 450),
                cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)

    cv2.imshow("Finger Counter", img)

    # ---------- ACTION IMAGE ----------
    if totalFingers in actionImages:
        cv2.imshow("Action Output", actionImages[totalFingers])

    # ---------- AUDIO (FIXED: NO RESOUND) ----------
    currentTime = time.time()
    if totalFingers != lastFingers and (currentTime - lastPlayTime) > AUDIO_DELAY:
        pygame.mixer.stop()
        if totalFingers in actionAudio:
            actionAudio[totalFingers].play()
        lastFingers = totalFingers
        lastPlayTime = currentTime

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# ================= CLEANUP =================
cap.release()
pygame.mixer.quit()
cv2.destroyAllWindows()


# In[ ]:





# In[ ]:




