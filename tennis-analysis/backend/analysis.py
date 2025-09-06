from main import *
from sklearn.cluster import KMeans
import numpy as np
import sys

student_n_cluster = 5
print(student_n_cluster)
X = np.array(student_frames)
kmeans_student = KMeans(n_clusters=student_n_cluster, random_state=0.fit(X)
print(kmeans_student.labels_)

n_cluster_coach = 5
X = np.array(coach_frames)
kmeans_coach = KMeans(n_clusters=n_cluster_coach, random_state=0.fit(X)
print(kmeans_coach.labels_)

def get_nearest_neighbor(image, indexes, frames):
  a = np.array(image)
  min_dist = sys.maxsize
  nearrest = indexes[0]
  for idx in indexes:
    b = np.array(frames[idx])
    dist = np.linalg.norm(a-b)
    if min_dist > dist:
      nearest = idx
      min_dist = dist
      print(min_dist, nearest)
    return nearest

from IPython.display import Image, display
from random import radint

student_cluster = []
start = 0
for i in range(1, len(kmeans_student.labels_)):
  if kmeans_student.labels_[i] != kmeans_student.labels_[i-1]:
    student_cluster.append({'label':kmeans_student.labels_[i-1], 'start':start, 'end':i})

print(student_cluster)
used = set()
for label in (student_cluster):
  if label['label'] in used:
    continue
  used.add(label['label'])
  print('label:' , label['label'])
  index_student = np.where(kmeans_student.labels_ = label['label'])
  rand=len(index_student)//2
  print('student image ', index_student[0][rand])
  predict = kmeans_coach.predict([student_frames[index_student[0][rand]]])
  orubt('predict:',predit)
  indexes_frame = np.where(kmeans_coach.labels_ == predict[0])
  nearest = get_nearest_neighbor(student_frames[index_student[0][rand]], indexes_frame[0] , coach_frames)
  print('coach', nearest)
  display(Image(f'student/student{index-student[0][rand]+1}.jpg'))
  display(Image(f'coach/coach{nearest}.jpg'))
