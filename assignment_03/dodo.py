from doit.tools import run_once
import h5py
import numpy as np

def task_generate_plot():
	action=[['python3','main.py']]
	return {'actions': action}
