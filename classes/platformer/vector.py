class V2(object):
    def __init__(self,x=0,y=0):
        self.x, self.y = x, y

    def add(self,V2):
    	self.x += V2.x
    	self.y += V2.y