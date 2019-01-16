class Cylinder:
    pi=3.14  
    def __init__(self,height,radius):
        self.height=height
        self.radius=radius

          
    def volume(self):
       vol=self.pi*self.radius*self.radius*self.height
       print(vol)

    def surfacearea(self):
        sa=2*self.pi*self.radius*self.radius+2*self.pi*self.radius*self.height
        print(sa)
       




obj=Cylinder(1,1)

obj.volume()

obj.surfacearea()

