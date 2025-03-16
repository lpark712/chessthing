import pygame,sys
from pygame import QUIT
from pawn import Pawn
import os
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Chess")

board = pygame.image.load("imgs/board.png")
board = pygame.transform.scale(board, (600, 600))

# saved positions for each square on the chess board for images
boardspots = []

# list for exact centers of the squares
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


# stores all the objects for all white pawns
whitepawnlist = []
# stores all the objects for all black pawns
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

recentposition = (0, 0)
lastrecent = (0, 0)
select1 = 1
selected = True
move = False
count = 0
print(boardspots)
print("\n\n\n\n\n\n\n\n")
print(boardspots2)
while True:
    screen.blit(board, (0, 0))


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


        if event.type == pygame.MOUSEBUTTONDOWN:
            print(pygame.mouse.get_pos())
            lastrecent = recentposition
            recentposition = closest(pygame.mouse.get_pos())
            if lastrecent == recentposition:
                select1 = select1 * -1
            else:
                select1 = 1

            if lastrecent != recentposition and selected == True and count > 0:
                move = True
                select1 = select1 * -1
            else:
                move = False

            count = 1
            print(move)
          
    
    if select1 == 1:
        selected = True
    if select1 == -1:
        selected = False 
        
    for pawn in whitepawnlist:
        pawn.select(recentposition, screen, selected)
        pawn.update(screen)
        pawn.movement(move, recentposition, lastrecent)

    for pawn in blackpawnlist:
        pawn.select(recentposition, screen, selected)
        pawn.update(screen)
        pawn.movement(move, recentposition, lastrecent)

    pygame.display.update()
    pygame.display.flip()