''' 
	Vector class for better coordinate handling
'''


class vector:
	def __init__(self, x, y, z):
		self.x = x
		self.y = y
		self.z = z
		self.magnitude = ((self.x**2)+(self.y**2)+(self.z**2))**0.5
	def normalize(self):
		self.x /= self.magnitude
		self.y /= self.magnitude
		self.z /= self.magnitude
		# Always make sure that the vector class has this line when normalizing
		self.magnitude = ((self.x**2)+(self.y**2)+(self.z**2))**0.5
	# Operator overloading: the order matters - go figure!
	def __sub__(self, other):
		a = self.x - other.x
		b = self.y - other.y 
		c = self.z - other.z
		return(a,b,c)
	def __add__(self,other):
		a = self.x + other.x
		b = self.y + other.y 
		c = self.z + other.z
		return (a,b,c)
#	def __div__(self,other):
#		a = self.x / other.x
#		b = self.y / other.y 
#		c = self.z / other.z
#		return (a,b,c)
	def __div__(self,num):
		a = self.x / num
		b = self.y / num
		c = self.z / num
		return (a,b,c)
	def __mul__(self,num):
		a = self.x * num
		b = self.y * num
		c = self.z * num
		return (a,b,c)

#a = vector(2,2,2)
#print 'Before normalization: x = %d, y = %d, z = %d' %( a.x, a.y, a.z )
#print 'Magnitude: %.2f' %(a.magnitude)
#b = vector (4,4,4)
#print b-a
#print b+a
## print b / a
#print b /2 
#print b * 3
#a.normalize()
#
#
#print 'After normalization: x = %.2f, y = %.2f, z = %.2f' %(a.x, a.y, a.z)
#a.normalize()
#print 'After normalization: x = %.2f, y = %.2f, z = %.2f' %(a.x, a.y, a.z)

#print a.magnitude
