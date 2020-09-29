from numpy import exp, zeros, meshgrid, linspace
from pylab import imshow, show, colorbar, quiver, streamplot

def f(x,y):
    return exp(-(x**2 + y**2)/width**2)
    
# constants
L = 1.0                     # size of square
N = 100                     # number of grid points on a side
a = L/N                     # grid point spacing
width = 0.2                 # width of concentration profile
Z = zeros([N,N], float)     # empty matrix for height
DX = zeros([N,N], float)    # empty matrix for gradient
DY = zeros([N,N], float)    # empty matrix for gradient

# calculate height profile
for i in range(N):
    y = -L/2 + i*a
    
    for j in range(N):
        x = -L/2 + j*a
        
        Z[i,j] = f(x,y)

# plot the results
imshow(Z, extent=[-L/2, L/2, -L/2, L/2], cmap="plasma")        
colorbar()
show()
