import pygame
import random

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

CELL_SIZE = 3

ROWS = int(SCREEN_HEIGHT / CELL_SIZE)
COLUMNS = int(SCREEN_WIDTH / CELL_SIZE)

DEAD = 0
ALIVE = 1

ALIVE_COLOR = (255, 255, 255)
DEAD_COLOR = (0, 0, 0)

firstGridArray: list = [[0] * COLUMNS for _ in range(ROWS)]

secondGridArray: list = [[0] * COLUMNS for _ in range(ROWS)]

worklist = [firstGridArray,secondGridArray]

currentList = 0
nextList = 1

hasFinished = 1

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
font = pygame.font.Font(pygame.font.get_default_font(), 24)
running = True

def InitGrid():
    for row in range(0, ROWS):
        for column in range(0, COLUMNS):
            if (random.randrange(0, 20) > 8):
                firstGridArray[row][column] = ALIVE
            else:
                firstGridArray[row][column] = DEAD

def CheckNeighbors(x, y, index):
    count = 0
    if(worklist[index][(x - 1) % ROWS][(y - 1) % COLUMNS] == 1):
        count = count + 1
    if(worklist[index][(x - 1) % ROWS][y] == 1):
        count = count + 1
    if(worklist[index][(x - 1) % ROWS][(y + 1) % COLUMNS] == 1):
        count = count + 1
    if(worklist[index][x][(y - 1) % COLUMNS] == 1):
        count = count + 1
    if(worklist[index][x][(y + 1) % COLUMNS] == 1):
        count = count + 1
    if(worklist[index][(x + 1) % ROWS][(y - 1) % COLUMNS] == 1):
        count = count + 1
    if(worklist[index][(x + 1) % ROWS][y] == 1):
        count = count + 1
    if(worklist[index][(x + 1) % ROWS][(y + 1) % COLUMNS] == 1):
        count = count + 1
    return count

def CreateNewGeneration():
    for row in range(0, ROWS):
        for column in range(0, COLUMNS):
            neighbors = CheckNeighbors(row, column, currentList) 
            worklist[nextList][row][column] = worklist[currentList][row][column]                            
            if(worklist[currentList][row][column] == ALIVE):
                if(neighbors < 2 or neighbors > 3):
                    worklist[nextList][row][column] = DEAD                
            else:
                if(neighbors == 3):
                    worklist[nextList][row][column] = ALIVE
            
def DrawGrid():
    for row in range(0, ROWS):
        for column in range(0, COLUMNS):
            if(worklist[currentList][row][column] == ALIVE):
                color = ALIVE_COLOR
            else:
                color = DEAD_COLOR
            pygame.draw.rect(screen, color, (column * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE))

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if(hasFinished == 1):
        InitGrid()
        hasFinished = 0

    DrawGrid()
    CreateNewGeneration()

    currentList ^= 1
    nextList ^= 1
    pygame.time.delay(50)
    pygame.display.flip()
    clock.tick(60)