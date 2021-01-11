
import Trees
import math

class Node:    
    def __init__(self,content,children=[]):
        self.content=content
        self.children=children
    
    def get_content(self):
        return self.content
    
    def get_children(self):
        return self.children

 
    def is_leaf(self):
        return len(self.get_children()) == 0

    def minmax(self, maximizingPlayer): 
        if self.is_leaf():
            return self.content
        
        if maximizingPlayer:
            value=-math.inf        
            for n in self.get_children():
                value=max(value,float(n.minmax(False)))
            return value
        
        else:
            value=math.inf
            for n in self.get_children():
                value=min(value,float(n.minmax(True)))
            return value
    
    
    def minmaxAlphaBeta(self, Alpha, Beta, maximizingPlayer):       
        if self.is_leaf():
            return self.content
        
        if maximizingPlayer:
            for n in self.get_children():
                Alpha=max(Alpha,float(n.minmaxAlphaBeta(Alpha, Beta, False)))
                if Alpha>=Beta:
                    return Beta
            return Alpha
        
        else:
            for n in self.get_children():
                Beta=min(Beta,float(n.minmaxAlphaBeta(Alpha, Beta, True)))
                if Alpha>=Beta:
                    return Alpha
            return Beta

def createTreeFromBoard(board, level, tree):
    
    if(board.is_game_over() or level >= 3):
        return []
    
    level = level + 1
    
    #Create a new tree here and add all the moves and then 
    newTree = Trees.Node(level, None)
    
    for move in board.legal_moves:
        #print(move.__str__().rjust(level * 5))
        
        #Le soucis est que on veut avoir seulement les coups des blancs alors que c'est alterné avec les blancs et les noirs, donc on fait un coups dans le vide pour faire genre que les noirs ont joué
        
        
        #If this is the last level we put a number
        if(level == 2):
            newTree.childrens.append(Trees.Node(level, move, '1'))
        else:
            newTree.childrens.append(Trees.Node(level, move, ''))
            
        board.push(move)
        board.push(move)
        
        
            
        
        createTreeFromBoard(board, level, tree)
        board.pop()
        board.pop()
    
    tree.childrens.append(newTree)
    
def evaluateBoard(board, whiteTurn):
        sumNoir=0
        sumBlanc=0
        i=0
        while liste[i]!=' ':
            if liste [i]=='p':
                sumNoir+=1
                i+=1
            elif liste[i]=='n' or liste[i]=='b' or liste[i]=='r' :
                sumNoir+=3
                i+=1
            elif liste [i]=='q':
                sumNoir+=9
                i+=1
            elif liste [i]=='P':
                sumBlanc+=1
                i+=1
            elif liste[i]=='N' or liste[i]=='B' or liste[i]=='R' :
                sumBlanc+=3
                i+=1
            elif liste [i]=='Q':
                sumBlanc+=9
                i+=1
            else:
                i+=1
        if boolean == True :
            return sumBlanc-sumNoir
        return sumNoir-sumBlanc



n12=Node('45')
n11=Node('-2')
n10=Node('6')
n9=Node('23')
n8=Node('-8')
n7=Node('22')
n6=Node('9')
n5=Node('3')
n4=Node('3')
n3=Node('',[n10,n11,n12])
n2=Node('',[n7,n8,n9])
n1=Node('',[n4,n5,n6])
n0=Node('',[n1,n2,n3])
    
print("minmax", n0.minmax(False))
print("minmaxAB", n0.minmaxAlphaBeta(-math.inf, math.inf, False))
        
        
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    