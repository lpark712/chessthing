import pygame,sys
from pygame import QUIT
from pawn import Pawn
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Chess")

board = pygame.image.load("imgs/board.png")
board = pygame.transform.scale(board, (600, 600))

boardspots = []

boardspots2 = []

x = -60
y = -62.5




def closest(mouse_pos):
    mouse_x = mouse_pos[0]
    mouse_y = mouse_pos[1]
    num = 0
    closest_x = 0
    closest_y = 0
    for _ in range(8):
        if abs(boardspots2[num][0][0] - mouse_x) < 36.25:
            closest_x = boardspots[num][0][0]
            
        num += 1
    num = 0
    for _ in range(8):
        if abs(boardspots2[0][num][1]- mouse_y) < 36.25:
            closest_y = boardspots[0][num][1]
            
        num += 1
    print(closest_x, closest_y)
    return (closest_x, closest_y)

        
x2 = 45 - 72.5
for _ in range(8):
    board_column2 = []
    y2 = 45 - 72.5
    x2 += 72.5
    for _ in range(8):
        y2 += 72.5
        board_column2.append((x2, y2))
    boardspots2.append(board_column2) 







for _ in range(8):
    board_column = []
    y = -62.5
    x += 72.5
    for _ in range(8):
        y += 72.5
        board_column.append((x, y))
    boardspots.append(board_column)


print (boardspots)
whitepawnlist = []
blackpawnlist = []

x = 0
y = 6
for _ in range(8):
    whitepawnlist.append(Pawn(x, y, "white", boardspots, boardspots2))
    x += 1
x = 0
y = 1
for _ in range(8):
    blackpawnlist.append(Pawn(x, y, "black", boardspots, boardspots2))
    x += 1
        
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            print(pygame.mouse.get_pos())
            closest(pygame.mouse.get_pos())
    


    
    screen.blit(board, (0, 0))
    for pawn in whitepawnlist:
        pawn.update(screen)
        pawn.movement()
    for pawn in blackpawnlist:
        pawn.update(screen)
        pawn.movement()
        
    pygame.display.update()
    pygame.display.flip()
    