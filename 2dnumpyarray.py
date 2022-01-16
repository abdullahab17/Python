# Create baseball, a list of lists
baseball = [[180, 78.4],
            [215, 102.7],
            [210, 98.5],
            [188, 75.2]]

# Import numpy
import numpy as np

# Create a 2D numpy array from baseball: np_baseball
np_baseball = np.array(baseball)
print(np_baseball)
# Print out the type of np_baseball
print(type(np_baseball))

# Print out the shape of np_baseball
print(np_baseball.shape)
#----------------------------------------

x = [["a", "b"], ["c", "d"]]
print([x[0][0], x[1][0]])

np_x = np.array(x)
print(np_x[:,0])

