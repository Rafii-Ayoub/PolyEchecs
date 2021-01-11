
import chess
import time
from MinMax import MinMax
import chess.svg
from selenium import webdriver
import Evaluation_FEN
from savgame import SaveGame

from IPython.display import SVG, display

class ModeJoueurContreOrdinateur:
    
    def __init__(self):
        self.player = input("Nom du joueur : ")
        self.nameAI = "AI"
        self.turnId = 0
        driver = webdriver.Chrome("C:\Windows\chromedriver.exe")
        self.url="https://lichess.org/editor/"
        driver.get(self.url)
        self.driver=driver
        self.board = chess.Board()
        
        self.gam = SaveGame(self.board)
        self.gam.headers(["test",None,None,None,None,None,None])
        print("Affichage PGN :")
        self.listCoups = [] 
        
    def commencerPartie(self):
        
        lastMove = None
        
        while(self.partieEstFinie()):
            
            self.notificationTourJoueur()
                
            #Si l'action est possible alors on la réalise
            move = self.getAction()
            self.board.push(move)
            fen_url = self.url+self.board.fen()
            
            self.driver.get(fen_url)
            #On print le plateau et c'est au joueur suivant de jouer si il n'est pas en echec et mat
            if(lastMove == None):
                display(SVG(chess.svg.board(board=self.board, lastmove = move)))
            else:
                display(SVG(chess.svg.board(board=self.board, lastmove = lastMove)))
        
            #On incremente l'id
            self.turnId += 1
            
            self.listCoups.append(move)
            
            lastMove = move
            time.sleep(2)
            
        self.finDePartie()
        
    def notificationTourJoueur(self):
        #Un joueur choisi une action (on annonce le tour du joueur, si id%2 == 0 alors blanc donc joueur sinon noir)
        if(self.turnId%2 == 0):
            print("C'est au tour de", self.player)
        else:
            print("C'est au tour de", self.nameAI)
            
        print(Evaluation_FEN.evaluation(self.board.fen()))
        
    def getAction(self):
        bestMove = ""
        with chess.polyglot.open_reader("bookfish.bin") as reader:
            for entry in reader.find_all(self.board):
                bestMove = entry.move.__str__()
                break
        
        #If the try succeed we can use bookfish, else we use min max with aplha beta
        try:
            move = chess.Move.from_uci(bestMove)
            method = "(Move by Bookfish)"
            
        except:   
            move = MinMax.minimaxRoot(3,self.board,True)
            method = "(Move by Min Max and Alpha Beta pruning"
        
        #Player
        if(self.turnId%2 == 0):
            action = input("Donner une action à réaliser (ex:" + str(move)  + ") : ")
            while(self.moveEstLegal(action) == False):
                print("L'action n'est pas autorisée, veuillez recommencer")
                action = input("Donner une action à réaliser (ex:" + str(move)  + ") : ")
            return chess.Move.from_uci(action)
        else:            
            print(self.nameAI + " a joue " + str(move), method)
            return move
    
    def moveEstLegal(self, action):
        try:
            tempMove = chess.Move.from_uci(action)
        except:
            return False
        
        if (tempMove in self.board.legal_moves):
            return True
        else: return False
        
        
    def partieEstFinie(self):
        return not self.board.is_game_over()
    
    def finDePartie(self):
        self.gam.save_game(self.listCoups)
        
        if (self.turnId%2 == 0):
            print(self.player, " a gagné")
        else:
            print(self.nameAI, " a gagné")