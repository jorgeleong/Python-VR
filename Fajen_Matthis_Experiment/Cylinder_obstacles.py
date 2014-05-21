'''
Cylinder class 
Inherits from obstacle - creates cylinder type obstacles
'''
import Obstacle
import vizshape
import vizinfo
import viz
import vector
import vizact
import random

'''
	Cylinder constructor
	Creates cylinder shaped obstacle that will not be present at the beginning of trial
		pos_vector	vector object for position
		fin_depth	Z coordinate of end position of obstacle
		shoulder	shoulder width of participant
		TTC			Time to close - number of seconds the gates will close
		color		color of cylinder pair
		radius		radius of cylinder pair
		height		height of cylinder pair
'''
class Cylinder(Obstacle.Obstacle,object):
	def __init__(self, pos_vector, fin_depth, shoulder, TTC, color_vector, radius, height):
		super(Cylinder,self).__init__(pos_vector.x,pos_vector.y,pos_vector.z, fin_depth, shoulder, TTC)
		self.radius = radius
		self.height = height
		self.cyl_Left = vizshape.addCylinder(self.height, self.radius)
		self.cyl_Right = vizshape.addCylinder(self.height, self.radius)
		self.cyl_Left.color (color_vector.x, color_vector.y, color_vector.z)
		self.cyl_Right.color (color_vector.x, color_vector.y, color_vector.z)
		self.cyl_Left.setPosition(self.position1)
		self.cyl_Right.setPosition(self.position2)
		self.disapr()
	def disapr(self):
		self.cyl_Left.alpha(0)
		self.cyl_Right.alpha(0)
	def reappear(self):
		self.cyl_Left.alpha(1)
		self.cyl_Right.alpha(1)

viz.setMultiSample(4)
viz.fov(60)
viz.go()

# Add the ground plane
ground = viz.addChild('ground.osgb')

##################FOREST
bambooForest1 = []
bambooForest2 = []

# add 200 bamboo trees to each forest
for i in range(0, 200, 1):
	bambooForest1.append(vizshape.addCylinder(random.randint(10,16),0.1))
	bambooForest2.append(vizshape.addCylinder(random.randint(10,16),0.1))
	bambooForest1[i].setPosition(random.randint(-16,-3),0.5,random.randint(-20,20))
	bambooForest2[i].setPosition(random.randint(3,16),0.5,random.randint(-20,20))
	bambooForest1[i].color(0.3,0.8,0.3)
	bambooForest2[i].color(0.3,0.8,0.3)
################FOREST

# Move back cam to see shape immediately
viz.MainView.move([0,0,-10])

col = vector.vector(0.8, 0.4, 0.4)
position = vector.vector(8, 2, 8)
# values must be float
#Cylinder(pos_vector, fin_depth, shoulder, TTC, color_vector, radius, height)
sample = Cylinder(position, 3.0, 1,2.5, col, 0.2, 10)

wii = viz.add('wiimote.dle')#Add wiimote extension
wiimote = wii.addWiimote()

print sample
print "Final x position for left and right cylinder respectively: %.2f, %.2f"%(sample.finalpos1[0], sample.finalpos2[0])

# Function to read in wiimote input
def simplePrint(key):
	if key == wii.BUTTON_B:
		sample.reappear()
	elif key == wii.BUTTON_A:
		sample.reappear()
		sample.cyl_Left.addAction(sample.act1,pool=0)
		sample.cyl_Left.addAction(sample.FagenSequence,pool=1)
		sample.cyl_Right.addAction(sample.act2,pool=0)
		sample.cyl_Right.addAction(sample.FagenSequence,pool=1)
#	messageWindow.remove()

# Listener for wiimote
vizact.onsensordown(wiimote,wii.BUTTON_B,simplePrint,wii.BUTTON_B)
vizact.onsensordown(wiimote,wii.BUTTON_A,simplePrint,wii.BUTTON_A)

