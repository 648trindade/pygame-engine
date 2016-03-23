'''
==============================================================================
	Primary application class

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
import pygame, os
from TextureBank import TextureBank
from Log import Log

os.environ['SDL_VIDEO_CENTERED'] = '1'

class App:
	Running = True
	WindowWidth = 1024
	WindowHeight = 768;
	
	def OnEvent(self, Event):
		'''Capture Pygame Events
		App.onEvent(event) -> None'''
		pass
	
	def Init(self):
		'''Initialize our Pygame game / app
		App.Init() -> bool'''
		try:
			pygame.init()
		except Exception as e:
			Log("Unable to Init Pygame:",e)
			return False
		
		try:
			self.Window = pygame.display.set_mode((self.WindowWidth, self.WindowHeight))
			pygame.display.set_caption("My Pygame game")
		except Exception as e:
			Log("Unable to create Pygame Window:",e)
			return False
		
		# Adaptation for SDL_SetRenderDrawColor
		self.DisplayDrawColor = (255,255,255)
		
		self.textureBank = TextureBank()
		if not self.textureBank.Init():
			Log("Unable to init TextureBank")
			return False
		
		return True
	
	def Loop(self):
		'''Logic Loop
		App.Loop() -> None'''
		pass
	
	def Render(self):
		'''Render loop (draw)
		App.Render() -> None'''
		self.Window.fill(self.DisplayDrawColor)
		
		try:
			# Check if your texture ID exists!
			self.textureBank.Get("Test").Render(0,0)
		except Exception as e:
			Log("Error to render Texture:",e)
		
		pygame.display.flip()
	
	def Cleanup(self):
		'''Free up resources
		App.Cleanup -> None'''
		self.textureBank.Cleanup()
		pygame.quit()
	
	def Execute(self):
		'''Main loop of the game. Call Init, seek events, call for modules to
		threat the events, loop and renderization. Delay the game for relative
		FPS.
		App.Execute() -> bool'''
		if not self.Init():
			return False
		
		while(self.Running):
			for event in pygame.event.get():
				self.OnEvent(event)
				
				if event.type == pygame.QUIT:
					self.Running = False
			
			self.Loop()
			self.Render()
			
			# Breath
			pygame.time.Clock().tick(60)
		
		self.Cleanup()
		return True
	
	def GetInstance(self):
		'''Return Instance of App Object
		App.GetInstance() -> App'''
		return self
	
	def GetWindowsWidth(self):
		'''Return Windows Width
		App.GetWindowsWidth() -> int'''
		return self.GetWindowsWidth
	
	def GetWindowsHeight(self):
		'''Return Windows Height
		App.GetWindowsHeight() -> int'''
		return self.GetWindowsHeight