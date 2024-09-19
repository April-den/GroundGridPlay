"""
Visulize a single frame
"""
import open3d as o3d
import numpy as np
data = np.loadtxt('/home/aiyang/groundgrid/pcd/004397.txt', delimiter='\t')
points = data[:,:3]
labels = data[:,3].astype(int)
print(points)
# ponitAxis = o3d.geometry.PointCloud()
# ponitAxis.points = o3d.utility.Vector3dVector([[1,0,0],[0,1,0],[0,0,0],[1.95,0,-1.73]])
# axiColor = np.array([[1,0,0],[1,0,0],[1,0,0],[1,0,0]])
# ponitAxis.colors = o3d.utility.Vector3dVector(axiColor)


point_cloud = o3d.geometry.PointCloud()
point_cloud.points = o3d.utility.Vector3dVector(points)
colors = np.zeros((points.shape[0], 3))
colors[labels == 49] = [0,1,0]
colors[labels == 99] = [1,0,0]
point_cloud.colors = o3d.utility.Vector3dVector(colors)
o3d.visualization.draw_geometries([point_cloud])