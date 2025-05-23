import cv2 as cv
import numpy as np
import mediapipe as mp
import matplotlib
import math

mpDraw = mp.solutions.drawing_utils
mpFaceMesh = mp.solutions.face_mesh
faceMesh = mpFaceMesh.FaceMesh(max_num_faces=2)
drawSpec = mpDraw.DrawingSpec(thickness=1, circle_radius=2)

def eye_aspect_ratio(p1, p2, p3, p4, p5, p6):
    # p1: 33 – horizontal eye corner (left)
	# p2: 159 – top eyelid (inner)
	# p3: 158 – top eyelid (outer)
	# p4: 133 – horizontal eye corner (right)
	# p5: 153 – bottom eyelid (outer)
	# p6: 145 – bottom eyelid (inner)
    # Compute vertical distances
    A = math.dist(p2, p6)
    B = math.dist(p3, p5)
    # Compute horizontal distance
    C = math.dist(p1, p4)
    # EAR formula
    EAR = (A + B) / (2.0 * C)
    return EAR

def detect_facial_and_eye_landmarks(frame):
    results = faceMesh.process(frame)
    points_R = []
    points_L = []
    if results.multi_face_landmarks:
        for faceLms in results.multi_face_landmarks:
            #TAKE ONLY SELECTED LANDMARKS OF THE TOTAL 468
            right_eye_indices = [33, 159, 158, 133, 153, 145]
            left_eye_indices = [362, 380, 374, 263, 386, 385]
            ih, iw, ic = frame.shape
            for eye_id in right_eye_indices:
                lm = faceLms.landmark[eye_id]
                x, y = int(lm.x * iw), int(lm.y * ih)
                # print(f"Landmark {eye_id}: x={x}, y={y}")
                # cv.circle(frame, (x, y), 2, (0, 255, 0), -1)
                points_R.append([x,y])
            for eye_id in left_eye_indices:
                lm = faceLms.landmark[eye_id]
                x, y = int(lm.x * iw), int(lm.y * ih)
                # print(f"Landmark {eye_id}: x={x}, y={y}")
                # cv.circle(frame, (x, y), 2, (0, 255, 0), -1)
                points_L.append([x,y])
    # frame = cv.cvtColor(frame, cv.COLOR_RGB2BGR)
    # cv.imshow("Video", frame)
    return points_R, points_L

def load_video_frames_and_RGB(video_path):
    capture = cv.VideoCapture(video_path)
    num = 0
    while True and num == 0:
        isTrue, frame = capture.read()
        if not isTrue:
            break
        frame = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
        num += 1
        if cv.waitKey(20) & 0xFF == ord('d'):
            break
    capture.release()
    return frame

def get_fps(video_path):
    capture = cv.VideoCapture(video_path)
    fps = capture.get(cv.CAP_PROP_FPS)
    capture.release()
    return fps

frame = load_video_frames_and_RGB("test.mov")
points_R, points_L = detect_facial_and_eye_landmarks(frame)
print("Right Eye Points:", points_R)
print("Left Eye Points:", points_L)
print("Right EAR: ", eye_aspect_ratio(points_R[0],points_R[1],points_R[2],points_R[3],points_R[4], points_R[5]))
print("Left EAR: ", eye_aspect_ratio(points_L[0],points_L[1],points_L[2],points_L[3],points_L[4], points_L[5]))