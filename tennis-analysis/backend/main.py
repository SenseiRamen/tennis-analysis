import mediapipe as mp
import cv2
import os
import numpy as np
from google.colab.patches import cv2_imshow
import sys
import matplotlib.pyplot as plt
from sklearn import metrics
from sklearn.model_selection import ParameterGrid
from sklearn.cluster import KMeans

def set_up_pose_detection_model():
    drawing = mp.solutions.drawing_utils
    drawing_style = mp.solutions.drawing_styles
    pose = mp.solutions.pose
    return drawing, pose

def get_video_writer(image_name, video_path):
    basename = os.path.basename(video_path)
    filename, extension = os.path.splitext(basename)
    size = (480, 640)
    make_directory(image_name)
    out = cv2.VideoWriter(f"{image_name}/{filename}_out.avi", cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'), 5, size)
    print(f"{image_name}/{filename}_out.avi")
    return out

def make_directory(name:str):
    if not os.path.isdir(name):
        os.mkdir(name)

def resize_image(image):
    h, w, c = image.shape
    downsize = (w//2, h//2)
    resize_img = cv2.resize(image, downsize)
    return resize_img, w//2, h//2

def pose_process_image(image, pose):
    image.flags.writeable = False
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = pose.process(image)

    image.flags.writeable = True
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    return image, results

def plot_angles_from_frames(mp_pose, landmarks, image, h, w, max_angle_right = 0):
    angles = []
    val = 50    
    angle, image = plot_angle(mp_pose.PoseLandmark.LEFT_SHOULDER.value, mp_pose.PoseLandmark.LEFT_ELBOW.value,
                              mp_pose.PoseLandmark.LEFT_WRIST.value, landmarks, image, h, w + val)
    angles.append(angle)
    angle, image = plot_angle(mp_pose.PoseLandmark.RIGHT_SHOULDER.value, mp_pose.PoseLandmark.RIGHT_ELBOW.value,
                              mp_pose.PoseLandmark.RIGHT_WRIST.value, landmarks, image, h, w - val)
    angles.append(angle)
    angle, image = plot_angle(mp_pose.PoseLandmark.LEFT_HIP.value, mp_pose.PoseLandmark.LEFT_KNEE.value,
                              mp_pose.PoseLandmark.LEFT_ANKLE.value, landmarks, image, h, w + val)
    angles.append(angle)
    angle, image = plot_angle(mp_pose.PoseLandmark.RIGHT_HIP.value, mp_pose.PoseLandmark.RIGHT_KNEE.value,
                              mp_pose.PoseLandmark.RIGHT_ANKLE.value, landmarks, image, h, w - val)
    angles.append(angle)
    angle, image = plot_angle(mp_pose.PoseLandmark.LEFT_SHOULDER.value, mp_pose.PoseLandmark.LEFT_HIP.value,
                              mp_pose.PoseLandmark.LEFT_KNEE.value, landmarks, image, h, w + val)
    angles.append(angle)
    angle, image = plot_angle(mp_pose.PoseLandmark.RIGHT_SHOULDER.value, mp_pose.PoseLandmark.RIGHT_HIP.value,
                              mp_pose.PoseLandmark.RIGHT_KNEE.value, landmarks, image, h, w - val)
    angles.append(angle)
    angle_left, image = plot_angle(mp_pose.PoseLandmark.LEFT_WRIST.value, mp_pose.PoseLandmark.LEFT_SHOULDER.value,
                              mp_pose.PoseLandmark.LEFT_HIP.value, landmarks, image, h, w + val)
    angles.append(angle_left)
    angle_right, image = plot_angle(mp_pose.PoseLandmark.RIGHT_WRIST.value, mp_pose.PoseLandmark.RIGHT_SHOULDER.value,
                              mp_pose.PoseLandmark.RIGHT_HIP.value, landmarks, image, h, w - val)
    angles.append(angle_right)
    max_angle_right = max(max_angle_right, angle_right)
    return angles, max_angle_right

def plot_angle(p1, p2, p3, landmarks, image, h, w):
    orgs1 = [landmarks[p1].x, landmarks[p1].y]
    orgs2 = [landmarks[p2].x, landmarks[p2].y]
    orgs3 = [landmarks[p3].x, landmarks[p3].y]
    angle = calculate_angle(orgs1, orgs2, orgs3)
    coord = np.multiply(orgs2, [w, h])
    draw_angle(tuple(coord.astype(int)), image, angle)
    return angle, image

def calculate_angle(a, b, c):
    a = np.array(a)
    b = np.array(b)
    c = np.array(c)

    radians = np.arctan2(c[1] - b[1], c[0] - b[0]) - np.arctan2(a[1] - b[1], a[0] - b [0])
    angle = np.abs(radians * 180.0 / np.pi)

    if angle > 180.0:
        angle = 360 - angle

    return round(angle, 1)

def draw_angle(org:tuple, image, angle):
    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = 2
    color = (0, 255, 0)
    thickness = 2
    cv2.putText(image, str(angle), org, font, font_scale, color, thickness)
    return image

def add_stage(frames, max_value):
    stage = 1
    for frame in frames:
        if frame[-1] == max_value:
            stage = 0
        frame.append(stage)
    return frames

def draw_landmarks(results, mp_drawing, mp_pose, image):
    landmark_list = results.pose_landmarks.landmark
    for id, lm in enumerate(landmark_list):
        if id in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 17, 18, 19, 20, 21, 22, 29, 30, 31, 32]:
          landmark_list[id].visibility = 0
    mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS,
                              mp_drawing.DrawingSpec(color = (255, 0, 0), thickness = 2, circle_radius = 2),
                              mp_drawing.DrawingSpec(color = (245, 66, 230), thickness = 2, circle_radius = 2))
    return image

def get_frames_angles(image_name:str, video_path:str)->tuple:

    mp_drawing, mp_pose = set_up_pose_detection_model()
    cap = cv2.VideoCapture(video_path)
    out = get_video_writer(image_name,video_path)
    img_count = 0
    output_images = []
    frames= []
    max_angle_right = 0
    with mp_pose.Pose(
        min_detection_confidence=0.5,
        min_tracking_confidence=0.5) as pose:
      while cap.isOpened():
        success, image = cap.read()
        if not success:
          print("Ignoring empty camera frame.")
          # If loading a video, use 'break' instead of 'continue'.
          break
        image,h,w = resize_image(image)
        image, results =pose_process_image(image, pose)
        #try:
        landmarks = results.pose_landmarks.landmark 
        angles , max_angle_right = plot_angles_from_frames(mp_pose, landmarks, image, h, w, max_angle_right)
        frames.append(angles)
        image = draw_landmarks(results, mp_drawing,mp_pose,image)
        out.write(image)
        #cv2.imshow("window", image) # in python IDE, change cv2_imshow to cv2.imshow('title of frame/image', image)
        outImageFile = f"{image_name}/{image_name}{img_count}.jpg"
        cv2.imwrite(outImageFile, image)
        img_count += 1
        #except ValueError:
            #print("#########################")
        #    print("Error!")
        #    print(ValueError)
        #    pass
        if cv2.waitKey(5) & 0xFF == 27:
          break

    cap.release()
    out.release()

    return frames, max_angle_right

coach_frames, max_angle_right = get_frames_angles(image_name = "coach", video_path = r"")
coach_frames = add_stage(coach_frames, max_angle_right)

student_frames, max_angle_right = get_frames_angles(image_name = "student", video_path = r"")
student_frames = add_stage(student_frames, max_angle_right)
