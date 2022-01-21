import pygame
import time
import math

blockSize = 20
blocks = 30
tiles = [0]*blocks**2

pygame.init()
screen = pygame.display.set_mode((blockSize * blocks, blockSize * blocks))
pygame.display.set_caption("Number Interpreter")
width, height = pygame.display.get_window_size()


def showTiles(tilesToBeShown):
    for i in range(0, blocks):
        for f in range(0, blocks):
            if tilesToBeShown[i*blocks+f] != 0:
                row = math.floor(((f / blocks) % 1) * blocks)
                collum = math.floor(((i / blocks) % 1) * blocks)
                pygame.draw.rect(screen, (255, 255, 255), (row*blockSize+1, collum*blockSize+1, blockSize-1, blockSize-1))


def showGrindr():
    for i in range(blockSize, blocks * blockSize, blockSize):
        pygame.draw.line(screen, (100, 100, 100), (i, 0), (i, height))
    for i in range(blockSize, blocks * blockSize, blockSize):
        pygame.draw.line(screen, (100, 100, 100), (0, i), (width, i))


def addLine(posi):
    global tiles
    row = math.floor(posi[0]/blockSize)
    collum = math.floor(posi[1]/blockSize)
    print(collum)
    tiles[row + collum * blocks] = 255
    tiles[row + collum * blocks + 1] = 255
    tiles[row + collum * blocks - 1] = 255
    tiles[row + collum * blocks + blocks] = 255
    tiles[row + collum * blocks - blocks] = 255


while 1:
    mousePos = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                exit()
            if event.key == pygame.K_DELETE:
                tiles = [0]*blocks**2

    if pygame.mouse.get_pressed(3)[0]:
        addLine(mousePos)

    showGrindr()
    showTiles(tiles)
    pygame.draw.circle(screen, (255, 255, 255), mousePos, 25)
    pygame.display.flip()
    screen.fill((0, 0, 0))
