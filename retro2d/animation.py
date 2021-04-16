
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
    
