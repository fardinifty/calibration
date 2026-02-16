import numpy as np

H = np.array([
    [ 3.13906045e-01,  4.59214504e-02,  1.17664009e+02],
    [-2.60329492e-03,  6.17787119e-01, -1.25708906e+02],
    [-6.75754769e-04,  1.21594080e-04,  1.00000000e+00]
])

img_pts = [
    (433,205),
    (218,355),
    (226,250),
    (283,147),
    (437,101),
    (538,155),
    (591,314),
    (652,105)
]

def pixel_to_robot(u,v):

    p = np.array([u,v,1]).reshape(3,1)

    pr = H @ p

    pr = pr / pr[2,0]

    return pr[0,0], pr[1,0]


print("Validation results:\n")

for pt in img_pts:

    X,Y = pixel_to_robot(pt[0],pt[1])

    print(f"Pixel {pt} -> Robot ({X:.1f},{Y:.1f})")
