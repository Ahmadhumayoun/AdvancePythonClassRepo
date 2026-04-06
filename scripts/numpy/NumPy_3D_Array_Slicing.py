import numpy as np
slicingMatric = np.array(range(60)).reshape(2,5,6)
print(slicingMatric[0,1:4,1:6:2])
