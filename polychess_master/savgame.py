import chess
import chess.pgn


class SaveGame:
    """
    this class is used to save a party in PGN format
    
    """
    def __init__(self,board):
         """
         constructor 
         """
         self.game=chess.pgn.Game() #PGN format
         self.board=board
         
    def save_game(self,listCoup=[]):
        """
        register a game with pgn format in txt fill
        """
        
        
        self.game.add_line(listCoup)            
        game_pgn = open("gamesave.pgn","w",encoding="utf-8")
        register = chess.pgn.FileExporter(game_pgn)
        self.game.accept(register)
        print(self.game)
        game_pgn.close()
        
    def headers(self,values=[None,None,None,None,None,None,None]):
        """
        allow to change head
        """
        labels = ["Event", "Site", "Date", "Round", "White", "Black", "Result"]
        
        for i in range(len(labels)):
            
            if values[i] !=  None :
                #print(self.game.headers[labels[i]])
                self.game.headers[labels[i]]=values[i]
    
    def readfillPGN(self):
        """
        open game who have been save
        """
        pgn = open("gamesave.pgn",encoding="utf-8-sig")
        go_game=chess.pgn.read_game(pgn)
        print("Event is : ",go_game.headers["Event"])
        Board=go_game.board()
        # Iterate through all moves and play them on a board.
        print("line", go_game.mainline())
        for move in go_game.mainline_moves():
            print(move)
            Board.push(move)
        

        
        
                
        
# ===================
# Tests
# ===================
        
if __name__ == "__main__":
    
    board = chess.Board()
    a="a2a4"
    b=chess.Move.from_uci(a)
    board.push(b)
    
    gam = SaveGame(board)
    gam.headers(["test",None,None,None,None,None,None])
    print("Affichage PGN :")
    listCoup=[chess.Move.from_uci("e2e4"),chess.Move.from_uci("b2b3"),chess.Move.from_uci("b3b4")]
    gam.save_game(listCoup)
    gam.readfillPGN()

        