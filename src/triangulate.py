#!/usr/bin/python
import objectTrack as ot

import matplotlib
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt 



#Motion track each video and save the raw tracking data
#(numpy array : [x , y , radius])
print("Tracking Cam X...", end="")
xRaw = ot.trackVideo("../RenderOutput/set0/X/x.mp4")
print("done.\nTracking Cam Y...", end="")
yRaw = ot.trackVideo("../RenderOutput/set0/Y/y.mp4")
print("done.\nTracking Cam Z...", end="")
zRaw = ot.trackVideo("../RenderOutput/set0/Z/z.mp4")
print("done.")

#encode the tracking visualization as an mp4 video 
print("Encoding tracking frames as video...", end="")
ot.writeFrames("./track.mp4")


print("done.\nProcessing...", end="")
fig = plt.figure()
ax = Axes3D(fig)

ax.plot(xRaw[:,2],yRaw[:,2],zRaw[:,2])
print("done.")
plt.show()
