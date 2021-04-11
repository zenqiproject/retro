# retro
> under development

a pygame framework to create 2d games easily

## Installation

```bash
$ pip install retrogame
```
(currently unavailable)


## Usage

```python

from retro2d.game import Game
from retro2d.scene import Scene



class GameScene(Scene):
  def __init__(self):
    super().__init__() # Inherit Scene class
    
  def ProcessInput(self, events, pressed_keys):
    for event in events:
      if event.type == KEYDOWN and event.key == K_return:
        print("Enter button is pressed")
    
   def Update(self):
    pass
    
   def Render(self, screen):
    screen.fill((255, 255, 255)) # fill the background to white
    
    
game = Game(
  scene = GameScene(),
  fullscreen = True,
  title = "Retro 2D with pygame"
)
game.run() # clas Game has already runned whenever you call it. But you can use game.run() as well.

```
