# Input : x1, y1 = (3, 4)
#            x2, y2 = (7, 7)
# Output : 5

# Input : x1, y1 = (3, 4) 
#            x2, y2 = (4, 3)
# Output : 1.41421

import math

def distance(x1 , y1 , x2 , y2):
    return math.sqrt(math.pow(x2 - x1, 2) +
                math.pow(y2 - y1, 2))


print("%.6f"%distance(3, 4, 4, 3))