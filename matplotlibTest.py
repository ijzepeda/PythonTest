 from matplotlib import pyplot as plt
import numpy as np
import pylab as pl
ds= np.random.normal(5.0,3.0,1000)
pl.hist(ds)
pl.xlabel('dataset')
pl.show()