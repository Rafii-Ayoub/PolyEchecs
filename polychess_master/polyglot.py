
import chess
#used to access Polyglot book
import chess.polyglot
#set the initial position
board = chess.Board()
moves = board.legal_moves
print(moves)
#access the Polyglot book
with chess.polyglot.open_reader("bookfish.bin") as reader:
    for entry in reader.find_all(board):
        print(entry.move, entry.weight, entry.learn)