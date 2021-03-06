#
#           Copyright (c) 2021, Zenqi. All rights reserved.
#
#   This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.


class Scene:
	"""
	Main class for handling scenes.
	"""
  
	def __init__(self):
		pass
  	
	def ProcessInput(self, events, pressed_keys):
		pass
  
	def Update(self):
		pass
  
	def Render(self, screen):
		pass

	def ChangeScene(self, next_scene):
		self.next = next_scene
	
	def Terminate(self):
		self.ChangeScene(None)
