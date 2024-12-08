import pygame

class Pawn:
    def __init__(self, column, row, type, boardspots, boardspots2):
        self.type = type
        self.boardspots = boardspots
        self.boardspots2 = boardspots2
        self.pawn = ""
        if self.type == "white":
            self.pawn = pygame.image.load("imgs/pawnwhite.png")
        elif self.type == "black":
            self.pawn = pygame.image.load("imgs/pawnblack.png")
        self.pawn = pygame.transform.scale(self.pawn, (70, 70))
        self.rect = self.pawn.get_rect()
        self.rect.x = self.boardspots[column][row][0]
        self.rect.y = self.boardspots[column][row][1]
        self.position = (self.boardspots2[column][row][0], self.boardspots2[column][row][1])
        self.column = column
        self.row = row
        
    def update(self, screen):
        screen.blit(self.pawn, self.rect)
    def movement(self):
        press = pygame.key.get_pressed()
    
        if press[pygame.K_w] and self.type == "white" and self.row == 6:
            self.row -= 2
            self.rect.y = self.boardspots[self.column][self.row][1]

        elif press[pygame.K_w] and self.type == "white" and self.row > 0:
            self.row -= 1
            self.rect.y = self.boardspots[self.column][self.row][1]

        if press[pygame.K_s] and self.type == "black" and self.row == 1:
            self.row += 2
            self.rect.y = self.boardspots[self.column][self.row][1]

        elif press[pygame.K_s] and self.type == "black" and self.row < 7:
            self.row += 1
            self.rect.y = self.boardspots[self.column][self.row][1]
    def select(self, position, screen):
        
        #move circle into middle of square next time
        
        if position[0] == self.position[0] and position[1] == self.position[1] and self.type == "white":
            pygame.draw.circle(screen, "gray", (self.rect.x, self.boardspots[self.column][self.row - 1][1]), 10)
        if position[0] == self.position[0] and position[1] == self.position[1] and self.type == "black":
            pygame.draw.circle(screen, "gray", (self.rect.x, self.boardspots[self.column][self.row + 1][1]), 10)