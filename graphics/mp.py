'''
This is a wrapper for the multiprocessing import that
handles cross platform threading
'''
print("handling mp")
import multiprocessing
import os
if os.name == 'nt':
    # linux uses fork
    multiprocessing.set_start_method('spawn')