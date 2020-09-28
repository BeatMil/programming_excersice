import sys
class Vector2: # my own vector2; idea from godot
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def get_x(self):
        return self.x
    
    def set_x(self, new_x):
        self.x = new_x

    def get_y(self):
        return self.y
    
    def set_y(self, new_y):
        self.y = new_y
    
    def __repr__(self):
        return f'(%s,%s)'%(self.x, self.y)


motion = Vector2(1,2)
# print(motion.get_x())
# print(motion.get_y())
print(sys.version)
