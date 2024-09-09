import pygame as pg

pg.init()
screen = pg.display.set_mode((1000,500))
clock = pg.time.Clock()
running = True

while running:
  for event in pg.event.get():
    if event.type == pg.QUIT:
      running = False
  screen.fill("blue")

  pg.display.flip()
  clock.tick(120)

pg.quit()
