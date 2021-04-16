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

import os
import pygame

class Animation:
  """
  Main class for handling animation.
  
  ATTRIBUTE:
    image_path    path of the image
    duration      duration of animation in frames
  """
  def __init__(self, image_path, duration):
    self.image_path = image_path
    self.duration   = duration
    
