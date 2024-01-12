import imageio.v3 as iio
import scipy.linalg as la
import numpy as np
import matplotlib.pyplot as plt

def compress(U, s, Vh, k):
    return (U[0:Vh.shape[0], 0:k], s[0:k], Vh[0:k, 0:Vh.shape[1]])
def combine(U, s, Vh):
    size = (U.shape[1], Vh.shape[0])
    sigma = np.zeros(size)
    for i in range(min(size[0], size[1])):
        sigma[i, i] = s[i]
    a1 = np.dot(U, np.dot(sigma, Vh))
    return a1
def get_size(U, s, Vh):
    return np.size(U) + np.size(s) + np.size(Vh)

im = iio.imread('C:\\Users\\20233259\\Documents\\Programming\\Y1Q2\\LAA\\Project\\Assignment_6a\\rename.png')
pixels = []
for i in range(im.shape[0]):
    for j in range(im.shape[1]):
        pixels.append(sum(im[i][j])/4/255)
pixels = np.array(pixels)
pixels = pixels.reshape(im.shape[0], im.shape[1])

level = 72

svd = la.svd(pixels, full_matrices=False)
# plt.plot(np.log(svd[1]))
# plt.axvline(x = 291, color = 'r', linestyle = '-')
# plt.axvline(x = 145, color = 'r', linestyle = '-')
# plt.axvline(x = 72, color = 'r', linestyle = '-')
# plt.xlabel("Singular value index")
# plt.ylabel("Log of Singular value")

half = compress(svd[0], svd[1], svd[2], level)
a1 = combine(half[0], half[1], half[2])

ratio = get_size(half[0], half[1], half[2]) / im.shape[0] / im.shape[1]

plt.imshow(a1, cmap='gray')
plt.title('k = ' + str(level) + ' compression = ' + str(ratio))
plt.show()