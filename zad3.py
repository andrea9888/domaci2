class Line:
    def __init__(self,koordinate1, koordinate2):
        self.x1=koordinate1[0]
        self.y1=koordinate1[1]
        self.x2=koordinate2[0]
        self.y2=koordinate2[1]
    def slope(self):
        return (self.y2-self.y1)/(self.x2-self.x1)
    def distance(self):
        return ((self.x2-self.x1)**2+(self.y2-self.y1)**2)**(1/2)
A=Line((3,2),(8,10))
print(A.distance())
print(A.slope())
