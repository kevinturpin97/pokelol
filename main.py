import pygame
import league_of_pokemon

pygame.init()

game = league_of_pokemon.PokeLol()
alive = True
start = False

while alive:
    pygame.display.update()

    if start:
        alive = game.play()
    else:
        start = game.homepage()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            alive = False

pygame.quit()
