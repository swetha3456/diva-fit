import cv2
import mediapipe as mp
import numpy as np
import csv
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_pose = mp.solutions.pose

not_live = False

if not_live:
    video_path = '/home/dyuthi/Videos/Screencasts/knee_jumps.webm'
else:
    video_path = 0
# For webcam input:
#cap = cv2.VideoCapture(0)
#video_path = 0

cap = cv2.VideoCapture(video_path)


landmarks = []
csv_data = []
frame_number = 0
with mp_pose.Pose(
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5) as pose:
    while cap.isOpened() and frame_number < 120:
        success, image = cap.read()
        if not success:
            print("Ignoring empty camera frame.")
          # If loading a video, use 'break' instead of 'continue'.
            continue

        # To improve performance, optionally mark the image as not writeable to
        # pass by reference.
        image.flags.writeable = False
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        results = pose.process(image)

        # Draw the pose annotation on the image.
        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        mp_drawing.draw_landmarks(
            image,
            results.pose_landmarks,
            mp_pose.POSE_CONNECTIONS,
            landmark_drawing_spec=mp_drawing_styles.get_default_pose_landmarks_style())
        
        if results.pose_landmarks:
            landmarks.append(results.pose_landmarks.landmark)
        
        # Flip the image horizontally for a selfie-view display.
        cv2.imshow('MediaPipe Pose', cv2.flip(image, 1))
        
        if cv2.waitKey(5) & 0xFF == 27:
            break
        frame_number += 1

cap.release()
cv2.destroyAllWindows()

print(landmarks)
import numpy as np

# Initialize lists to store coordinates
left_hip_coords = []
right_hip_coords = []
left_knee_coords = []
right_knee_coords = []
left_ankle_coords = []
right_ankle_coords = []

# Extract coordinates for each frame
for frame_landmarks in landmarks:
    left_hip_coords.append([
        frame_landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].x,
        frame_landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].y,
        frame_landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].z
    ])
    right_hip_coords.append([
        frame_landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value].x,
        frame_landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value].y,
        frame_landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value].z
    ])
    left_knee_coords.append([
        frame_landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value].x,
        frame_landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value].y,
        frame_landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value].z
    ])
    right_knee_coords.append([
        frame_landmarks[mp_pose.PoseLandmark.RIGHT_KNEE.value].x,
        frame_landmarks[mp_pose.PoseLandmark.RIGHT_KNEE.value].y,
        frame_landmarks[mp_pose.PoseLandmark.RIGHT_KNEE.value].z
    ])
    left_ankle_coords.append([
        frame_landmarks[mp_pose.PoseLandmark.LEFT_ANKLE.value].x,
        frame_landmarks[mp_pose.PoseLandmark.LEFT_ANKLE.value].y,
        frame_landmarks[mp_pose.PoseLandmark.LEFT_ANKLE.value].z
    ])
    right_ankle_coords.append([
        frame_landmarks[mp_pose.PoseLandmark.RIGHT_ANKLE.value].x,
        frame_landmarks[mp_pose.PoseLandmark.RIGHT_ANKLE.value].y,
        frame_landmarks[mp_pose.PoseLandmark.RIGHT_ANKLE.value].z
    ])

# Convert lists to NumPy arrays
left_hip_coords = np.array(left_hip_coords)
right_hip_coords = np.array(right_hip_coords)
left_knee_coords = np.array(left_knee_coords)
right_knee_coords = np.array(right_knee_coords)
left_ankle_coords = np.array(left_ankle_coords)
right_ankle_coords = np.array(right_ankle_coords)


if not_live:
    # Save NumPy arrays to files
    np.save('left_hip_coords.npy', left_hip_coords)
    np.save('right_hip_coords.npy', right_hip_coords)
    np.save('left_knee_coords.npy', left_knee_coords)
    np.save('right_knee_coords.npy', right_knee_coords)
    np.save('left_ankle_coords.npy', left_ankle_coords)
    np.save('right_ankle_coords.npy', right_ankle_coords)

else:
    # Save NumPy arrays to files
    np.save('left_hip_coords_live.npy', left_hip_coords)
    np.save('right_hip_coords_live.npy', right_hip_coords)
    np.save('left_knee_coords_live.npy', left_knee_coords)
    np.save('right_knee_coords_live.npy', right_knee_coords)
    np.save('left_ankle_coords_live.npy', left_ankle_coords)
    np.save('right_ankle_coords_live.npy', right_ankle_coords)
