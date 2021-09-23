#ORB-SLAM2 vs RTAB-Map with RGB-D and stereo camera
from google.colab import files
import numpy as np
import matplotlib.pyplot as plt
import io
import pandas as pd

#Ground Truth
ground_truth = files.upload()

#Upload data trajectory robot in indoor ORB-SLAM2 and RTAB-Map RGB-D and stereo camera
data_orb_slam2_RGBD = files.upload()

data_orb_slam2_stereo = files.upload()

data_rtabmap_RGBD = files.upload()

data_rtabmap_stereo = files.upload()

file_ground_truth = next(iter(ground_truth))

file_orb_slam2_RGBD = next(iter(data_orb_slam2_RGBD))
file_orb_slam2_stereo = next(iter(data_orb_slam2_stereo))
file_rtabmap_RGBD = next(iter(data_rtabmap_RGBD))
file_rtabmap_stereo = next(iter(data_rtabmap_stereo))

string_ground_truth = io.StringIO(ground_truth[file_ground_truth].decode('ISO 8859-1').strip())

string_orb_slam2_RGBD = io.StringIO(data_orb_slam2_RGBD[file_orb_slam2_RGBD].decode('ISO 8859-1').strip())
string_orb_slam2_stereo = io.StringIO(data_orb_slam2_stereo[file_orb_slam2_stereo].decode('ISO 8859-1').strip())
string_rtabmap_RGBD = io.StringIO(data_rtabmap_RGBD[file_rtabmap_RGBD].decode('ISO 8859-1').strip())
string_rtabmap_stereo = io.StringIO(data_rtabmap_stereo[file_rtabmap_stereo].decode('ISO 8859-1').strip())

df_ground_truth = pd.read_csv(string_ground_truth)

df_orb_slam2_RGBD = pd.read_csv(string_orb_slam2_RGBD)
df_orb_slam2_stereo = pd.read_csv(string_orb_slam2_stereo)
df_rtabmap_RGBD = pd.read_csv(string_rtabmap_RGBD)
df_rtabmap_stereo = pd.read_csv(string_rtabmap_stereo)

df_ground_truth_x = []
df_ground_truth_y = []
df_ground_truth_z = _

#Warning ! The coordenates it's changed between the Gazebo and ORB-SLAM2/RTAB-Map, then x = x, z = y. 
df_orb_slam2_RGBD_x = []
df_orb_slam2_RGBD_y = _
df_orb_slam2_RGBD_z = []

#Warning ! The coordenates it's changed between the Gazebo and ORB-SLAM2/RTAB-Map, then x = x, z = y. 
df_orb_slam2_stereo_x = []
df_orb_slam2_stereo_y = _
df_orb_slam2_stereo_z = []

#Warning ! The coordenates it's changed between the Gazebo and ORB-SLAM2/RTAB-Map, then x = x, z = y. 
df_rtabmap_RGBD_x = []
df_rtabmap_RGBD_y = _
df_rtabmap_RGBD_z = []

#Warning ! The coordenates it's changed between the Gazebo and ORB-SLAM2/RTAB-Map, then x = x, z = y. 
df_rtabmap_stereo_x = []
df_rtabmap_stereo_y = _
df_rtabmap_stereo_z = []

for i in range(0, len(df_ground_truth['---']), 4):
  df_ground_truth_x.append( float(df_ground_truth['---'][i].split('x: ')[1]))
  df_ground_truth_y.append( float(df_ground_truth['---'][i+1].split('y: ')[1]))
  #df_ground_truth_z.append( float(df_ground_truth['---'][i+2].split('z: ')[1]))

for z in range(len(df_orb_slam2_RGBD['id x y z'])):
  df_orb_slam2_RGBD_x.append( float(df_orb_slam2_RGBD['id x y z'][z].split(' ')[1]))
  #df_orb_slam2_RGBD_y.append( float(df_orb_slam2_RGBD['id x y z'][z].split(' ')[2]))
  df_orb_slam2_RGBD_z.append( float(df_orb_slam2_RGBD['id x y z'][z].split(' ')[3]))

for z in range(len(df_orb_slam2_stereo['id x y z'])):
  df_orb_slam2_stereo_x.append( float(df_orb_slam2_stereo['id x y z'][z].split(' ')[1]))
  #df_orb_slam2_RGBD_y.append( float(df_orb_slam2_RGBD['id x y z'][z].split(' ')[2]))
  df_orb_slam2_stereo_z.append( float(df_orb_slam2_stereo['id x y z'][z].split(' ')[3]))

for i in range(0, len(df_rtabmap_RGBD['---']), 4):
  df_rtabmap_RGBD_x.append( float(df_rtabmap_RGBD['---'][i].split('x: ')[1]))
  #df_rtabmap_RGBD_y.append( float(df_ground_truth['---'][i+1].split('y: ')[1]))
  df_rtabmap_RGBD_z.append( float(df_rtabmap_RGBD['---'][i+2].split('z: ')[1]))

for i in range(0, len(df_rtabmap_stereo['---']), 1):
  df_rtabmap_stereo_x.append( float(df_rtabmap_stereo['---'][i].split('\t')[1]))
  df_rtabmap_stereo_z.append( float(df_rtabmap_stereo['---'][i].split('\t')[2]))

plt.plot(df_ground_truth_x[0:len(df_ground_truth_x):1] , df_ground_truth_y[0:len(df_ground_truth_y):1], label='ground truth', color='k')
plt.plot(df_orb_slam2_RGBD_x[0:len(df_orb_slam2_RGBD_x):1] , df_orb_slam2_RGBD_z[0:len(df_orb_slam2_RGBD_z):1], label='ORB-SLAM2 RGBD', color='r')
plt.plot(df_orb_slam2_stereo_x[0:len(df_orb_slam2_stereo_x):1] , df_orb_slam2_stereo_z[0:len(df_orb_slam2_stereo_z):1], label='ORB-SLAM2 stereo', color='g')
plt.plot(df_rtabmap_RGBD_x[0:len(df_rtabmap_RGBD_x):1] , df_rtabmap_RGBD_z[0:len(df_rtabmap_RGBD_z):1], label='RTAB-Map RGBD', color='y')
plt.plot(df_rtabmap_stereo_x[0:len(df_rtabmap_stereo_x):1] , df_rtabmap_stereo_z[0:len(df_rtabmap_stereo_z):1], label='RTAB-Map stereo', color='m')
plt.legend()
plt.show() 

#Transformando em array
df_ground_truth_x = np.array(df_ground_truth_x)
df_ground_truth_y = np.array(df_ground_truth_y)

df_orb_slam2_RGBD_x = np.array(df_orb_slam2_RGBD_x)
df_orb_slam2_RGBD_z = np.array(df_orb_slam2_RGBD_z)

df_orb_slam2_stereo_x = np.array(df_orb_slam2_stereo_x)
df_orb_slam2_stereo_z = np.array(df_orb_slam2_stereo_z)

df_rtabmap_RGBD_x = np.array(df_rtabmap_RGBD_x)
df_rtabmap_RGBD_z = np.array(df_rtabmap_RGBD_z)

df_rtabmap_stereo_x = np.array(df_rtabmap_stereo_x)
df_rtabmap_stereo_z = np.array(df_rtabmap_stereo_z)

distance_df_ground_truth_x = []
distance_df_ground_truth_y = []

distance_df_orb_slam2_RGBD_x = []
distance_df_orb_slam2_RGBD_z = []

distance_df_orb_slam2_stereo_x = []
distance_df_orb_slam2_stereo_z = []

distance_df_rtabmap_RGBD_x = []
distance_df_rtabmap_RGBD_z = []

distance_df_rtabmap_stereo_x = []
distance_df_rtabmap_stereo_z = []

#Math of trajectory
for i in range(len(df_ground_truth_x) - 1):
  distance_df_ground_truth_x.append(abs(df_ground_truth_x[i] - df_ground_truth_x[i+1]))
  distance_df_ground_truth_y.append(abs(df_ground_truth_y[i] - df_ground_truth_y[i+1]))

#Math of trajectory
for i in range(len(df_orb_slam2_RGBD_x) - 1):
  distance_df_orb_slam2_RGBD_x.append(abs(df_orb_slam2_RGBD_x[i] - df_orb_slam2_RGBD_x[i+1]))
  distance_df_orb_slam2_RGBD_z.append(abs(df_orb_slam2_RGBD_z[i] - df_orb_slam2_RGBD_z[i+1]))

#Math of trajectory
for i in range(len(df_orb_slam2_stereo_x) - 1):
  distance_df_orb_slam2_stereo_x.append(abs(df_orb_slam2_stereo_x[i] - df_orb_slam2_stereo_x[i+1]))
  distance_df_orb_slam2_stereo_z.append(abs(df_orb_slam2_stereo_z[i] - df_orb_slam2_stereo_z[i+1]))

#Math of trajectory
for i in range(len(df_rtabmap_RGBD_x) - 1):
  distance_df_rtabmap_RGBD_x.append(abs(df_rtabmap_RGBD_x[i] - df_rtabmap_RGBD_x[i+1]))
  distance_df_rtabmap_RGBD_z.append(abs(df_rtabmap_RGBD_z[i] - df_rtabmap_RGBD_z[i+1]))

#Math of trajectory
for i in range(len(df_rtabmap_stereo_x) - 1):
  distance_df_rtabmap_stereo_x.append(abs(df_rtabmap_stereo_x[i] - df_rtabmap_stereo_x[i+1]))
  distance_df_rtabmap_stereo_z.append(abs(df_rtabmap_stereo_z[i] - df_rtabmap_stereo_z[i+1]))

#Pitagoras
print('Trajetória ground Truth: ',  np.sqrt( sum(distance_df_ground_truth_x)**2 + sum(distance_df_ground_truth_y)**2 ) )
print('Trajetória orb_slam2_RGBD: ',  np.sqrt( sum(distance_df_orb_slam2_RGBD_x)**2 + sum(distance_df_orb_slam2_RGBD_z)**2 ) )
print('Trajetória orb_slam2_stereo: ',  np.sqrt( sum(distance_df_orb_slam2_stereo_x)**2 + sum(distance_df_orb_slam2_stereo_z)**2 ) )
print('Trajetória rtabmap_RGBD: ',  np.sqrt( sum(distance_df_rtabmap_RGBD_x)**2 + sum(distance_df_rtabmap_RGBD_z)**2 ) )
print('Trajetória rtabmap_stereo: ',  np.sqrt( sum(distance_df_rtabmap_stereo_x)**2 + sum(distance_df_rtabmap_stereo_z)**2 ) )

#Distance
ground_truth_trajectory =     np.sqrt( sum(distance_df_ground_truth_x)**2 + sum(distance_df_ground_truth_y)**2 )
orb_slam2_RGBD_trajectory =   np.sqrt( sum(distance_df_orb_slam2_RGBD_x)**2 + sum(distance_df_orb_slam2_RGBD_z)**2 )
orb_slam2_stereo_trajectory = np.sqrt( sum(distance_df_orb_slam2_stereo_x)**2 + sum(distance_df_orb_slam2_stereo_z)**2 )
rtabmap_RGBD_trajectory =     np.sqrt( sum(distance_df_rtabmap_RGBD_x)**2 + sum(distance_df_rtabmap_RGBD_z)**2 )
rtabmap_stereo_trajectory =   np.sqrt( sum(distance_df_rtabmap_stereo_x)**2 + sum(distance_df_rtabmap_stereo_z)**2 )

trajectory_all = [orb_slam2_RGBD_trajectory, orb_slam2_stereo_trajectory, rtabmap_RGBD_trajectory, rtabmap_stereo_trajectory]
trajectory_ground_truth = [ground_truth_trajectory, ground_truth_trajectory, ground_truth_trajectory, ground_truth_trajectory]

#Graph of the trajectory distance
plt.rc('figure', figsize = (15, 8))
area = plt.figure()

g1 = plt.plot(['orb_slam2_RGBD','orb_slam2_stereo','rtabmap_RGBD','rtabmap_stereo'], trajectory_ground_truth, label = 'Ground Truth', color = 'gray', marker='o')  
g2 = plt.bar(['orb_slam2_RGBD','orb_slam2_stereo','rtabmap_RGBD','rtabmap_stereo'], trajectory_all, label = 'Distances', color = 'c')

plt.title('Trajectory Distance')
plt.legend()
plt.plot()
