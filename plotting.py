#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Bounding box plotting and cropping
import numpy as np
from shapely.geometry import Polygon
def weighted_merge(g, p):
    g[:8] = (g[8] * g[:8] + p[8] * p[:8])/(g[8] + p[8])
    g[8] = (g[8] + p[8])
    return g
if __name__ == '__main__':
    # 343,350,448,135,474,143,369,359
    print(Polygon(np.array([[343, 350], [448, 135],
                            [474, 143], [369, 359]])).area)
    

