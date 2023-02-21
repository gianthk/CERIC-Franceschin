import h5py
import numpy as np
read = False

list1 = list(range(2,11))
arr1 = np.ndarray([120], 'uint8')
# print(arr1)

with h5py.File("foo.hdf5", "w") as f:
    g1 = f.create_group("results")
    g1.create_dataset("onelist", data=list1, dtype='uint8')
    g1.create_dataset("onearray", data=arr1, dtype='uint8')
    g11 = g1.create_group("spam")
    g11.create_dataset("anotherarray", data=arr1*0.345, dtype='float')

# read
if read:
    import h5py
    f = h5py.File('test/foo.hdf5', 'r')
    list(f.keys())
    res = f['results']
    list(res.keys())
