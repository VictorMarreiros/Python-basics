N = 4


def mostrar_solucao(sol):
    for i in sol: 
        for j in i: 
            print(str(j) + " ", end="")
        print("") 


def e_seguro(maze, x, y):
    if (x >= 0) and (x < N) and (y >= 0) and (y < N) and (maze[x][y] == 1):
        return True
      
    return False


def solucao_labirinto(maze):
    sol = [ [ 0 for j in range(4) ] for i in range(4) ]

    if solucao_util_do_labirinto(maze, 0, 0, sol) == False:
        print("Não existe solução"); 
        return False
    mostrar_solucao(sol)
    return True


def solucao_util_do_labirinto(maze, x, y, sol):
      
    if x == N - 1 and y == N - 1: 
        sol[x][y] = 1
        return True
           
    if e_seguro(maze, x, y) == True:
        sol[x][y] = 1
        if solucao_util_do_labirinto(maze, x + 1, y, sol) == True:
            return True
        elif solucao_util_do_labirinto(maze, x, y + 1, sol) == True:
            return True

        sol[x][y] = 0
        return False


if __name__ == "__main__": 
    maze = [ [1, 0, 0, 0], 
             [1, 1, 0, 1], 
             [0, 1, 0, 0], 
             [1, 1, 1, 1] ] 
               
    solucao_labirinto(maze)
