def maze_translator(file):
        file = open(file, 'r')   
        matrix = []  
        for line in file:
            row = []
            for letter in line.strip():
                if letter == 'O':
                    row.append(0)
                elif letter == 'X':
                    row.append(1)
            matrix.append(row)
            print(row)
        return matrix
        
def m_to_g(maze):
    nodes = set()
    edges = []
    u = []
    for i, row in enumerate(maze):
        index = 0
        for j, k in enumerate(row):
            if k is not None:
                print(i,j)
                nodes.add((i,j))
                if k == 0:
                    pass
            
    nodes = list(nodes)
    return nodes
            
matrix = maze_translator('maze.txt')
print(m_to_g(matrix))

