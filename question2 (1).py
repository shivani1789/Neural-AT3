import numpy as np

random_vector = np.random.uniform(1, 20, 20)
# print(random_vector)
reshaped_array = random_vector.reshape(4, 5)
reshaped_array[np.arange(reshaped_array.shape[0]), reshaped_array.argmax(axis=1)] = 0
print(reshaped_array)