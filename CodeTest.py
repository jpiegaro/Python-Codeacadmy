__author__ = 'Joel'
'''
Sandbox for Code Academy Python Course
'''

class Triangle(object):
    number_of_sides = 3
    def __init__(self,angle1,angle2,angle3):
        self.angle1=angle1
        self.angle2=angle2
        self.angle3=angle3
    def check_angles(self):
        if self.angle1+self.angle2+self.angle3 == 180:
            return True
        else:
            return False

my_triangle = Triangle(90,30,60)
print my_triangle.number_of_sides
print my_triangle.check_angles()

class Equilateral(Triangle):
    angle = 60
    def __init__(self):
        self.angle1,self.angle2,self.angle3 = self.angle,self.angle,self.angle
    def check_angles(self):
        if (self.angle1+self.angle2+self.angle3)/3 == 60:
            return True,'Checks out to 180, sir!'
        else:
            return False

test=Equilateral()
print test.number_of_sides
print test.angle
print test.check_angles()
