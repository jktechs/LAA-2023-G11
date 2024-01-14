import scipy.linalg as la
import numpy as np
data = [-1, -2, 1, 2,  1, -2,  0, 2,  2,  1, 2, # Guy
        -1, -2, 2, 0, -2, -2,  1, 0, -1,  1, 2, # Akvile
        -2, -2, 2, 1, -2, -2, -2, 1,  1,  0, 1, # Remi
        -2,  0, 2, 1, -2,  1, -1, 0,  1,  0, 2, # Joris
        -1, -2, 1, 0, -1, -2, -2, 2, -2, -1, 1, # Jannick
        -2, -1, 1, 1,  2,  2,  0,0,0,0,0] # Damyan
data = np.array(data)
data = np.reshape(data, (6,11))
svd = la.svd(data, full_matrices=False)
def compress(U, s, Vh, k):
    return (U[0:Vh.shape[0], 0:k], s[0:k], Vh[0:k, 0:Vh.shape[1]])
def combine(U, s, Vh):
    size = (U.shape[1], Vh.shape[0])
    sigma = np.zeros(size)
    for i in range(min(size[0], size[1])):
        sigma[i, i] = s[i]
    a1 = np.dot(U, np.dot(sigma, Vh))
    return a1
lower = compress(svd[0], svd[1], svd[2], 2)
a = combine(lower[0], lower[1], lower[2])
print(a)

# 5 0.01333316  0.13657602 -0.07240646 -0.04415701  0.22937771
# 4 -0.82036812  0.41498545  0.88946355 -0.28839771  0.03690892
# 3 0.06980741 -0.03837665  1.52255854  0.36896718  0.48484598
# 2 -0.82036812  0.41498545  0.88946355 -0.28839771  0.03690892