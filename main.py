import pygame
from checkers.constants import WIDTH, HEIGHT, SQUARE_SIZE, ROWS, RED, WHITE
from minimax.algorithm import minimax
from checkers.game import Game

FPS = 60

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Checkers')

def get_row_col_from_mouse(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col

def main():
    run = True
    clock = pygame.time.Clock()
    game = Game(WIN)

    while run:
        clock.tick(FPS)

        if game.turn == WHITE:
            value, new_board = minimax(game.get_board(), 3, WHITE, game)
            game.ai_move(new_board)


        if game.winner() != None:
            print(game.winner())
        
        for event in pygame.event.get(): #check to see if any events have happened the current time
            if event.type == pygame.QUIT: #Can look at the event and see if it is this specific type
                run = False #that will end this loop rigth here
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_row_col_from_mouse(pos)
                
                game.select(row, col)
                    
                    

        game.update()

    pygame.quit()

main()
