'''
Participant class
Creates a participant object to obtain information for experiment
'''

import viz
import viztask
import vizinfo


class Participant:
	def __init__(self, height, shoulder, name):
		self.height = height
		self.s_width = shoulder
		self.name = name
# addSpeed provides information about participants speed - affected by gain presence
	def addSpeed(self,speedIn, gain):
		if (gain):
			self.speed = speedIn*1.5
		else:
			self.speed = speedIn
	def __str__(self):
		return ('Name:\t\t\t\t%s')%(self.name)+('\nHeight:\t\t\t\t%d inches')%(self.height)+('\nShoulder width:\t\t%d inches')%(self.s_width)+('\nSpeed:\t\t\t\t%d m/s')%(self.speed)



#alberto = Participant(68, 52, "Alberto")
#alberto.addSpeed(4,True)
#
#print alberto
