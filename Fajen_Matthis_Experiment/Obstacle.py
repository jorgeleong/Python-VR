'''
Obstacle class
Defines obstacles that come in pairs and are equidistant
'''
import vector
import vizshape
import viz
import vizact

'''
	Obstacle constructor
	Base class for all obstacles, generates movement actions
		x 				distance determined by path's x-midpoint +/- (distance/2) for each obstacle
		y 				is constant for this experiment
		z 				is obtained by random function
		zf				Final z position of obstacle
		shoulder_width	shoulder width of participant, affects the final x position of obstacle
		TTC				Time to close - time variable for gates to arrive at final position
'''
class Obstacle: 
# Create constructor: input position and integer that represents distance

	def __init__(self, x, y, z, zf, shoulder_width,TTC):
		# Width requires float variable, else round up...
		self.s_width = float(shoulder_width)/2
		self.TTC = float(TTC)
		self.position1 = [x, y, z]
		self.position2 = [-x, y, z]
		self.finalpos1 = [self.s_width, y, zf]
		self.finalpos2 = [-self.s_width, y, zf]
		self.act1 = vizact.moveTo(self.finalpos1,self.position1, time = self.TTC)
		self.act2 = vizact.moveTo(self.finalpos2,self.position2, time = self.TTC)
		self.disappear = vizact.fadeTo(0,time = 0)
		self.pause = vizact.waittime(1)
		self.FagenSequence = vizact.sequence(self.pause,self.disappear)
	def __str__(self):
		return ('For first obstacle: %.2f, %.2f, %.2f')%(self.position1[0], self.position1[1], self.position1[2])+('\nFor second obstacle: %.2f, %.2f, %.2f')%(self.position2[0], self.position2[1], self.position2[2])+"\nTime to close: %.2f"%(self.TTC)


#cylinders = Obstacle(3.0, 2.0, 8.0)
#print 'Results! '
#print cylinders