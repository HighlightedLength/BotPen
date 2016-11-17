import numpy as np
import cmath

def to_polar(pt):
    return cmath.polar(complex(pt[0],pt[1]))

def estimate_shape_orientation(shape_pts,obs_pts):
    pt_count = len(shape_pts)

    shape_polars = [to_polar(pt) for pt in shape_pts]
    obs_polars = [to_polar(pt) for pt in obs_pts]

    phasors = [
        (   shape_polars[i][0] * obs_polars[i][0],
            shape_polars[i][1] - obs_polars[i][1]
        )
        for i in range(pt_count)
    ]

    total = np.sum(phasors,0)

    offset = 0 if phasors[0] > 0 else np.pi

    return total[1] + offset
