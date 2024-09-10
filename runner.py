import pygame as pg
import tictactoe as ttt

pg.init()
screen = pg.display.set_mode((1280,780))
clock = pg.time.Clock()
running = True

# def drawing_move(move){
#   if move ==1:
#     pg.draw.line(screen,(0,0,0),())

# }

while running:
  for event in pg.event.get():
    if event.type == pg.QUIT:
      running = False


  screen.fill(pg.Color("#EEE3CB"))
  pg.draw.line(screen,(0,0,0),(450,100),(450,700),12)
  pg.draw.line(screen,(0,0,0),(800,100),(800,700),12)
  pg.draw.line(screen,(0,0,0),(100,250),(1200,250),12)
  pg.draw.line(screen,(0,0,0),(100,500),(1200,500),12)
  # pg.draw.line(screen,(0,0,0),())

  pg.display.flip()

  clock.tick(120)

pg.quit()
