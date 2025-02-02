import pygame

class Pawn:
    def __init__(self, column, row, type, boardspots, boardspots2):
        self.type = type
        self.firstrow = True
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
    def movement(self, position, screen, selected):
        #add another condition for if the square is occupied and one more for if we clicked on the square to go to
        if self.select(position, screen, selected):
            self.rect.y = self.boardspots[self.column][self.row - 1][1]

    def select(self, position, screen, selected):
        if position[0] == self.position[0] - 32.5 and position[1] == self.position[1] - 35 and selected:
            surface = pygame.Surface((70, 70))
            surface.fill("yellow")
            screen.blit(surface, position)
        else:
            selected = False
        return selected
        
    def options(self, whitepawnlist, blackpawnlist):
        # the pawn lists have objects stored inside them we can check against to see which spots are occupied

        # either 1 giant class or a bunch of different classes for each piece
