'''
Experiment class
Main class will hold participant data and print it to file 
also will have functions related to Fajen's experiment directly
'''
import random
import viz
import viztask
import vizact
import vizproximity
import vizinfo
import vizshape

import Cylinder_obstacles
import Participant
import vector

class Fajen_Experiment:
	'''
	Default constructor
	'''
	def __init__(self, obstacle, participant, speed):
		self.obstacle = obstacle
		self.critical_speed = speed
		self.participantSpeed = participant.speed
	# return a string instead of printing one
	def speedCompare(self):
		if (self.critical_speed > self.participantSpeed):
			self.passable = False
			print 'Impossible to pass. Required speed %.2f larger than participant\'s speed %.2f'%(self.critical_speed,self.participantSpeed)
		else:
			self.passable = True
			print 'Passable. Required speed %.2f, participant\'s speed %.2f'%(self.critical_speed,self.participantSpeed)
# This void function creates the bamboo Forest, replicating that which is found on Experiment 1 of Fajen et Al (2011)
	def bambooForest(self):
		# Add the ground plane
		ground = viz.addChild('ground.osgb')
		# Bamboo sticks
		bambooForest1 = []
		bambooForest2 = []
		
		# add 200 bamboo trees to each forest
		for i in range(0, 400, 1):
			bambooForest1.append(vizshape.addCylinder(random.randint(10,16),0.1))
			bambooForest2.append(vizshape.addCylinder(random.randint(10,16),0.1))
			bambooForest1[i].setPosition(random.randint(-16,-3),0.5,random.randint(-20,20))
			bambooForest2[i].setPosition(random.randint(3,16),0.5,random.randint(-20,20))
			bambooForest1[i].color(0.3,0.8,0.3)
			bambooForest2[i].color(0.3,0.8,0.3)
			
	def __str__(self):
		return '\n****Experiment data**** '+('\nCritical speed:\t\t\t%.2f m/s')%(self.critical_speed)+('\nTime to close:\t\t\t%.2f seconds')%(self.exp_time)+('\nGap at critical width:\t%.2f')%(self.exp_init_pos)

# Hard coded Time to close values and initial position
TTC = [1.2, 1.4, 1.6, 1.8, 2.0]
initPosition = [3, 4, 5]
# Size of arrays
len(initPosition)
len(TTC)
# choose the index of each 
indexofTTC = random.randint(0,len(TTC)-1)
indexofPos = random.randint(0,len(initPosition)-1)
exp_time = TTC[indexofTTC]
exp_init_pos = initPosition[indexofPos]
# minimum speed required by participant to pass
critical_speed = exp_init_pos/exp_time



wii = viz.add('wiimote.dle')#Add wiimote extension
wiimote = wii.addWiimote()

target = vizproximity.Target(viz.MainView)
exp_sensor = vizproximity.Sensor(vizproximity.RectangleArea([2,1],center=[0,3]),None)

exp_manager = vizproximity.Manager()
exp_manager.addSensor(exp_sensor)
exp_manager.addTarget(target)

exp_manager.setDebug(viz.ON)


'''
	Function obtains answer via wiiMote
	Returns boolean depending on whether subject thinks they could have passed
	obstacle or not
'''
def inputRequest(key):
	messageWindow = vizinfo.add('')
	#yield viztask.waitTime(1.2) # wait for 1.2 seconds
	messageWindow.message("Do you think you could pass? \nPress \"a\" if you think you could, \"b\" if not.")
	messageWindow.translate(0.9, 0.95)   # can vary depending on desired position of box
	messageWindow.visible(viz.ON)
	
	if key == wii.BUTTON_A:
		participant_answer = True
		messageWindow.remove()
	if key == wii.BUTTON_B:
		participant_answer = False
		messageWindow.remove()

#
# Listener for wiimote
vizact.onsensordown(wiimote,wii.BUTTON_B,inputRequest,wii.BUTTON_B)
vizact.onsensordown(wiimote,wii.BUTTON_A,inputRequest,wii.BUTTON_A)

