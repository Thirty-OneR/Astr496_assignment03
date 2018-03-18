import mpi4py as mpi
import numpy as np

N=1024

if mpi.COMM_WORLD.rank==0:
	arr=np.random.random(N)
else:
	arr=np.empty(N)

print(mpi.COMM_WORLD.rank,arr)
mpi.COMM_WORLD.Barrier()
mpi.COMM_WORLD.Bcast([arr, mpi.DOUBLE],root=0)
print(mpi.COMM_WORLD.rank,arr)
