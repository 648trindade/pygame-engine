'''
==============================================================================
	Texture class for wrapping Pygame Surfaces

	(C++ version)
	3/11/2014
    SDLTutorials.com
    Tim Jones
	
	(Python3 version)
	22/03/2016
	www.inf.ufsm.br/~rtrindade
	Rafael Gauna Trindade
	
==============================================================================
'''
from pygame import image
from Log import Log

class Texture:
	Filename = None
	Width = 0
	Height = 0
	PygameSurface = None
	Display = None
	
	def Load(self, Display, Filename):
		self.Display = Display
		self.Filename = Filename
		
		# Load Pygame Surface
		try:
			self.PygameSurface = image.load(Filename)
		except Exception as e:
			Log("Unable to load image:",Filename,":",e)
			return False
		
		# Grab dimensions
		self.Width  = self.PygameSurface.get_width()
		self.Height = self.PygameSurface.get_height()
		
		return True
	
	def Render(self, X, Y, Width=None, Height=None, SX=None, SY=None, SWidth=None, SHeight=None):
		if Width is None:
			Width = self.Width
		if Height is None:
			Height = self.Height
		if None in (SX, SY, SWidth, SHeight):
			area = None
		else:
			area = (SX, SY, SWidth, SHeight)
		
		dest = (X, Y, Width, Height)
		self.Display.blit(self.PygameSurface, dest, area=area)
	
	def GetWidth(self):
		return self.Width
	
	def GetHeight(self):
		return self.Height