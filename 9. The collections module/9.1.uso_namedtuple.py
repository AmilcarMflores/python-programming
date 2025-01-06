# vision = (9.5, 8.8)

# # Ojo izquierdo
# left = vision[0] # 9.5

# # Ojo derecho
# right = vision[1] # 8.8

from collections import namedtuple

Vision = namedtuple('Vision', ['left', 'combined', 'right'])
vision = Vision(9.5, 9.2, 8.8)

# Ojo izquierdo
vision.left # 9.5
vision.right # 8.8
vision.combined # 9.2