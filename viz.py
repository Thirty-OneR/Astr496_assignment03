import numpy as np
from mpi4py import MPI
import matplotlib.pyplot as plt

N=1024*1024
position=np.random.normal(size=(N,2))
v,x,y=np.histogram2d(position[:0],position[:1],
		bins = mgrid[-1.0:1.0:256j] )

v=MPI.COMM_WORLD.allreduce(v, MPI.SUM)
plt.imshow(v)
plt.savefig('hi.png')



