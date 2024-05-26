from copy import deepcopy
import pygame

RED = (255, 0, 0)
WHITE = (255, 255, 255)

def minimax(position, depth, max_player, game):
    if depth == 0 or position.winner() != None:
        return position.evaluate(), position
    
    if max_player:
        minEval = float('-inf')#Which one is the best
        best_move = None
        for move in get_all_moves(position, WHITE, game):
            evaluation = minimax(move, depth-1, False, game)[0]
            minEval = max(minEval, evaluation)
            if minEval == evaluation:
                best_move = move
        
        return minEval, best_move
    else:
        minEval = float('inf')#Which one is the worse
        best_move = None
        for move in get_all_moves(position, RED, game):
            evaluation = minimax(move, depth-1, True, game)[0]
            minEval = min(minEval, evaluation)
            if minEval == evaluation:
                best_move = move
        
        return minEval, best_move

def simulate_move(pice, move, board, game, skip):
    board.move(pice, move[0], move[1])
    if skip:
        board.remove(skip)

    return board

def get_all_moves(board, color, game):
    moves = []#[[board,piece]]

    for piece in board.get_all_pieces(color):
        valid_moves = board.get_valid_moves(piece)
        #(row, col): [pieces]
        for move, skip in valid_moves.items():
            draw_move(game, board, piece)
            temp_board = deepcopy(board)
            temp_piece = temp_board.get_piece(piece.row, piece.col)
            new_board = simulate_move(temp_piece, move, temp_board, game, skip)
            moves.append(new_board)

    return moves

def draw_move(game, board, piece):
    valid_moves = board.get_valid_moves(piece)
    board.draw(game.win)
    pygame.draw.circle(game.win, (0, 255, 0), (piece.x, piece.y), 50, 5)
    game.draw_valid_moves(valid_moves.keys()) #{(4, 6): [Piece()]}
    pygame.display.update()
    #pygame.time.delay(100)

# x = []
# y = deepcopy(x)

