#!/usr/bin/env python3
import cv2

cap = cv2.VideoCapture(0)
ret, frame = cap.read()

cv2.imshow('', frame)
cv2.waitKey()
