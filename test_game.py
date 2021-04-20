from retro2d.game import Game
from retro2d.scene import Scene
from pygame.locals import *

class GameScene(Scene):
    def __init__(self):
        super().__init__() # Inherit Scene class
    
    def ProcessInput(self, events, pressed_keys): # a function for handling inputs
        for event in events:
            if event.type == KEYDOWN and event.key == K_RETURN:
                print("Enter button is pressed")
    
    def Update(self): # a function that updates every frame
        pass
    
    def Render(self, screen): # a function that handle rendering stuff.
        screen.fill((255, 255, 255)) # fill the background to white
    
    
game = Game(
  scene = GameScene(),
  fullscreen = True,
  title = "Retro 2D with pygame"
)