from Robot import Robot
from matplotlib import pyplot as plt
from scipy.spatial import Voronoi, voronoi_plot_2d

points=[(0,0),(1,1),(2,1),(3,3),(5,4)]
startPoint=points[0]
goalPoint=points[points.__len__()-1]
problem=Robot(startPoint[0],startPoint[1],goalPoint[0],goalPoint[1],points)


vor=Voronoi(points)
print vor.ridge_vertices
print vor.regions
print vor.ridge_points
voronoi_plot_2d(vor)
plt.xlim(-1,7)
plt.ylim(-1,7)
plt.show()




