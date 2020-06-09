from skimage.color import rgb2gray
import numpy as np

def per_row_grayscale_var(painting, isGray=True, avg=False):
    if not isGray:
        painting = rgb2gray(painting)
        
    rows = painting.shape[0]
    row_variances = []
    
    for i in range(rows):
        row_variances.append(np.var(painting[i,:]))
    
    if avg:
        return np.mean(np.array(row_variances))
    
    return np.array(row_variances)

def edge_score(painting, isGray=True):
    if not isGray:
        painting = rgb2gray(painting)
        
    edges = ndimage.gaussian_gradient_magnitude(painting,sigma=1)
    plt.imshow(edges, cmap='gray')
    
    rows, cols = painting.shape
    
    row_avg = 0
    for r in range(rows):
        row_avg += sum(edges[r,:])
    row_avg /= rows
    
    col_avg = 0
    for c in range(cols):
        col_avg += sum(edges[:,c])
    col_avg /= cols
    
    
    return max(row_avg, col_avg)