'''
============================================================================
	Class for loading files and reading directories

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
from os import listdir, getcwd
from Log import Log

DIR_SEPARATOR = "/"

class FileManager:
	def SetContents(self, Filename, Content, Relative=True):
		if Filename == "":
			return False
		
		if Relative:
			Filename = getcwd() + DIR_SEPARATOR + Filename
		
		with open(Filename, 'w') as FileHandle:
			FileHandle.write(Content)
		
		return True
	
	def GetContents(self, Filename, Relative=True):
		if Filename == "":
			return False
		
		if Relative:
			Filename = getcwd() + DIR_SEPARATOR + Filename
		
		Content = None
		with open(Filename) as FileHandle:
			Content = FileHandle.read()
		
		return Content
	
	def GetFilesInFolder(self, Folder):
		List = []
		Path = getcwd()
		
		if Folder != "":
			Path += DIR_SEPARATOR + Folder
		
		try:
			for Filename in listdir(Path):
				List.append(Path + DIR_SEPARATOR + Filename)
		except:
			Log("Unable to open directory :",Path)
		
		return List
	
	def GetFilenameWithoutExt(self, Filename):
		return Filename[Filename.rfind(DIR_SEPARATOR)+1:Filename.rfind('.')]
	
	def GetFilenameExt(self, Filename):
		return Filename[Filename.rfind('.')+1:]