'''
==============================================================================
	Texture Bank class for loading multiple textures

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
from Texture import Texture
from FileManager import FileManager
from pygame import display
from Log import Log

class TextureBank:
	TexList = {}
	
	#=========================================================================
	def Init(self):
		self.Cleanup()
		
		# Relative to CWD
		Files = FileManager().GetFilesInFolder("Textures")
		Display = display.get_surface()
		
		for Filename in Files:
			Ext = FileManager().GetFilenameExt(Filename)
			ID = FileManager().GetFilenameWithoutExt(Filename)
			
			# Skip all non-png files
			if Ext != "png":
				continue
			
			self.AddTexture(Display, ID, Filename)
		
		return True
	
	#-------------------------------------------------------------------------
	def Cleanup(self):
		if len(self.TexList) <= 0:
			return
		self.TexList.clear()
	
	#=========================================================================
	def AddTexture(self, Display, ID, Filename):
		if ID == "":
			return
			
		NewTexture = Texture()
		if not NewTexture.Load(Display, Filename):
			Log("Unable to Load Texture:",ID)
			return
		
		self.TexList[ID] = NewTexture
	
	#-------------------------------------------------------------------------
	def Get(self, ID):
		return self.TexList.get(ID)
		
	#=========================================================================
	def GetInstance(self):
		return self