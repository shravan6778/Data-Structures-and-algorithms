# Input: l1 = { 0, 10 }, r1 = { 10, 0 }, l2 = { 5, 5 }, r2 = { 15, 0 }
# Output: Rectangles Overlap

# Input: l1 = { 0, 10 }, r1 = { 10, 0 }, l2 = { -10, 5 }, r2 = { -1, 0 }
# Output: Rectangles Don't Overlap

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def do_overlap(l1, r1, l2, r2):
    # If one rectangle is to the left of the other
    if l1.x > r2.x or l2.x > r1.x:
        return False

    # If one rectangle is above the other
    if r1.y > l2.y or r2.y > l1.y:
        return False

    return True

# Driver code
if __name__ == "__main__":
    l1 = Point(0, 10)
    r1 = Point(10, 0)
    l2 = Point(12, 7)
    r2 = Point(12, 8)

    if do_overlap(l1, r1, l2, r2):
        print("Rectangles Overlap")
    else:
        print("Rectangles Don't Overlap")