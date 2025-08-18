import numpy as np

a = np.array([1,2,3])
print(a)
print(type(a[0]))
print(a.shape)
print(a.ndim)
print(a.itemsize)
print(a.size)

# accessing specific elements rowa,columns

b= np.array([[1,2,3],[4,5,6],[7,8,9]])
#print(b[2,1])
#print(b[1,:]) # get specific row
#print(b[1:,])
print(b[1,1:]) #o/p [5,6]
print(b[1:,1:]) #o/p [[5,6],[8,9]]

#copy
c = a   # not a real copy!
c[0] = 99
print(a)  # [99  2  3] → original changed too

#real copy
c = a.copy()
c[0] = 99
print(a)  # [1 2 3] → unchanged

print(a.dtype)     # int64 (depends on system)
f = np.array([1,2,3], dtype='float32')
print(f, f.dtype)  # [1. 2. 3.] float32


print(np.zeros((2,3)))      # 2x3 array of zeros
print(np.ones((2,3)))       # 2x3 array of ones
print(np.full((2,3), 7))    # 2x3 array filled with 7
print(np.eye(3))            # identity matrix (3x3)
print(np.arange(0,10,2))    # [0 2 4 6 8]
print(np.linspace(0,1,5))   # [0.   0.25 0.5  0.75 1. ]


x = np.array([1,2,3])
y = np.array([4,5,6])

print(x + y)     # [5 7 9]
print(x * y)     # elementwise multiply [4 10 18]
print(x.dot(y))  # dot product = 32
print(np.sqrt(x)) # [1. 1.41 1.73]

print(b.sum())       # 45
print(b.mean())      # 5.0
print(b.max())       # 9
print(b.min())       # 1
print(b.sum(axis=0)) # column sums [12 15 18]
print(b.sum(axis=1)) # row sums [6 15 24]


print(np.random.rand(3,3))   # random floats (0-1)
print(np.random.randint(10, size=(3,3))) # random ints 0-9
