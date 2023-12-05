def newBoard(n):
    '''
    fonction qui creer le plateau de jeu
    enter:
    n : int()
    '''
    board = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        for j in range(n):
            if (i+j)%2==0:
                board[i][j]=2
            else:
                board[i][j]=1
    centre = n // 2
    board[centre][centre]=0          
    return board


def displayBoard(board, n):
    """
    fonction qui fait l'affichage du jeu
    enter:
    board : lst()
    n : int()
    """
    for i in range(n):
        if i+1>=10:
            print(i+1, end=" |")
        else:
            print(i+1, end="  |")
        for j in range(n):
            if board[i][j]==0:
                print("  .", end="")
            if board[i][j]==1:
                print("  x", end="")
            if board[i][j]==2:
                print("  o", end="")
        print("")
    print("   ", end="")
    print(f"{(n*3+2)*'-'}")
    print("     ", end="")
    for p in range(1,n+1):
        if p+1>=10:
            print(f" {p}", end="")
        else:
            print(f" {p} ", end="")
            

def possiblePawn(board, n , player, i, j):
    '''
    fonction qui verifie si player peut bouger le pion de la case i,j
    enter:
    board : lst()
    n : int()
    player : int()
    i : int()
    j :int()
    '''
    return 0<=i-1<n and 0<=j-1<n and board[i-1][j-1]==player

    
def selectPawn(board, n, player):
    '''
    fonction qui demande au joueur de saisir une coordonné d'un pion deplacable si celui ci ne l'est pas le joueur se fera reposer la question tant qu'elle n'est pas correcte
    enter:
    board : lst()
    n : int()
    player : int()
    '''
    while True:
        print("")
        i=int(input("Choississez la coordonnées d'une colonne d'un pion déplacable : "))
        print("")
        j=int(input("Choississez la coordonnées d'une ligne d'un pion déplacable : "))
        if possiblePawn(board,n,player,i,j) and (board[i-1][j-2]==0 or board[i-2][j-1]==0 or board[i-1][j]==0 or board[i][j-1]==0):
            return i,j
        else:
            print("\nCoordonnées invalides. Veuillez réessayer.")
            


def updateBoard(board, player,n, i, j):
    '''
    fonction qui s'occupe de bouger les pions 
    enter:
    board : lst()
    player : int()
    n : int()
    i : int()
    j :int()
    '''
    if board[i-1][j-2]==0:
        if board[i-1][j-1]==player:
            board[i-1][j-2]=player
            board[i-1][j-1]=0
    elif board[i-2][j-1]==0:
        if board[i-1][j-1]==player:
            board[i-2][j-1]=player
            board[i-1][j-1]=0
    elif board[i-1][j]==0:
        if board[i-1][j-1]==player:
            board[i-1][j]=player
            board[i-1][j-1]=0
    elif board[i][j-1]==0:
        if board[i-1][j-1]==player:
            board[i][j-1]=player
            board[i-1][j-1]=0


def again(board, n, player):
    '''
    fonction qui vérifie si la partie est terminé ou non
    enter:
    board : lst()
    n : int()
    player : int()
    '''
    for i in range(n):
        for j in range(n):
            if board[i-1][j-1]==player:
                if board[i-1][j-2]==0 or board[i-2][j-1]==0 or board[i-1][j]==0 or board[i][j-1]==0:
                    return True
    return False

            
def lewthwaite(n):
    '''
    fonction qui simule la partie de jeu
    enter:
    n : int()
    '''
    if n>81:
        return "Le plateau sur lequel vous voulez jouer est beaucoup trop grand."
    for k in range(81):
        if n==4*k+1:
            plateau=newBoard(n)
            displayBoard(plateau,n)
            joueur=1
            print("\n\nLe joueur 1 a les croix et le joueur 2 les ronds.")
            while again(plateau,n,joueur):
                print(f"\n\nC'est au tour du joueur {joueur}")
                coor=selectPawn(plateau,n,joueur)
                updateBoard(plateau,joueur,n,coor[0],coor[1])
                print("")
                displayBoard(plateau,n)
                joueur = 3 - joueur
            return f"\n\nLe joueur {3-joueur} a gagné la partie. "
    return lewthwaite(9)

print(lewthwaite(9))

