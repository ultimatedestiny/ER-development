import sys
import joint_entity_attr_relation

global l 
global sentence_no
sentence_no = 0
l = []
def goto(lineno):
    frame = sys._getframe().f_back
    called_from = frame

    def hook(frame, event, arg):
        if event == 'line' and frame == called_from:
            try:
                frame.f_lineno = lineno
            except ValueError as e:
                print("jump failed:", e)
            while frame:
                frame.f_trace = None
                frame = frame.f_back
            return None
        return hook

    while frame:
        frame.f_trace = hook
        frame = frame.f_back
    sys.settrace(hook)

#def draw(entity,attr1,attr2,attr3,attr4,attr5,attr8,attr9,para):

def draw(entity,attr1,attr2,attr3,attr4,attr5,attr6,attr7,attr8,attr9,para):
    #cou = count
    global l
    global sentence_no
    sentence_no = sentence_no + 1
    para_length = para
    l1 = attr1
    l2 = attr2
    l3 = attr3
    l4 = attr4
    l5 = attr5
    l6 = attr6
    l7 = attr7
    l8 = attr8
    l9 = attr9
    e = entity
    if not l1:
        del(l1)
    else:
        l.append(l1)
    if not l2:
        del(l2)
    else:
        l.append(l2)
    if not l3:
        del(l3)
    else:
        l.append(l3)
    if not l4:
        del(l4)
    else:
        l.append(l4)
    if not l5:
        del(l5)
    else:
        l.append(l5)
    if not l6:
        del(l6)
    else:
        l.append(l6)
    if not l7:
        del(l7)
    else:
        l.append(l7)
    if not l8:
        del(l8)
    else:
        l.append(l8)
    if not l9:
        del(l9)
    else:
        l.append(l9)
    print(l)
    length = len(l)
    for i in range(length):
        for j in range(i+1,length):
            try :
                if(l[i][0] == l[j][0]):
                    l[j].pop(0)
                    l[i] = l[i] + l[j]
                    del(l[j])
                    length = length - 1
                    print(l)
            except:
                if(l[length-1][0] == l[0][0]):
                    l[length-1].pop(0)
                    l[0] = l[0] + l[length-1]
                    del(l[length-1])
                    print(l)
                elif(l[length-1][0] == l[1][0]):
                    l[length-1].pop(0)
                    l[1] = l[1] + l[length-1]
                    del(l[length-1])
                    print(l)

                
    print(l)
    if(len(l)==sentence_no):
        joint_entity_attr_relation.append(e[0],e[1],e[2],l[sentence_no-1],sentence_no-1,para_length)
        return
        #joint_entity_attr_relation.attribute_graph(l,cou)
        #goto(100)
    else:
        joint_entity_attr_relation.append_only_entity_relation(e[0],e[1],e[2],sentence_no-1,para_length)
        return



#print(l)
#draw(['customer','withdrawal','carries'],['withdrawal','amount'],['withdrawal','date'],['withdrawal','time'],[],[],[],['withdrawal','type'],[],[],2)
#draw(['system','user','warns'],['system','id'],['system','modelname','modelnumber'],['system','make'],[],[],[],[],[],[],2)

#draw(['customer','withdrawal','carries'],[],[],[],[],[],[],[],[],[],2)
#draw(['system','user','warns'],[],[],[],[],[],[],[],[],[],2)
#draw(['Professor','Student','teaches'],[],[],[],[],[],[],[],[],[],5)

#draw(['Student','Courses','studies'],['Courses','Mathematics','TOC','Machine Learning',],[],[],[],[],[],[],[],[],5)
#draw(['Student','Books','reads'],['Books','TOC_hopcroft','OS_Tanenbaum'],[],[],[],[],[],[],[],[],5)
#draw(['Student','Library','reads_in'],[],[],[],[],[],[],[],[],[],5)

#draw(['Institute','Student','admits'],['Student','Name','Address','Roll_no'],[],[],[],[],[],[],[],[],5)
#draw(['Institute','Professor','emplos'],[],[],[],[],[],[],[],[],[],6)


#draw(['Employee','Employee','Supervises'],['Employee','Name','Sex','Address','salary'],[],[],[],[],[],[],[],[],5)
#draw(['Employee','Department','Manages'],[],[],[],[],[],[],[],[],[],5)

#draw(['Employee','Dependent','Dependents_of'],[],[],[],[],[],[],[],[],[],5)

#draw(['Employee','Project','Works_on'],['Project','Name','Number','Location'],[],[],[],[],[],[],[],[],5)

#draw(['Department','Project','Controls'],['Department','Name','Number','Location'],[],[],[],[],[],[],[],[],5)



