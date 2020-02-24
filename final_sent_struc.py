import sys
from stanfordcorenlp import StanfordCoreNLP
from nltk.tag import StanfordPOSTagger
from collections import defaultdict
import TR1
import TR4
import TR5
import TR6
import TR7
import TR8
import TR9
import TR47
import TR48
import TR52_53
import finalgraph


#sentence = 'The manager assists his subordinates to calculate price.'
#sentence = 'The system sends the user an email.'
#sentence = 'The system informs the user that the battery is full.'
#sentence = 'The system validates that the password is correct.'
#sentence = 'The system warns the user not to restart the system'
#sentence = 'The customer selects not to fill the tank.'
#sentence = 'The system marks the errors to be red.'
#sentence = 'The system commands the motor to start.'
#sentence = 'The system keeps the user waiting.'
#sentence = 'The system validates the record entered by the customer.'
#sentence = 'The system keeps the door open.'
#sentence = 'The system makes the user an administrator.'
#sentence = 'The system tells the user where to go.'
#sentence = 'The system stops the motor when the tank is full.'
#sentence = 'The server responds the query quickly.'
#sentence = 'The system will eject the ATM Card.'
#sentence = 'The system sends the message to the customer.'
#sentence = 'The system guides where to go.'
#sentence = 'The motor stops when the tank is full.'
#sentence = 'The system starts to fill the tank.'
#sentence = 'The printer starts printing the document.'
#sentence = 'The elevator moves up or down.'
#sentence = 'The customer is employee.'
#sentence = 'The system waits for 5 seconds.'
#sentence = 'The ATM Card is ejected by the system.'
#sentence = 'The ATM Card will be ejected by the system.'
#sentence = 'The system prompts for password.'
#sentence = 'If the ATM card is valid.'
#sentence = 'The system restarts.'
#sentence = 'The system validates that the ATM has enough funds.'
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

def sent_token(sentence_tokenized):
    para_length = len(sentence_tokenized)
    for i in range(len(sentence_tokenized)):
        print(sentence_tokenized[i])
        feed = sentence_tokenized[i]
        feed2 = TR1.tr1(feed)
        print("\n")
        L3,POS,TOKENIZED,PARSED = parsing_tokinizing(feed2)
        attr4 = TR4.tr4(feed2,POS)
        attr5 = TR5.tr5(feed2,POS,TOKENIZED,PARSED)
        attr6 = TR6.tr6(feed2,POS,TOKENIZED,PARSED)
        attr7 = TR7.tr7(feed2,POS,TOKENIZED,PARSED)
        attr8 = TR8.tr8(feed2,POS)
        attr9 = TR9.tr9(feed2,POS,TOKENIZED,PARSED)
        attr47 = TR47.tr47(feed2,POS)
        attr48 = TR48.tr48(feed2,POS)
        attr52_53 = TR52_53.tr52_53(feed2,POS)
        if (len(attr4) == len(attr5) == len(attr6) == len(attr7) == len(attr8) == len(attr9) == len(attr47) == len(attr48) == len(attr52_53) == 0):
            print(1)
            entities_relationships_list = sentence_structure_determine(L3,TOKENIZED,POS)
            finalgraph.draw(entities_relationships_list,attr4,attr5,attr6,attr7,attr8,attr9,attr47,attr48,attr52_53,para_length)
        else:
            finalgraph.draw([],attr4,attr5,attr6,attr7,attr8,attr9,attr47,attr48,attr52_53,para_length)



def parsing_tokinizing(sentence):
    nlp = StanfordCoreNLP(r'H:\stanford parser\stanford-corenlp-full-2018-10-05')
    tokenized = ['ROOT-0']
    for word in nlp.word_tokenize(sentence):   #TOKENIZATION
        tokenized.append(word)
    print(tokenized, )
    parsed = nlp.dependency_parse(sentence)   #PARSING TO GET DEPENDENCIES
    print(parsed)                              #DEPENDENCIES PRINTED
    l1 = []
    for i in parsed:
        for j in i:
            l1.append(j)
    print(l1)                        # LIST CONTAINING ALL DEPENDENCIES AS INDIVIDUAL ELEMENTS IN THE LIST.
    l2 = defaultdict(list)          #OBJECT CREATED TO CONVERT THE LIST INTO dictionary
    length = len(l1)
    initial = 0
    step = 3
    for y in range(0, int(length/3)):
        for x in range(initial, step):
            l2[int(initial/3)].append(l1[x])
        initial = initial + 3
        step = step + 3             # sets of 3 elements from the l1 list are created, containg dependency with antecedent and consequet numerics.
    print(l2)                       # dictionary printed where the key are system generated numeric values and value for each numeric key is the set of 3 elements created above.
    l3 = []                     #empty list which will be used as a container for lists, hence l3 ill be list of lists.
    for i in range(len(l2)):
        l3.append(l2[i])        #her each value set from the dictionnary is treated as a sigle element and appended in the list l3.
    print(l3)
    #PROCEDURE FOR pos TAGGING SIMILAR TO THE PROCEDURE DEFINED ABOVE FOR PARSING.
    #FROM LINE 70 TO LINE 80 THERE IS AN EXTRA CODE USEFUL IN POS TAGGING,HERE WE REMOVE THE root KEYWORD FROM THE TEXT AFTER TOKENIZATON, 
    #CLUB THEM AGAIN TOGETHER TO FORM THE SENTENCE BUT FULL STOP SEPARATED. tHIS IS NECESSARY IN POS TAGGING AS IF FULL STOP IS NOT SEPARATED FROM TEXT, IT 
    #POS TAGGING RESULT OFTEN COMES WRONG, SOMETIMES TREATING VERN AS NOUN.
    tokenized_modified = []        
    for i in range(len(tokenized)):
        tokenized_modified.append(tokenized[i])
    tokenized_modified.pop(len(tokenized_modified)-1)
    tokenized_modified.pop(0)
    print(tokenized_modified)
    text = ""
    for i in range(len(tokenized_modified)):
        text = text + tokenized_modified[i]
        text = text + " "
    print(text)
    #STANFORD TAGGER OPENED
    '''stanford_dir = (r"H:\stanford parser\stanford-postagger-2018-10-16")
    modelfile = stanford_dir+(r"\models\english-bidirectional-distsim.tagger")
    jarfile = stanford_dir+(r"\stanford-postagger.jar")
    tagger = StanfordPOSTagger(model_filename=modelfile, path_to_jar=jarfile)
    tagged = tagger.tag(text.split())
    tagged_list = []
    for i in tagged:
        for j in i:
            tagged_list.append(j)
    print(tagged_list)
    tagged_dictionary = defaultdict(list)       #similar to dictionary formed in parsing
    length = len(tagged_list)
    initial = 0
    step = 2                                    #dictionary with value length ==2.
    for y in range(0, int(length/2)):
        for x in range(initial, step):
            tagged_dictionary[int(initial/2)].append(tagged_list[x])
        initial = initial + 2
        step = step + 2
    print(tagged_dictionary)
    POS_tagged_list = []
    for i in range(len(tagged_dictionary)):
        POS_tagged_list.append(tagged_dictionary[i])
    print(POS_tagged_list)                      # list of lists with pos_tags.'''
    #real tagger by vishal

    tagged = nlp.pos_tag(text)

    print("hey --->> ",tagged)    # Printing pos tags of sentence

    POS_tagged_list = [list(tup) for tup in tagged]  
    print("hey --->> ",POS_tagged_list)     #list of tuple to list of list conversion
    nlp.close()
    return l3,tagged,tokenized,parsed


#PROCEDURE FOR PARsSING AND GENERATION OF LIST OF LISTS.
def sentence_structure_determine(l3,TOKENIZED,POS):
    try:
        tokenized = TOKENIZED
        POS_tagged_list = POS
        for n1 in range(len(l3)):
            if(l3[n1][0] == 'nsubj'):      #searching for the first occurence of the 'nsubj' dependency 
                nsubj_A = l3[n1][1]         #storing the 1st numeric value of the 'nsubj' dependency
                nsubj_B = l3[n1][2]         #storing the 2nd numeric value of the 'nsubj' dependency
                n1 = n1 + 1                  #storing the index where the 1st 'nsubj' depenedency occurs.
                for n2 in range(n1, len(l3)):
                    if(l3[n2][0] == 'nsubj'):           #searching 2nd occurrence of 'nsubj'
                        nsubj_2_A = l3[n2][1]           #storing the dependency numerics
                        nsubj_2_B = l3[n2][2]
                        for mark_i in range(len(l3)):
                            if(l3[mark_i][0] == 'mark'):
                                mark_A = l3[mark_i][1]
                                mark_B = l3[mark_i][2]
                                for dob in range(len(l3)):
                                    if(l3[dob][0] == 'dobj'):  # Rule for 1 'dobj'
                                        #no_of_dobj = 1
                                        dobj_A = l3[dob][1]
                                        dobj_D = l3[dob][2]
                                        sentence_structure = "SVDOThatClause"    #list of lists l3 contains 2 nsubj, cop,mark,dobj,comp hence sentence structure is SVDOThat clause.
                                        print(sentence_structure)           #printing sentence structure identified
                                        entity_1 = tokenized[nsubj_B]
                                        entity_2 = tokenized[dobj_D]
                                        relationship = tokenized[dobj_A]
                                        o = []
                                        o.append(entity_1)
                                        o.append(entity_2)
                                        o.append(relationship)
                                        return o
        for n1 in range(len(l3)):
            if(l3[n1][0] == 'nsubj'):      #searching for the first occurence of the 'nsubj' dependency 
                nsubj_A = l3[n1][1]         #storing the 1st numeric value of the 'nsubj' dependency
                nsubj_B = l3[n1][2]         #storing the 2nd numeric value of the 'nsubj' dependency
                n1 = n1 + 1                  #storing the index where the 1st 'nsubj' depenedency occurs.
                for n2 in range(n1, len(l3)):
                    if(l3[n2][0] == 'nsubj'):           #searching 2nd occurrence of 'nsubj'
                        nsubj_2_A = l3[n2][1]           #storing the dependency numerics
                        nsubj_2_B = l3[n2][2]
                        for mark_i in range(len(l3)):
                            if(l3[mark_i][0] == 'mark'):
                                mark_A = l3[mark_i][1]
                                mark_B = l3[mark_i][2]
                                sentence_structure = "SVThatClause"     #list l3 contains 2 nsubj,cop,mark but not dobj and ccomp, hence the sent struc is SVTHATCLAUSE.
                                print(sentence_structure)  #printing structure identofied
                                entity_1 = tokenized[nsubj_B]
                                entity_2 = tokenized[nsubj_2_B]
                                relationship = tokenized[nsubj_A]
                                o = []
                                o.append(entity_1)
                                o.append(entity_2)
                                o.append(relationship)
                                return o
        for n1 in range(len(l3)):
            if(l3[n1][0] == 'nsubj'):      #searching for the first occurence of the 'nsubj' dependency 
                nsubj_A = l3[n1][1]         #storing the 1st numeric value of the 'nsubj' dependency
                nsubj_B = l3[n1][2]         #storing the 2nd numeric value of the 'nsubj' dependency
                n1 = n1 + 1                  #storing the index where the 1st 'nsubj' depenedency occurs.
                for n2 in range(n1, len(l3)):
                    if(l3[n2][0] == 'nsubj'):           #searching 2nd occurrence of 'nsubj'
                        nsubj_2_A = l3[n2][1]           #storing the dependency numerics
                        nsubj_2_B = l3[n2][2]
                        for dob in range(len(l3)):#above coding does not get 'mark' dependency and hence not to go inside it , hence control comes here to check dependenies after 2 'nsubj' and cop
                            if(l3[dob][0] == 'dobj'):  # Rule for 1 'dobj'
                                #no_of_dobj = 1
                                dobj_A = l3[dob][1]
                                dobj_D = l3[dob][2]
                                for advmod_i in range(len(l3)):
                                    if(l3[advmod_i][0] == 'advmod'):
                                        advmod_A = l3[advmod_i][1]
                                        advmod_B = l3[advmod_i][2]
                                        sentence_structure = "SVDOConjClause" #l3 contains 2 nsubj, cop dobj advmod advcl hence struc is SVDOConjClause.
                                        print(sentence_structure)
                                        entity_1 = tokenized[nsubj_B]
                                        entity_2 = tokenized[dobj_D]
                                        relationship = tokenized[nsubj_A]
                                        o = []
                                        o.append(entity_1)
                                        o.append(entity_2)
                                        o.append(relationship)
                                        return o
        for n1 in range(len(l3)):
                if(l3[n1][0] == 'nsubj'):      #searching for the first occurence of the 'nsubj' dependency 
                    nsubj_A = l3[n1][1]         #storing the 1st numeric value of the 'nsubj' dependency
                    nsubj_B = l3[n1][2]         #storing the 2nd numeric value of the 'nsubj' dependency
                    n1 = n1 + 1                  #storing the index where the 1st 'nsubj' depenedency occurs.
                    for n2 in range(n1, len(l3)):
                        if(l3[n2][0] == 'nsubj'):           #searching 2nd occurrence of 'nsubj'
                            nsubj_2_A = l3[n2][1]           #storing the dependency numerics
                            nsubj_2_B = l3[n2][2]
                            for dep_i in range(len(l3)):
                                if(l3[dep_i][0] == 'dep'):
                                    dep_A = l3[dep_i][1]
                                    dep_B = l3[dep_i][2]
                                    sentence_structure = "SVDOPresentPart"
                                    print(sentence_structure)
                                    entity_1 = tokenized[nsubj_B]
                                    entity_2 = tokenized[nsubj_2_B]
                                    relationship = tokenized[nsubj_A]+tokenized[nsubj_2_A]
                                    o = []
                                    o.append(entity_1)
                                    o.append(entity_2)
                                    o.append(relationship)
                                    return o
        for n1 in range(len(l3)):
                if(l3[n1][0] == 'nsubj'):      #searching for the first occurence of the 'nsubj' dependency 
                    nsubj_A = l3[n1][1]         #storing the 1st numeric value of the 'nsubj' dependency
                    nsubj_B = l3[n1][2]         #storing the 2nd numeric value of the 'nsubj' dependency
                    n1 = n1 + 1                  #storing the index where the 1st 'nsubj' depenedency occurs.
                    for n2 in range(n1, len(l3)):
                        if(l3[n2][0] == 'nsubj'):           #searching 2nd occurrence of 'nsubj'
                            nsubj_2_A = l3[n2][1]           #storing the dependency numerics
                            nsubj_2_B = l3[n2][2]
                            for xcomp_i in range(len(l3)):
                                if(l3[xcomp_i][0] == 'xcomp'):
                                    xcomp_A = l3[xcomp_i][1]
                                    xcomp_B = l3[xcomp_i][2]
                                    for check in range(len(POS_tagged_list)):
                                        if(POS_tagged_list[check][0] == tokenized[nsubj_2_A]):
                                            if(POS_tagged_list[check][1] == 'JJ'):
                                                sentence_structure = 'SVDOAdj'
                                                print(sentence_structure)
                                                entity_1 = tokenized[nsubj_B]
                                                entity_2 = tokenized[nsubj_2_B]
                                                relationship = tokenized[nsubj_A]
                                                o = []
                                                o.append(entity_1)
                                                o.append(entity_2)
                                                o.append(relationship)
                                                return o
                                            if(POS_tagged_list[check][1] == 'NN'):
                                                    sentence_structure = 'SVDONoun'
                                                    print(sentence_structure)
                                                    entity_1 = tokenized[nsubj_B]
                                                    entity_2 = tokenized[nsubj_2_B]
                                                    relationship = tokenized[nsubj_A]
                                                    o = []
                                                    o.append(entity_1)
                                                    o.append(entity_2)
                                                    o.append(relationship)
                                                    return o
        for n1 in range(len(l3)):
                if(l3[n1][0] == 'nsubj'):      #searching for the first occurence of the 'nsubj' dependency 
                    nsubj_A = l3[n1][1]         #storing the 1st numeric value of the 'nsubj' dependency
                    nsubj_B = l3[n1][2]         #storing the 2nd numeric value of the 'nsubj' dependency
                    n1 = n1 + 1    
                    for dob in range(len(l3)):
                        if(l3[dob][0] == 'dobj'):  # Rule for 1 'dobj'
                            #no_of_dobj = 1
                            dobj_A = l3[dob][1]
                            dobj_D = l3[dob][2]
                            dob = dob +1
                            for mark_i in range(len(l3)):
                                if(l3[mark_i][0] == 'mark'):
                                    mark_A = l3[mark_i][1]
                                    mark_B = l3[mark_i][2]
                                    for xcomp_i in range(len(l3)):
                                        if(l3[xcomp_i][0] == 'xcomp'):
                                            xcomp_A = l3[xcomp_i][1]
                                            xcomp_B = l3[xcomp_i][2]
                                            for neg_i in range(len(l3)):
                                                if(l3[neg_i][0] == 'neg'):
                                                    neg_A = l3[neg_i][1]
                                                    neg_B = l3[neg_i][2]
                                                    for dob2 in range(dob, len(l3)):
                                                        if(l3[dob2][0] == 'dobj'):
                                                            dobj_2_A = l3[dob2][1]
                                                            dobj_2_B = l3[dob2][2]
                                                            sentence_structure ='SVDONotToInf'
                                                            print(sentence_structure)
                                                            entity_1 = tokenized[nsubj_B]
                                                            entity_2 = tokenized[dobj_D]
                                                            relationship = tokenized[nsubj_A]
                                                            o = []
                                                            o.append(entity_1)
                                                            o.append(entity_2)
                                                            o.append(relationship)
                                                            return o
                                                            #entity_matrix.append(entity_1,entity_2,relationship)
                                                            #transform.SVDONotToInf(entity_1, entity_2, relationship)
                                                            goto(803)
                                                            #exit(0)
                                                    sentence_structure = 'SVNotToInf'
                                                    print(sentence_structure)
                                                    entity_1 = tokenized[nsubj_B]
                                                    entity_2 = tokenized[dobj_D]
                                                    relationship = tokenized[nsubj_A]
                                                    o = []
                                                    o.append(entity_1)
                                                    o.append(entity_2)
                                                    o.append(relationship)
                                                    return o
        for n1 in range(len(l3)):
                if(l3[n1][0] == 'nsubj'):      #searching for the first occurence of the 'nsubj' dependency 
                    nsubj_A = l3[n1][1]         #storing the 1st numeric value of the 'nsubj' dependency
                    nsubj_B = l3[n1][2]         #storing the 2nd numeric value of the 'nsubj' dependency
                    n1 = n1 + 1                
                    for mark_i in range(len(l3)):
                        if(l3[mark_i][0] == 'mark'):
                            mark_A = l3[mark_i][1]
                            mark_B = l3[mark_i][2]
                            for xcomp_i in range(len(l3)):
                                if(l3[xcomp_i][0] == 'xcomp'):
                                    xcomp_A = l3[xcomp_i][1]
                                    xcomp_B = l3[xcomp_i][2]
                                    sentence_structure = 'SVToInf'
                                    print(sentence_structure)
                                    for dob in range(len(l3)):
                                        if(l3[dob][0] == 'dobj'):
                                            dobj_A = l3[dob][1]
                                            dobj_B = l3[dob][2]
                                            entity_1 = tokenized[nsubj_B]
                                            entity_2 = tokenized[dobj_B]
                                            relationship = tokenized[nsubj_A]
                                            o = []
                                            o.append(entity_1)
                                            o.append(entity_2)
                                            o.append(relationship)
                                            return o
                                    else:
                                        entity_1 = tokenized[nsubj_B]
                                        entity_2 = tokenized[nsubj_B]
                                        relationship = tokenized[nsubj_A]
                                        o = []
                                        o.append(entity_1)
                                        o.append(entity_2)
                                        o.append(relationship)
                                        print("")
                                        print("")
                                        print("")
                                        print("")
                                        return o
        for n1 in range(len(l3)):
                if(l3[n1][0] == 'nsubj'):      #searching for the first occurence of the 'nsubj' dependency 
                    nsubj_A = l3[n1][1]         #storing the 1st numeric value of the 'nsubj' dependency
                    nsubj_B = l3[n1][2]         #storing the 2nd numeric value of the 'nsubj' dependency
                    n1 = n1 + 1     
                    for dob in range(len(l3)):
                        if(l3[dob][0] == 'dobj'):  # Rule for 1 'dobj'
                            #no_of_dobj = 1
                            dobj_A = l3[dob][1]
                            dobj_D = l3[dob][2]
                            dob = dob +1
                            for mark_i in range(len(l3)):
                                if(l3[mark_i][0] == 'mark'):
                                    mark_A = l3[mark_i][1]
                                    mark_B = l3[mark_i][2]
                                    for advcl_i in range(len(l3)):
                                        if(l3[advcl_i][0] == 'advcl'):
                                            advcl_A = l3[advcl_i][1]
                                            advcl_B = l3[advcl_i][2]
                                            for cop_i in range(len(l3)):
                                                if(l3[cop_i][0] == 'cop'):
                                                    cop_A = l3[cop_i][1]
                                                    cop_B = l3[cop_i][2]
                                                    sentence_structure ="SVDOtobeComp"
                                                    print(sentence_structure)
                                                    entity_1 = tokenized[nsubj_B]
                                                    entity_2 = tokenized[dobj_D]
                                                    relationship = tokenized[nsubj_A]
                                                    o = []
                                                    o.append(entity_1)
                                                    o.append(entity_2)
                                                    o.append(relationship)
                                                    return o
                                            for advmod_i in range(len(l3)):
                                                if(l3[advmod_i][0] == 'advmod'):
                                                    advmod_A = l3[advmod_i][1]
                                                    advmod_B = l3[advmod_i][2]
                                                    sentence_structure = "SVDOConjToInf"
                                                    print(sentence_structure)  
                                                    entity_1 = tokenized[nsubj_B]
                                                    entity_2 = tokenized[dobj_D]
                                                    relationship = tokenized[nsubj_A]
                                                    o = []
                                                    o.append(entity_1)
                                                    o.append(entity_2)
                                                    o.append(relationship)
                                                    return o
                                            sentence_structure = "SVDOToInf"
                                            print(sentence_structure)
                                            entity_1 = tokenized[nsubj_B]
                                            entity_2 = tokenized[dobj_D]
                                            relationship = tokenized[nsubj_A]
                                            o = []
                                            o.append(entity_1)
                                            o.append(entity_2)
                                            o.append(relationship)
                                            return o                                     
        for n1 in range(len(l3)):
                if(l3[n1][0] == 'nsubj'):      #searching for the first occurence of the 'nsubj' dependency 
                    nsubj_A = l3[n1][1]         #storing the 1st numeric value of the 'nsubj' dependency
                    nsubj_B = l3[n1][2]  
                    for xcomp_i in range(len(l3)):
                        if(l3[xcomp_i][0] == 'xcomp'):
                            xcomp_A = l3[xcomp_i][1]
                            xcomp_B = l3[xcomp_i][2]
                            sentence_structure = "SVGerund"
                            print(sentence_structure)
                            entity_1 = tokenized[nsubj_B]
                            relationship = tokenized[nsubj_A]
                            for dob in range(len(l3)):
                                if(l3[dob][0] == 'dobj'):  # Rule for 1 'dobj'
                                    #no_of_dobj = 1
                                    dobj_A = l3[dob][1]
                                    dobj_D = l3[dob][2]
                                    dob = dob +1
                                    entity_2 = tokenized[dobj_D]
                                else:
                                    entity_2 = tokenized[nsubj_B]
                            o = []
                            o.append(entity_1)
                            o.append(entity_2)
                            o.append(relationship)
                            return o
        for n1 in range(len(l3)):
                if(l3[n1][0] == 'nsubj'):      #searching for the first occurence of the 'nsubj' dependency 
                    nsubj_A = l3[n1][1]         #storing the 1st numeric value of the 'nsubj' dependency
                    nsubj_B = l3[n1][2]  
                    for dob in range(len(l3)):
                        if(l3[dob][0] == 'dobj'):  # Rule for 1 'dobj'
                            #no_of_dobj = 1
                            dobj_A = l3[dob][1]
                            dobj_D = l3[dob][2]
                            dob = dob +1
                            for iobj_i in range(len(l3)):
                                if(l3[iobj_i][0] == 'iobj'):
                                    iobj_A = l3[iobj_i][1]
                                    iobj_B = l3[iobj_i][2]
                                    sentence_structure ="SVIODO"
                                    print(sentence_structure)
                                    entity_1 = tokenized[nsubj_B]
                                    entity_2 = tokenized[dobj_D]
                                    relationship = tokenized[nsubj_A]
                                    o = []
                                    o.append(entity_1)
                                    o.append(entity_2)
                                    o.append(relationship)
                                    return o
                            for advmod_i in range(len(l3)):
                                if(l3[advmod_i][0] == 'advmod'):
                                    advmod_A = l3[advmod_i][1]
                                    advmod_B = l3[advmod_i][2]
                                    sentence_structure = "SVDOAdverbial"
                                    print(sentence_structure)
                                    entity_1 = tokenized[nsubj_B]
                                    entity_2 = tokenized[dobj_D]
                                    relationship = tokenized[nsubj_A]
                                    o = []
                                    o.append(entity_1)
                                    o.append(entity_2)
                                    o.append(relationship)
                                    return o
                            for acl_i in range(len(l3)):
                                if(l3[acl_i][0] == 'acl'):
                                    acl_A = l3[acl_i][1]
                                    acl_B = l3[acl_i][2]
                                    sentence_structure = "SVDOPastPart"
                                    print(sentence_structure)
                                    entity_1 = tokenized[nsubj_B]
                                    entity_2 = tokenized[acl_A]
                                    relationship = tokenized[nsubj_A]
                                    o = []
                                    o.append(entity_1)
                                    o.append(entity_2)
                                    o.append(relationship)
                                    return o
                            for nmod_i in range(len(l3)):
                                if((l3[nmod_i][0] == 'nmod') or (l3[nmod_i][0] == 'nmod:poss')):
                                    nmod_A = l3[nmod_i][1]
                                    nmod_B = l3[nmod_i][2]
                                    sentence_structure = "SVDOPO"
                                    print(sentence_structure)
                                    entity_1 = tokenized[nsubj_B]
                                    relationship = tokenized[nsubj_A]
                                    entity_2 = tokenized[nmod_B]
                                    o = []
                                    o.append(entity_1)
                                    o.append(entity_2)
                                    o.append(relationship)
                                    return o
                            sentence_structure = "SVDO"
                            print(sentence_structure)
                            entity_1 = tokenized[nsubj_B]
                            entity_2 = tokenized[dobj_D]
                            relationship = tokenized[nsubj_A]
                            o = []
                            o.append(entity_1)
                            o.append(entity_2)
                            o.append(relationship)
                            return o
        for n1 in range(len(l3)):
                if(l3[n1][0] == 'nsubj'):      #searching for the first occurence of the 'nsubj' dependency 
                    nsubj_A = l3[n1][1]         #storing the 1st numeric value of the 'nsubj' dependency
                    nsubj_B = l3[n1][2]  
                    for aux_i in range(len(l3)):
                        if(l3[aux_i][0] == 'aux'):
                            aux_A = l3[aux_i][1]
                            aux_B = l3[aux_i][2]
                            for dob in range(len(l3)):
                                if(l3[dob][0] == 'dobj'):  # Rule for 1 'dobj'
                                    #no_of_dobj = 1
                                    dobj_A = l3[dob][1]
                                    dobj_D = l3[dob][2]
                                    dob = dob +1
                                    sentence_structure = "SAuxVDO"
                                    print(sentence_structure)
                                    entity_1 = tokenized[nsubj_B]
                                    entity_2 = tokenized[dobj_D]
                                    relationship = tokenized[nsubj_A]
                                    o = []
                                    o.append(entity_1)
                                    o.append(entity_2)
                                    o.append(relationship)
                                    return o
                    for advmod_i in range(len(l3)):
                        if(l3[advmod_i][0] == 'advmod'):
                            advmod_A = l3[advmod_i][1]
                            advmod_B = l3[advmod_i][2]
                            for advcl_i in range(len(l3)):
                                if(l3[advcl_i][0] == 'advcl'):
                                    advcl_A = l3[advcl_i][1]
                                    advcl_B = l3[advcl_i][2]
                                    for mark_i in range(len(l3)):
                                        if(l3[mark_i][0] == 'mark'):
                                            mark_A = l3[mark_i][1]
                                            mark_B = l3[mark_i][2]
                                            sentence_structure = 'SVConjToInf'
                                            print(sentence_structure)
                                            entity_1 = tokenized[nsubj_B]
                                            entity_2 = tokenized[nsubj_B]
                                            relationship = tokenized[nsubj_A]
                                            o = []
                                            o.append(entity_1)
                                            o.append(entity_2)
                                            o.append(relationship)
                                            return o
                                    for n2 in range(n1,len(l3)):
                                        if(l3[n2][0] == 'nsubj'):
                                            nsubj_2_A = l3[n2][1]
                                            nsubj_2_B = l3[n2][2]
                                            sentence_structure = "SVConjClause"
                                            print(sentence_structure)
                                            entity_1 = tokenized[nsubj_B]
                                            entity_2 = tokenized[nsubj_B]
                                            relationship = tokenized[nsubj_A]
                                            o = []
                                            o.append(entity_1)
                                            o.append(entity_2)
                                            o.append(relationship)
                                            return o
                            sentence_structure = 'SVAdverbialAdjunct'
                            print(sentence_structure)
                            entity_1 = tokenized[nsubj_B]
                            entity_2 = tokenized[nsubj_B]
                            relationship = tokenized[nsubj_A]
                            o = []
                            o.append(entity_1)
                            o.append(entity_2)
                            o.append(relationship)
                            return o
                    for cop_i in range(len(l3)):
                        if(l3[cop_i][0] == 'cop'):
                            cop_A = l3[cop_i][1]
                            cop_B = l3[cop_i][2]
                            sentence_structure = "SVPredicative"
                            print(sentence_structure)
                            entity_1 = tokenized[cop_A]
                            entity_2 = tokenized[nsubj_B]
                            relationship = tokenized[cop_B]   #generalisation
                            o = []
                            o.append(entity_1)
                            o.append(entity_2)
                            o.append(relationship)
                            return o
        for n1 in range(len(l3)):
                if(l3[n1][0] == 'nsubj'):      #searching for the first occurence of the 'nsubj' dependency 
                    nsubj_A = l3[n1][1]         #storing the 1st numeric value of the 'nsubj' dependency
                    nsubj_B = l3[n1][2]  
                    for nmod_i in range(len(l3)):
                        if(l3[nmod_i][0] == 'nmod:poss'):    #earlier nmod:poss was nmod
                            nmod_A = l3[nmod_i][1]
                            nmod_B = l3[nmod_i][2]
                            sentence_structure = "SVForComp or SVPO"
                            print(sentence_structure)
                            entity_1 = tokenized[nsubj_B]
                            relationship = tokenized[nsubj_A]
                            entity_2 = tokenized[nmod_B]
                            o = []
                            o.append(entity_1)
                            o.append(entity_2)
                            o.append(relationship)
                            print("")
                            return o
        for n1 in range(len(l3)):
                if(l3[n1][0] == 'nsubj'):      #searching for the first occurence of the 'nsubj' dependency 
                    nsubj_A = l3[n1][1]         #storing the 1st numeric value of the 'nsubj' dependency
                    nsubj_B = l3[n1][2]  
                    sentence_structure = "SV"
                    print(sentence_structure)
                    #entity_1 = tokenized[nsubj_B]
                    #entity_2 = tokenized[nsubj_B]
                    #relationship = tokenized[nsubj_A]
                    entity_1 = tokenized[nsubj_B]
                    entity_2 = entity_1
                    relationship = tokenized[nsubj_A]
                    o = []
                    o.append(entity_1)
                    o.append(entity_2)
                    o.append(relationship)
                    print("\n")
                    print("\n")
                    return o
        for nsubj_p in range(len(l3)):
                if(l3[nsubj_p][0] == 'nsubjpass'):
                    nsubj_p_A = l3[nsubj_p][1]
                    nsubj_p_B = l3[nsubj_p][2]
                    for nmod_i in range(len(l3)):
                        if(l3[nmod_i][0] == 'nmod'):
                            nmod_A = l3[nmod_i][1]
                            nmod_B = l3[nmod_i][2]
                            sentence_structure = 'SAuxVPassPO or SVPassPO'
                            print(sentence_structure)
                            entity_1 = tokenized[nmod_B]
                            entity_2 = tokenized[nsubj_p_B]
                            relationship = tokenized[nsubj_p_A]
                            o = []
                            o.append(entity_1)
                            o.append(entity_2)
                            o.append(relationship)
                            return o
    except:
        pass