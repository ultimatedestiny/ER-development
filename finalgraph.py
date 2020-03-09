#import sys
import joint_entity_attr_relation
global final_list
global l 
global sentence_no
sentence_no = 0
l = []
final_list = []
def draw(entity,New_attr,attr1,attr2,attr3,attr4,attr5,attr6,attr7,attr8,attr9,para):
    global l
    global sentence_no
    sentence_no = sentence_no + 1
    no_of_sentences = para
    l1 = attr1
    l2 = attr2
    l3 = attr3
    l4 = attr4
    l5 = attr5
    l6 = attr6
    l7 = attr7
    l8 = attr8
    l9 = attr9
    l10 = New_attr
    e = entity
    if not l10:
        del(l10)
    else:
        l.append(l10)
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
    print("")
    print("")
    print(entity,attr1,attr2,attr3,attr4,attr5,attr6,attr7,attr8,attr9,para)
    print("")
    print("")
    print("PRINTING l:",end="")
    print(l)
    length_l = len(l)
    for i in range(length_l):
        for j in range(i+1,length_l):
            try :
                if(l[i][0] == l[j][0]):
                    l[j].pop(0)
                    l[i] = l[i] + l[j]
                    del(l[j])
                    length_l = length_l - 1
                    print(l)
            except:
                if(l[length_l-1][0] == l[0][0]):
                    l[length_l-1].pop(0)
                    l[0] = l[0] + l[length_l-1]
                    del(l[length_l-1])
                    print(l)
                elif(l[length_l-1][0] == l[1][0]):
                    l[length_l-1].pop(0)
                    l[1] = l[1] + l[length_l-1]
                    del(l[length_l-1])
                    print(l)

                
    print("printing l :",l)
    print(length_l)
    print("sentence no. ",sentence_no)
    print("E is : ",e)
    print(len(e))
    
    '''if ((length_l > 0) and (len(e)==0) and sentence_no == no_of_sentences):
        #joint_entity_attr_relation.append_only_attribute(l[sentence_no-1],sentence_no-1,no_of_sentences)
        joint_entity_attr_relation.append_only_attribute(l[0],sentence_no-1,no_of_sentences)
        return
        #joint_entity_attr_relation.attribute_graph(l,cou)
        #goto(100)
    elif(len(e)>0 and (length_l == 0) and sentence_no == no_of_sentences):
        joint_entity_attr_relation.append_only_entity_relation(e[0],e[1],e[2],sentence_no-1,no_of_sentences)
        return
    else:
        if sentence_no < no_of_sentences:
            if len(e)>0:
                final_list.append(e)
            elif(len(l)>0):
                final_list.append(l)
        elif sentence_no == no_of_sentences:
            #for i in range(len(final_list)):
            joint_entity_attr_relation.append(final_list[0][0],final_list[0][2],final_list[0][2],final_list[1],sentence_no,no_of_sentences)'''
    if ((sentence_no == no_of_sentences) and len(final_list)==0):
        if ((length_l > 0) and (len(e)==0)):
            joint_entity_attr_relation.append_only_attribute(l[0],sentence_no-1,no_of_sentences)
        if (len(e)>0 and (length_l == 0)):
            joint_entity_attr_relation.append_only_entity_relation(e[0],e[1],e[2],sentence_no-1,no_of_sentences)
    else:
        if(len(e) > 0):
            final_list.append(e)
            print("final_list is :", final_list)
        elif(len(l)>0):
            final_list.append(l)
            print("final_list is :", final_list)
            if(len(final_list)==no_of_sentences):
                print("final_list is :", final_list)
                joint_entity_attr_relation.append(final_list[0][0],final_list[0][1],final_list[0][2],final_list[1][0],sentence_no,no_of_sentences)

        elif(len(final_list)==no_of_sentences):
            print("final_list is :", final_list)
            joint_entity_attr_relation.append(final_list[0][0],final_list[0][1],final_list[0][2],final_list[1][0],sentence_no,no_of_sentences)
    


#print(l)
#draw(['customer','withdrawal','carries'],['withdrawal','amount','withdrawalnumber'],['withdrawal','date'],['withdrawal','time'],[],[],[],['withdrawal','type'],[],[],2)
#draw(['system','user','warns'],['system','id'],['system','modelname','modelnumber'],['system','make'],[],[],[],[],[],[],2)
#draw(['customer','withdrawal','carries'],[],['withdrawal','amount','withdrawalnumber'],['withdrawal','date'],['withdrawal','time'],[],[],[],['withdrawal','type'],[],[],1)
#draw(['customer','withdrawal','carries'],[],[],[],[],[],[],[],[],[],[],2)
#draw(['system','user','warns'],[],[],[],[],[],[],[],[],[],1)
#draw(['Professor','Student','teaches'],[],[],[],[],[],[],[],[],[],[],1)
#draw(['Institute','Details','has'],['Details','Name','Address','Affiliated_to','Affiliationnumber'],[],[],[],[],[],[],[],[],[],1)
#draw([],[],['withdrawal','amount','withdrawalnumber'],['withdrawal','date'],['withdrawal','time'],[],[],[],['withdrawal','type'],[],[],2)

'''draw(['Institute','Student','admits'],['Student','Name','Address','Enrollno'],[],[],[],[],[],[],[],[],4)

draw(['Student','Courses','studies'],['Courses','Mathematics','TOC','Machine Learning'],[]';,[],[],[],[],[],[],[],4)
draw(['Student','Books','reads'],['Books','TOC_hopcroft','OS_Tanenbaum','Booknumber'],[],[],[],[],[],[],[],[],4)'''
#draw(['Student','Library','reads_in'],['Library','Cardnumber','Issued_on','Issued_till'],[],[],[],[],[],[],[],[],5)



#draw(['Employee','Employee','Supervises'],['Employee','Name','Sex','Address','salary'],[],[],[],[],[],[],[],[],5)
#draw(['Employee','Department','Manages'],[],[],[],[],[],[],[],[],[],5)

#draw(['Employee','Dependent','Dependents_of'],[],[],[],[],[],[],[],[],[],5)

#draw(['Employee','Project','Works_on'],['Project','Name','Number','Location'],[],[],[],[],[],[],[],[],5)

#draw(['Department','Project','Controls'],['Department','Name','Number','Location'],[],[],[],[],[],[],[],[],5)



