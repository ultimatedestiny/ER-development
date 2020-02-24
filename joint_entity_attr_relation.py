import random
from graphviz import Graph
import tempfile
global dot
dot = Graph(comment='sentence structure')
global collect
global call
global para_length
global m
global n
global dict
global matrix

call = 0
para_length = 0
collect = []
m = []
n = []
dict = {}
matrix = [[]]
def append(e1,e2,r,set,sentence_no,para):
    global para_length
    para_length = para
    global collect
    list = []
    list.append(e1)
    list.append(e2)
    list.append(r)
    list.append(set)
    print(list)
    collect.append(list)
    print(" ")
    print("FINAL LIST collect TO BE USED IN DIAGRAM :")
    print(collect)
    print(" ")
    final(sentence_no,para_length)

def final(sentence_no,para):
    global para_length
    global call
    global collect
    global count
    global m
    global n
    global dict
    global matrix
    global dot
    para_length = para
    call = call + 1
    print(collect)
    count = 0
    dict = {}
    for x in collect:        #for the elemets with index 0 and 1 i.e. entities, if they are not in dictionaries they are assigned a key in ditionary
        if(x[0] not in dict):
            dict[x[0]] = count   #checking 1st entity in dict
            count = count + 1
        if(x[1] not in dict):
            dict[x[1]] = count  #checking 2nd entity in dict
            count = count + 1
    print(dict)

    m = len(collect)*2     #list of entities
    n = len(collect)*2      #list of relationships between entities
    matrix = [ [ 0 for i in range(n) ] for j in range(m) ]    #constructing matrices
    for i in range(len(collect)):
        index1 = dict[collect[i][0]]      
        index2 = dict[collect[i][1]]
        matrix[index1][index2] = 1         #assigning 1 in the matrices if there exists a relation between 2 entities
    print(matrix)
    
    m = []                                  #entity matrix
    for x in range(len(collect)):
        for j in range(2):
            if(collect[x][j] not in m):     #adding entities in the entity list m if not present in m
                m.append(collect[x][j])       
                if(len(m)>1):
                    if(m[len(m)-1] == m[len(m)-2]):   #if the last and 2nd last elements are same they are removed from the list , m, to remove redundancy.
                        m.pop()
                    if(m[-1].startswith(m[-2])):     #if the last entity name starts with name of 2nd last entity, it is removed because it is an attribute not an entity.
                        m.pop()
    print(m)

    n = []              #relationship matrix
    for x in range(len(collect)):
        n.append(collect[x][2])  #adding relation to relationship matrix
        '''if(n[len(n)-1] == 'has'):  #if has is detected as relation it is removed as we have a TR for detection 'has' relationship.
            n.pop()'''
    print(n)

    k=0
    for i in range(len(m)):
        dot.node(str(i),m[i],shape='rectangle',fontname="sans",fontcolor="red")  #creating node for entities
    count = i + 2
    index = 0
    
    list = collect[sentence_no][3]
    print(collect[sentence_no][3])
    '''for i in range(len(m)):
        if(list[0][0] == m[i]):
            for j in range(1,len(list[0])):
                if list[0][j].endswith('number'):
                    dot.node(str(list[0][j]),str(list[0][j]),fontname="sans",fontcolor="green")
                    dot.edge(str(list[0][j]),str(i),label=" ",dir=None)
                else:
                    dot.node(str(list[0][j]),str(list[0][j]))
                    dot.edge(str(list[0][j]),str(i),label=" ",dir=None)'''
#########################
    for i in range(len(m)):
        if(list[0] == m[i]):
            for j in range(1,len(list)):
                if list[j].endswith('number' or 'Number' or 'NUMBER' or 'no' or 'NO' or 'No'):
                    dot.node(str(list[j]),str(list[j]),fontname="sans",fontcolor="green")
                    dot.edge(str(list[j]),str(i),label=" ",dir=None)
                else:
                    dot.node(str(list[j]),str(list[j]))
                    dot.edge(str(list[j]),str(i),label=" ",dir=None)

    if(call == para_length):
        for i in range(len(m)):
            for k in range(len(m)):
                if(matrix[i][k] == 1):
                    dot.node(str(count+k),n[index],shape ='diamond')
                    index = index + 1
                    dot.edge(str(i), str(count+k), label=" ",dir=None)
                    dot.edge(str(count+k), str(k), label=" ",dir=None)
                    #dot.edge(str(i), str(j), label=l[i][j][2])
                    #dot.edge(str(i), str(k+2), label=str(n[k]))
                    #dot.edge(str(k+2), str(k+1))
                    #dot.edge(str(count+j), str(i+1))
            count = count + k 
        dot.view(tempfile.mktemp('.gv')) 
        return

def append_only_entity_relation(e1,e2,r,sentence_no,para):
    global para_length
    para_length = para
    global collect
    list = []
    list.append(e1)
    list.append(e2)
    list.append(r)
    print("printing list",list)
    collect.append(list)
    print(" ")
    print("FINAL LIST l2 TO BE USED IN DIAGRAM :")
    print(collect)
    print(" ")
    final_2(sentence_no,para_length)
def final_2(sentence_no,para):
    global call
    global para_length
    global collect
    global count
    global m
    global n
    global dict
    global matrix
    global dot
    para_length = para
    call = call + 1
    print(collect)
    count = 0
    dict = {}
    for x in collect:
        if(x[0] not in dict):
            dict[x[0]] = count
            count = count + 1
        if(x[1] not in dict):
            dict[x[1]] = count
            count = count + 1
    print(dict)

    m = len(collect)*2
    n = len(collect)*2
    matrix = [ [ 0 for i in range(n) ] for j in range(m) ] 
    for i in range(len(collect)):
        for j in range(len(collect)):
            index1 = dict[collect[i][0]]
            index2 = dict[collect[i][1]]
            matrix[index1][index2] = 1
    print(matrix)
    m = []
    for x in range(len(collect)):
        for j in range(2):
            if(collect[x][j] not in m):
                m.append(collect[x][j])
                '''if(len(m)>1):
                    if(m[len(m)-1] == m[len(m)-2]):
                        m.pop()'''
    print(m)
    n = []
    for x in range(len(collect)):
        n.append(collect[x][2])
    print(n)

    k=0
    for i in range(len(m)):
        dot.node(str(i),m[i],shape='rectangle',fontname="sans",fontcolor="red")
    count = i + 2
    index = 0
    if(call == para_length):
        for i in range(len(m)):
            for k in range(len(m)):
                if(matrix[i][k] == 1):
                    dot.node(str(count+k),n[index],shape ='diamond')
                    index = index + 1
                    dot.edge(str(i), str(count+k), label=" ",dir="None")
                    dot.edge(str(count+k), str(k), label=" ",dir="None")
                    #dot.edge(str(i), str(j), label=l[i][j][2])
                    #dot.edge(str(i), str(k+2), label=str(n[k]))
                    #dot.edge(str(k+2), str(k+1))
                    #dot.edge(str(count+j), str(i+1))
            count = count + k 
        dot.view(tempfile.mktemp('.gv')) 
        return

#ONLY ATTRIBUTES
def append_only_attribute(set,sentence_no,para):
    global para_length
    para_length = para
    global collect
    list = []
    #list.append(e1)
    #list.append(e2)
    #list.append(r)
    list.append(set)
    print(list)
    collect.append(list)
    print(" ")
    print("FINAL LIST collect TO BE USED IN DIAGRAM :")
    print(collect)
    print(" ")
    final_only_attribute(sentence_no,para_length)

def final_only_attribute(sentence_no,para):
    global para_length
    global call
    global collect
    global count
    global m
    global n
    global dict
    global matrix
    global dot
    para_length = para
    call = call + 1
    print(collect)
    count = 0
    '''dict = {}
    for x in collect:        #for the elemets with index 0 and 1 i.e. entities, if they are not in dictionaries they are assigned a key in ditionary
        if(x[0] not in dict):
            dict[x[0]] = count   #checking 1st entity in dict
            count = count + 1
        if(x[1] not in dict):
            dict[x[1]] = count  #checking 2nd entity in dict
            count = count + 1
    print(dict)'''

    m = len(collect)*2     #list of entities
    #n = len(collect)*2      #list of relationships between entities
    #matrix = [ [ 0 for i in range(n) ] for j in range(m) ]    #constructing matrices
    #for i in range(len(collect)):
    #    index1 = dict[collect[i][0]]      
    #    index2 = dict[collect[i][1]]
    #    matrix[index1][index2] = 1         #assigning 1 in the matrices if there exists a relation between 2 entities
    #print(matrix)
    
    m = []                                  #entity matrix
    for x in range(len(collect)):
        for j in range(1):
            if(collect[x][j][0] not in m):     #adding entities in the entity list m if not present in m
                m.append(collect[x][j][0])      
                print(m) 
                if(len(m)>1):
                    if(m[len(m)-1] == m[len(m)-2]):   #if the last and 2nd last elements are same they are removed from the list , m, to remove redundancy.
                        m.pop()
                    if(m[-1].startswith(m[-2])):     #if the last entity name starts with name of 2nd last entity, it is removed because it is an attribute not an entity.
                        m.pop()
    print(m)

    #n = []              #relationship matrix
    #for x in range(len(collect)):
    #    n.append(collect[x][2])  #adding relation to relationship matrix
        #if(n[len(n)-1] == 'has'):  #if has is detected as relation it is removed as we have a TR for detection 'has' relationship.
        #    n.pop()'''
    #print(n)

    k=0
    for i in range(len(m)):
        dot.node(str(i),str(m[i]),shape='rectangle',fontname="sans",fontcolor="red")  #creating node for entities
    #count = i + 2
    index = 0
    
    list = collect[sentence_no][0]
    print(collect[sentence_no][0])
    '''for i in range(len(m)):
        if(list[0] == m[i]):
            for j in range(1,len(list)):
                if list[j].endswith('number'):
                    dot.node(str(list[j]),str(list[j]),fontname="sans",fontcolor="green")
                    dot.edge(str(list[j]),str(i),label=" ",dir=None)
                else:
                    dot.node(str(list[j]),str(list[j]))
                    dot.edge(str(list[j]),str(i),label=" ",dir=None)'''
#########################
    for i in range(len(m)):
        if(list[0] == m[i]):
            for j in range(1,len(list)):
                if list[j].endswith('number' or 'Number' or 'NUMBER' or 'no' or 'NO' or 'No'):
                    dot.node(str(list[j]),str(list[j]),fontname="sans",fontcolor="green")
                    dot.edge(str(list[j]),str(i),label=" ",dir=None)
                else:
                    dot.node(str(list[j]),str(list[j]))
                    dot.edge(str(list[j]),str(i),label=" ",dir=None)

   # if(call == para_length):
   #     for i in range(len(m)):
   #         for k in range(len(m)):
   #             if(matrix[i][k] == 1):
   #                 dot.node(str(count+k),n[index],shape ='diamond')
   #                 index = index + 1
   #                 dot.edge(str(i), str(count+k), label=" ",dir=None)
   #                 dot.edge(str(count+k), str(k), label=" ",dir=None)
   #                 #dot.edge(str(i), str(j), label=l[i][j][2])
   #                 #dot.edge(str(i), str(k+2), label=str(n[k]))
   #                 #dot.edge(str(k+2), str(k+1))
   #                 #dot.edge(str(count+j), str(i+1))
   #         count = count + k 
    dot.view(tempfile.mktemp('.gv')) 
    return
