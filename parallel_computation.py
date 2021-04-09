from joblib import Parallel, delayed
import multiprocessing
from functools import partial
def foo(arg1, arg2, arg3, arg4):
    '''
    body of the function
    '''
    return output
input = [11,32,44,55,23,0,100,...] # arbitrary list
# num_cores = multiprocessing.cpu_count()
foo_ = partial(foo, arg2=arg2, arg3=arg3, arg4=arg4)
# arg1 is being fetched from input list
output = Parallel(n_jobs=num_cores)(delayed(foo_)(i) for i in input)
