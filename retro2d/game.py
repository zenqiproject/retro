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

import pygame
from pygame.locals import *
import argparse
from .scene import Scene
import sys

class Game:
    """
    Main class for handling all events probably the main class for the game

    Eventually, I dont have a handler for resizing event but I'll go with that sooner
    
    ATTRIBUTE:
      width: int          = None, # Width of the game -> integer 
      height: int         = None, # Height of the game -> integer 
      title: str          = None, # Window Title of the game -> string
      icon: str           = None, # Window Icon of the game -> string (path)
      fps: int            = 60, # fps of the game -> integer
      scene: Scene        = None, # Main scene for the game -> SceneBase 
      fullscreen: bool    = True, # Is the game will be full screened or no -> boolean
      splashscreen: bool  = True # Default splash screen of the game -> boolean
    
    """
    screen = None

    def __init__(self, width: int = None, # Width of the game -> integer 
                height: int = None, # Height of the game -> integer 
                title: str = None, # Window Title of the game -> string
                icon: str = None, # Window Icon of the game -> string (path)
                fps: int = 60, # fps of the game -> integer
                scene: Scene = None, # Main scene for the game -> SceneBase 
                fullscreen: bool = True, # Is the game will be full screened or no -> boolean
                splashscreen: bool = True # Default splash screen of the game -> boolean
            ):
        
        pygame.init()
        self.width          = width
        self.height         = height
        self.title          = title
        self.icon           = icon
        self.fps            = fps
        self.scene          = scene
        self.fullscreen     = fullscreen
        self.splashscreen   = splashscreen
        
        
        if fullscreen != False:
            info = pygame.display.Info()
            self.screen = pygame.display.set_mode((info.current_w, info.current_h), pygame.NOFRAME)

        else:
            self.screen = pygame.display.set_mode((self.width, self.height))

        if self.icon != None:
            pygame.display.set_icon(self.icon)
        
        if self.title != None:
            pygame.display.set_caption(self.title)

        self.run()

    def run(self):

        clock = pygame.time.Clock()

        while self.scene != None and self.screen != None:
            pressed_keys = pygame.key.get_pressed()
            
            filtered_events = []

            for event in pygame.event.get():
                quit = False
                if event.type == QUIT:
                    pygame.quit()
            
                elif event.type == KEYDOWN:
                    alt_pressed = pressed_keys[K_LALT] or \
                                pressed_keys[K_RALT]

                    if event.key == K_F4 and alt_pressed:
                        quit = True
                        pygame.quit()
                
                if quit:
                    self.scene.Terminate()
                    
                else:
                    filtered_events.append(event)

            
            self.scene.ProcessInput(filtered_events, pressed_keys)
            self.scene.Update()
            self.scene.Render(self.screen)

            pygame.display.flip()
            clock.tick(self.fps)
