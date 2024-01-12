import imageio.v3 as iio
import scipy.linalg as la

def compress(U, s, Vh, a):
    return (U, s, Vh)

im = iio.imread('C:\\Users\\20233259\\Documents\\Programming\\Y1Q2\\LAA\\Project\\Assignment_6a\\rename.png')
pixels = []
for i in range(im.shape[0]):
    for j in range(im.shape[1]):
        pixels.append(sum(im[i][j])/4/255)
pixels.reshape(im.shape[0], im.shape[1])
svd = la.svd(pixels)

half = compress(svd.U, svd.s svd.Vh)