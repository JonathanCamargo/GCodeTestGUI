import numpy as np
from scipy.spatial.transform import Rotation as R

kPatterns=['spiral','s']

def trajectory2gcode(points):
    gcode=[]
    for i in range(points.shape[0]):
        gcode.append('G01 X{:1.2f} Y{:1.2f}'.format(points[i,0],points[i,1]))
    gcode='\n'.join(gcode)
    return gcode

def patternCreator(pattern='spiral'):
    if pattern=='spiral':
        pat=np.array([[0,0],
        [0,1],
        [1,1],
        [1,0.1],
        [0.1,0.1]])
        p=pat
        maxiters=6
        for loop in range(0,maxiters):
            newPattern=pat*(0.8)**(loop+1)+p[-1,:]
            p=np.concatenate([p,newPattern])
    elif pattern=='s':
        maxiters=6
        dy=1.0/((maxiters+1)*2)
        pat=np.array([[0,0],
        [1,0],
        [1,1.0*dy],
        [0,1.0*dy],
        [0,2.0*dy]])
        p=pat
        for loop in range(0,maxiters):
            newPattern=pat+p[-1,:]
            p=np.concatenate([p,newPattern])
        
    else:
        error
    return p-np.array([0.5,0.5])

def createPattern(pattern='spiral',xmin=0,xmax=100,ymin=0,ymax=100,ang_deg=0):
    points=patternCreator(pattern)
    dx=xmax-xmin
    dy=ymax-ymin
    c=np.array([xmin+(xmax-xmin)/2,ymin+(ymax-ymin)/2])
    ang=np.deg2rad(ang_deg)
    r = R.from_rotvec(-ang* np.array([0, 0, 1])).as_matrix()[0:2,0:2]
    points=np.matmul(points,r)
    maxpoints=np.array([points[:,0].max(),points[:,1].max()])
    minpoints=np.array([points[:,0].min(),points[:,1].min()])
    dif=maxpoints-minpoints
    cpoints=np.array([maxpoints[0]+(maxpoints[0]-minpoints[0])/2,maxpoints[1]+(maxpoints[1]-minpoints[1])/2])
    #rescale to fit dimensions
    r=0.8*np.array([[dx/dif[0],0],[0,dy/dif[1]]])
    points=np.matmul(points,r)-cpoints+c
    #recenter to bed center
    return points
