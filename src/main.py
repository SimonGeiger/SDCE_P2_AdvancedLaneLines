'''
Layout of Algorithm:
  - camera class
    > calibration
    > brain
    > process image

  - image class
    > distortion
    > color transform + gradients
    > perspective transform
    > lane detection (init + continous)

  - line class
    > position
    > curvature
    > sanity check
    > tracking + smoothing

Layout of main:
  - test images
  - video

'''