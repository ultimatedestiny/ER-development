import random
from graphviz import Graph
import tempfile
dot = Graph(comment='sentence structure')
global l
global call
#global l
global para_length
global m
global n
global dict
global matrix

call = 0
para_length = 0
l = []
l = []
m = []
n = []
dict = {}
matrix = [[]]
def append(e1,e2,r,set,sentence_no,para):
    global para_length
    para_length = para
    global l
    list = []
    list.append(e1)
    list.append(e2)
    list.append(r)
    list.append(set)
    print(list)
    l.append(list)
    print(" ")
    print("FINAL LIST L TO BE USED IN DIAGRAM :")
    print(l)
    print(" ")
    final(sentence_no,para_length)

def final(sentence_no,para):
    global para_length
    global call
    global l
    global count
    global m
    global n
    global dict
    global matrix
    para_length = para
    call = call + 1
    print(l)
    count = 0
    dict = {}
    for x in l:
        if(x[0] not in dict):
            dict[x[0]] = count
            count = count + 1
        if(x[1] not in dict):
            dict[x[1]] = count
            count = count + 1
    print(dict)

    m = len(l)*2
    n = len(l)*2
    matrix = [ [ 0 for i in range(n) ] for j in range(m) ] 
    for i in range(len(l)):
        index1 = dict[l[i][0]]
        index2 = dict[l[i][1]]
        matrix[index1][index2] = 1
    print(matrix)
    m = []
    for x in range(len(l)):
        for j in range(2):
            if(l[x][j] not in m):
                m.append(l[x][j])
                if(len(m)>1):
                    if(m[len(m)-1] == m[len(m)-2]):
                        m.pop()
                    if(m[-1].startswith(m[-2])):
                        m.pop()
    print(m)
    n = []
    for x in range(len(l)):
        n.append(l[x][2])
        if(n[len(n)-1] == 'has'):
            n.pop()
    print(n)

    k=0
    for i in range(len(m)):
        dot.node(str(i),m[i],shape='rectangle',fontname="sans",fontcolor="red")
    count = i + 2
    index = 0
    
    list = l[sentence_no][3]
    print(l[sentence_no][3])
    for i in range(len(m)):
        if(list[0] == m[i]):
            for j in range(1,len(list)):
                    if list[j].find("number")!=-1:
                        dot.node(str(list[j]),str(list[j]),fontname="sans",fontcolor="green")
                        dot.edge(str(list[j]),str(i),label=" ",dir=None)
                    else:
                        dot.node(str(list[j]),str(list[j]))
                        dot.edge(str(list[j]),str(i),label=" ",dir=None)


    #if(cou==1):
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
    #else:
        
        
    #else:
        #print("not done")

def append_only_entity_relation(e1,e2,r,sentence_no,para):
    global para_length
    para_length = para
    global l
    list = []
    list.append(e1)
    list.append(e2)
    list.append(r)
    print(list)
    l.append(list)
    print(" ")
    print("FINAL LIST l2 TO BE USED IN DIAGRAM :")
    print(l)
    print(" ")
    final_2(sentence_no,para_length)
def final_2(sentence_no,para):
    global call
    global para_length
    global l
    global count
    global m
    global n
    global dict
    global matrix
    para_length = para
    call = call + 1
    print(l)
    count = 0
    dict = {}
    for x in l:
        if(x[0] not in dict):
            dict[x[0]] = count
            count = count + 1
        if(x[1] not in dict):
            dict[x[1]] = count
            count = count + 1
    print(dict)

    m = len(l)*2
    n = len(l)*2
    matrix = [ [ 0 for i in range(n) ] for j in range(m) ] 
    for i in range(len(l)):
        for j in range(len(l)):
            index1 = dict[l[i][0]]
            index2 = dict[l[i][1]]
            matrix[index1][index2] = 1
    print(matrix)
    m = []
    for x in range(len(l)):
        for j in range(2):
            if(l[x][j] not in m):
                m.append(l[x][j])
                '''if(len(m)>1):
                    if(m[len(m)-1] == m[len(m)-2]):
                        m.pop()'''
    print(m)
    n = []
    for x in range(len(l)):
        n.append(l[x][2])
    print(n)
    ##dot = Digraph(comment='sentence structure')
    k=0
    for i in range(len(m)):
        dot.node(str(i),m[i],shape='rectangle')
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