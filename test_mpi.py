from mpi4py import MPI
import numpy as np
'''
N=100
np.random.seed(0x4d3d3d3)
arr=np.random.random(N)
my_num=N/MPI.COMM_WORLD.size

my_sum=arr[my_num*MPI.COMM_WORLD.rank: my_num* (MPI.COMM_WORLD.rank+1)].sum()
total=MPI.COMM_WORLD.allreduce(my_sum,MPI.SUM)

print(total)
'''
N=1024
total_N=1024*MPI.COMM_WORLD.size

if MPI.COMM_WORLD.rank==0:
	for i in range(MPI.COMM_WORLD.size-1):
		arr=np.random.random(N)
		print('send', arr)
		MPI.COMM_WORLD.send(arr,dest=i+1)
else:
	input_arr=np.empty(N,dtype='float64')
	value=MPI.COMM_WORLD.recv([input_arr,MPI.DOUBLE],source=0)
	print('recieved', input_arr.sum())
print('entering barrier', MPI.COMM_WORLD.rank)
MPI.COMM_WORLD.barrier()
print('exiting barrier', MPI.COMM_WORLD.rank)
