import random
import copy
import numpy as np
import time
print ("Hey! Let's conduct an experiment on domination games in graphs!")
print("Enter the length: ")
length = int(input()) 
print("Enter the height: ")
height = int(input())
num_of_vertices = length*height
#matrix that contanins the information about neighboring vertices
adjacency_matrix = [[0] * num_of_vertices for i in range(num_of_vertices)] 
names = [] #numeration of vertices
count = 1
dominated_vertices = set () #set of dominated vertices
dom_set = set() #dominating set

for i in range (0, num_of_vertices):
    names.append(i)

#function which crates adjacecncy matrix of graph
def create_AM(length, height):
    #for i in range (1, height+1):
        #print(names[i - 1])
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
        #print (adjacency_matrix[i])

create_AM(length, height)
#print(adjacency_matrix)
def calculate (length, height):
    neighbours = []
    for i in adjacency_matrix:
        count_neighbour = 0
        for j in range (length*height):
            if i[j] == 1:
                count_neighbour += 1
        neighbours.append(count_neighbour)
    #print("The number of neighbours of each vertex: ", neighbours)
    print()
    #print ("Numeration of vertices: ", names)
    flag = 1
    while len(dominated_vertices) < num_of_vertices:
        if flag == 1:                              #Dominator's step
            supposed_indexes = []
            supposed_indexes_not_in_dom = []
            max_neighbours = max(neighbours)
            for i in range (len(neighbours)):
                if neighbours[i] == max_neighbours:
                    supposed_indexes.append(i)
            indicator = 0
            for j in supposed_indexes:
                if j not in dominated_vertices:
                    supposed_indexes_not_in_dom.append(j)
                    indicator = 1
            if indicator == 0:
                chosen_element = random.choice(supposed_indexes)
            elif indicator == 1:
                chosen_element = random.choice(supposed_indexes_not_in_dom)  
                dominated_vertices.add(chosen_element)              
            dom_set.add(chosen_element)
            #print (chosen_element)
            neighbours[chosen_element] = -1
            names.remove(chosen_element)
            for i in range(len(adjacency_matrix[chosen_element])):
                if adjacency_matrix[chosen_element][i] == 1 and neighbours[i] != -1:
                    adjacency_matrix[chosen_element][i] = -1
                    neighbours[i] -= 1
                    for l in range(len(adjacency_matrix[i])):
                        if adjacency_matrix[i][l] == 1 and neighbours[l] != -1 :
                            adjacency_matrix[i][l] = -1
                            neighbours[l] -= 1

                if adjacency_matrix[chosen_element][i] == -1 and neighbours[i] != -1:
                    for l in range(len(adjacency_matrix[i])):
                        if adjacency_matrix[i][l] == 1 and neighbours[l] != -1:
                            adjacency_matrix[i][l] = -1
                            neighbours[l] -= 1
            for i in range(len(adjacency_matrix[chosen_element])):
                if abs(adjacency_matrix[chosen_element][i]) == 1:
                    dominated_vertices.add(i)
            flag = 0
        if flag == 0:                                           #Staller's step
            if (len(dominated_vertices) == num_of_vertices):
                break
            supposed_indexes = []
            supposed_indexes_in_dom = []
            min_neighbours = sorted(set(neighbours))[1]
            for i in range (len(neighbours)):
                if neighbours[i] == min_neighbours:
                    supposed_indexes.append(i)
            temp_index = copy.copy(supposed_indexes)

            for j in temp_index:
                if j in dominated_vertices and neighbours[j] == 0:
                    supposed_indexes.remove(j)
            if(len(supposed_indexes) != 0):
                for j in supposed_indexes:
                    indicator = 0
                    if j in dominated_vertices:
                        supposed_indexes_in_dom.append(j)
                        indicator = 1
                if indicator == 0:
                    chosen_element = random.choice(supposed_indexes)
                elif indicator == 1:
                    chosen_element = random.choice(supposed_indexes_in_dom)

                dom_set.add(chosen_element)
                #print(chosen_element)
                dominated_vertices.add(chosen_element)
                neighbours[chosen_element] = -1
                names.remove(chosen_element)
                for i in range(len(adjacency_matrix[chosen_element])):
                    if adjacency_matrix[chosen_element][i] == 1 and neighbours[i] != -1:
                        adjacency_matrix[chosen_element][i] = -1
                        neighbours[i] -= 1
                        for l in range(len(adjacency_matrix[i])):
                            if adjacency_matrix[i][l] == 1 and neighbours[l] != -1:
                                adjacency_matrix[i][l] = -1
                                neighbours[l] -= 1
                    if adjacency_matrix[chosen_element][i] == -1 and neighbours[i] != -1:
                        for l in range(len(adjacency_matrix[i])):
                            if adjacency_matrix[i][l] == 1 and neighbours[l] != -1:
                                adjacency_matrix[i][l] = -1
                                neighbours[l] -= 1
                for i in range(len(adjacency_matrix[chosen_element])):
                    if abs(adjacency_matrix[chosen_element][i]) == 1:
                        dominated_vertices.add(i)
                flag = 1
            else:
                min_neighbours = sorted(set(neighbours))[2]
                for i in range (len(neighbours)):
                    if neighbours[i] == min_neighbours:
                        supposed_indexes.append(i)
                for j in supposed_indexes:
                    indicator = 0
                    if j in dominated_vertices:
                        supposed_indexes_in_dom.append(j)
                        indicator = 1
                if indicator == 0:
                    chosen_element = random.choice(supposed_indexes)
                elif indicator == 1:
                    chosen_element = random.choice(supposed_indexes_in_dom)
                dom_set.add(chosen_element)
                #print(chosen_element)
                dominated_vertices.add(chosen_element)
                neighbours[chosen_element] = -1
                names.remove(chosen_element)
                for i in range(len(adjacency_matrix[chosen_element])):
                    if adjacency_matrix[chosen_element][i] == 1 and neighbours[i] != -1:
                        adjacency_matrix[chosen_element][i] = -1
                        neighbours[i] -= 1
                        for l in range(len(adjacency_matrix[i])):
                            if adjacency_matrix[i][l] == 1 and neighbours[l] != -1:
                                adjacency_matrix[i][l] = -1
                                neighbours[l] -= 1
                    if adjacency_matrix[chosen_element][i] == -1 and neighbours[i] != -1:
                        for l in range(len(adjacency_matrix[i])):
                            if adjacency_matrix[i][l] == 1 and neighbours[l] != -1:
                                adjacency_matrix[i][l] = -1
                                neighbours[l] -= 1
                for i in range(len(adjacency_matrix[chosen_element])):
                    if abs(adjacency_matrix[chosen_element][i]) == 1:
                        dominated_vertices.add(i)
                flag = 1

    print()
    #print (dom_set)
    print("The whole number of steps is: ", len(dom_set))       
    print("expected upper bound: ", length*height*3/5) 

for i in range (1):
    calculate(length, height)


    