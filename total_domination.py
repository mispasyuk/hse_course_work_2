import random
import numpy as np
arr = [(10,10),(12,12), (10, 16), (14,14), (15,15), (16,16), (17,17), (15, 20), (18, 18), (19, 19), (20, 20)]
ans = []
def experiment(t_length, t_height):
    #with open("text.txt", "a") as f:
     #   f.write("new exp\n")
    print ("Hey! Let's conduct an experiment on total domination games in graphs!")
    #print("Enter the length: ")
    length = t_length
    #print("Enter the height: ")
    height = t_height
    num_of_vertices = length*height
    #matrix that contanins the information about neighboring vertices
    adjacency_matrix = [[0] * num_of_vertices for i in range(num_of_vertices)] 
    names = [] #numeration of vertices
    count = 1
    dom_set = set() #dominating set

    for i in range (0, num_of_vertices):
        names.append(i)

    #function which crates adjacecncy matrix of graph
    def create_AM(length, height):
        for i in range (length*height):
            if i+1<length*height and (i + 1) % length != 0:
                adjacency_matrix[i][i+1] = 1
            if i+length<length*height:
                adjacency_matrix[i][i+length] = 1
            if i-1>=0 and i % length != 0:
                adjacency_matrix[i][i-1] = 1
            if i-length>=0:
                adjacency_matrix[i][i-length] = 1
        #for i in range (length*height):
         #   print (adjacency_matrix[i])

    create_AM(length, height)

    neighbours = [0 for i in range(num_of_vertices)] 

    #print ("Numeration of vertices: ", names)
    while sum(neighbours) < num_of_vertices:
        vertex = random.choice(names)
        #with open("text.txt", "a") as f:
         #   f.write(str(vertex) + "\n")
        dom_set.add(vertex)
        print(vertex, end = ", ")
        names.remove(vertex)
        for i in range(len(adjacency_matrix[vertex])):
            if adjacency_matrix[vertex][i] == 1:
                neighbours[i] = 1
            
    print("")
    print("The whole number of steps is: ", len(dom_set)) 
    print("")
    print(dom_set, "\n")
    ans.append(len(dom_set))


for j in range(11):
    for i in range(20):
        experiment(arr[j][0],arr[j][1])
    with open("text.txt", "a") as f:
        f.write(f"{round(np.mean(ans))} \n")
    ans.clear()
        
