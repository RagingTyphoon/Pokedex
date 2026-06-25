import math

# CLASS CREATION
# A "blueprint" for creating objects
class Point2D:
    '''
    This class represents a point in two dimensional space
    '''

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        '''
        Controls how the point is printed when print() is called
        '''
        return f"({self.x}, {self.y})"

    def distance_to(self, other_point):
        distance = math.hypot(self.x - other_point.x, self.y - other_point.y)
        # distance = math.sqrt( (self.x - other_point.x)**2 + (self.y - other_point.y)**2 )
        return distance

point_one = Point2D(3, 4)
print("Point one:", point_one)
point_two = Point2D(5, 6)
print("Point two:", point_two)

print(point_one.distance_to(point_two))

point_three = Point2D(0, 0)
point_four = Point2D(3, 4)
print(point_three.distance_to(point_four))


'''
DICTIONARIES

These are data structures that basically work like a dictionary.
That is, they are like lists of "key-value" pairs. In a dictionary,
the "key" is a word, and the "value" is a definition.

In Python, dictionaries are declared like so:

new_dict = {
    "key_one": "value_one",
    "key_two": "value_two"
}

If you want to access individual entries in your dictionary,
you must use the dictionary name, square brackets, and the key
inside the square brackets:

variable = new_dict["key_one"]          # THIS will set variable to "value_one"
'''

def find_furthest_point(origin, points_dict):
    '''
    This function takes an origin point and a dictionary of points,
    then loops through the dictionary to find the point which
    is furthest from the origin. Finally, it returns the point.
    '''
    max_distance = -1
    furthest_label = None

    # Let's go through the dictionary's key-value pairs
    for label, point in points_dict.items():
        distance = origin.distance_to(point)
        if distance > max_distance:
            max_distance = distance
            furthest_label = label

    return furthest_label, max_distance


locations = {
    "Home": Point2D(0, 0),
    "McDonalds": Point2D(7, 8),
    "IHOP": Point2D(9,0),
    "KFC": Point2D(1,1),
    "Chickfilla": Point2D(1,2)
}

home = locations["Home"]
print(home)

furthest_from_home, furthest_distance = find_furthest_point(Point2D(0, 0), locations)
print(furthest_from_home, "is", furthest_distance, "miles away")