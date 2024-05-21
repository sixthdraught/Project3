def Maze_Solver(file):
        file = open(file, 'r')   
        data = []
        for row in file:
            data.append([x for x in row.split()])
        print(data)
        i = 0
        lst = []
        for i in range((len(data))):
            lst.append('i')
            lst[i] = []
        i = 0   
        for line in data:
            for letter in line:
                lst[i].append(letter)
                lst[i] = lst[i]
            i+=1
        print(lst)
        
        
Maze_Solver('maze.txt')