import nltk
from stanfordcorenlp import StanfordCoreNLP
from nltk.tag import StanfordPOSTagger
from collections import defaultdict
from graphviz import Digraph
nlp = StanfordCoreNLP(r'H:\stanford parser\stanford-corenlp-full-2018-10-05')

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
sentence = 'The system will eject the ATM Card.'
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

#PROCEDURE FOR PARSING AND GENERATION OF LIST OF LISTS.
tokenized = ['ROOT-0']
for word in nlp.word_tokenize(sentence):   #TOKENIZATION
    tokenized.append(word)
print(tokenized, )
parsed = nlp.dependency_parse(sentence)   #PARSING TO GET DEPENDENCIES
print(parsed)                              #DEPENDENCIES PRINTED
nlp.close()                         #STANFORD PARSER CLOSED

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
stanford_dir = (r"H:\stanford parser\stanford-postagger-2018-10-16")
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
print(POS_tagged_list)                      # list of lists with pos_tags.

# Function to draw the ER diagram
#currently not used in this moduke

def ER_graph(source_ent, dest_ent, op_name):
    dot = Digraph(comment='sentence structure')
    dot.node('A', source_ent)
    dot.node('B', dest_ent)
    edgename = op_name
    dot.edge('A', 'B', label=edgename)
    dot.render('test-output/ER_Diagram.gv', view=True)


# Procedure to determine sentence structure starts
for n1 in range(len(l3)):
    if(l3[n1][0] == 'nsubj'):      #searching for the first occurence of the 'nsubj' dependency 
        nsubj_A = l3[n1][1]         #storing the 1st numeric value of the 'nsubj' dependency
        nsubj_B = l3[n1][2]         #storing the 2nd numeric value of the 'nsubj' dependency
        n1 = n1 + 1                  #storing the index where the 1st 'nsubj' depenedency occurs.
        for n2 in range(n1, len(l3)):
            if(l3[n2][0] == 'nsubj'):           #searching 2nd occurrence of 'nsubj'
                nsubj_2_A = l3[n2][1]           #storing the dependency numerics
                nsubj_2_B = l3[n2][2]
                for cop in range(len(l3)):
                    if(l3[cop][0] == 'cop'):
                        cop_A = l3[cop][1]              #similarly storing dependency numerics values for cop dependency.
                        cop_B = l3[cop][2]
                        for mark_i in range(len(l3)):
                            if(l3[mark_i][0] == 'mark'):
                                mark_A = l3[mark_i][1]
                                mark_B = l3[mark_i][2]
                                for dob in range(len(l3)):
                                    if(l3[dob][0] == 'dobj'):  # Rule for 1 'dobj'
                                        #no_of_dobj = 1
                                        dobj_A = l3[dob][1]
                                        dobj_D = l3[dob][2]
                                        for ccomp_i in range(len(l3)):
                                            if(l3[ccomp_i][0] == 'ccomp'):
                                                ccomp_A = l3[ccomp_i][1]
                                                ccomp_B = l3[ccomp_i][2]
                                                sentence_structure = "SVDOThatClause"    #list of lists l3 contains 2 nsubj, cop,mark,dobj,comp hence sentence structure is SVDOThat clause.
                                                print(sentence_structure)           #printing sentence structure identified
                                                exit(0)                     #exiting from the program since task completed.
                                sentence_structure = "SVThatClause"     #list l3 contains 2 nsubj,cop,mark but not dobj and ccomp, hence the sent struc is SVTHATCLAUSE.
                                print(sentence_structure)  #printing structure identofied
                                exit(0)     #exiting from program 
                        for dob in range(len(l3)):#above coding does not get 'mark' dependency and hence not to go inside it , hence control comes here to check dependenies after 2 'nsubj' and cop
                            if(l3[dob][0] == 'dobj'):  # Rule for 1 'dobj'
                                #no_of_dobj = 1
                                dobj_A = l3[dob][1]
                                dobj_D = l3[dob][2]
                                for advmod_i in range(len(l3)):
                                    if(l3[advmod_i][0] == 'advmod'):
                                        advmod_A = l3[advmod_i][1]
                                        advmod_B = l3[advmod_i][2]
                                        for advcl_i in range(len(l3)):
                                            if(l3[advcl_i][0] == 'advcl'):
                                                advcl_A = l3[advcl_i][1]
                                                advcl_B = l3[advcl_i][2]
                                                sentence_structure = "SVDOConjClause" #l3 contains 2 nsubj, cop dobj advmod advcl hence struc is SVDOConjClause.
                                                print(sentence_structure)
                                                exit(0)
                for dep_i in range(len(l3)):
                    if(l3[dep_i][0] == 'dep'):
                        dep_A = l3[dep_i][1]
                        dep_B = l3[dep_i][2]
                        for check in range(len(POS_tagged_list)):
                            if(POS_tagged_list[check][0] == tokenized[nsubj_2_A]):
                                if(POS_tagged_list[check][1] == 'VBG'):
                                    sentence_structure = "SVDOPresentPart"
                                    print(sentence_structure)
                                    exit(0)

                        
                for xcomp_i in range(len(l3)):
                    if(l3[xcomp_i][0] == 'xcomp'):
                        xcomp_A = l3[xcomp_i][1]
                        xcomp_B = l3[xcomp_i][2]
                        for check in range(len(POS_tagged_list)):
                            if(POS_tagged_list[check][0] == tokenized[nsubj_2_A]):
                                if(POS_tagged_list[check][1] == 'JJ'):
                                    sentence_structure = 'SVDOAdj'
                                    print(sentence_structure)
                                    exit(0)
                                if(POS_tagged_list[check][1] == 'NN'):
                                    sentence_structure = 'SVDONoun'
                                    print(sentence_structure)
                                    exit(0)
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
                                                exit(0)
                                        sentence_structure = 'SVNotToInf'
                                        print(sentence_structure)
                                        exit(0)
                                sentence_structure = 'SVToInf'
                                print(sentence_structure)
                                exit(0)
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
                                        exit(0)
                                for advmod_i in range(len(l3)):
                                    if(l3[advmod_i][0] == 'advmod'):
                                        advmod_A = l3[advmod_i][1]
                                        advmod_B = l3[advmod_i][2]
                                        sentence_structure = "SVDOConfToInf"
                                        print(sentence_structure)  
                                        exit(0)
                                sentence_structure = "SVDOToInf"
                                print(sentence_structure)
                                exit(0)
                for xcomp_i in range(len(l3)):
                    if(l3[xcomp_i][0] == 'xcomp'):
                        xcomp_A = l3[xcomp_i][1]
                        xcomp_B = l3[xcomp_i][2]
                        sentence_structure = "SVGerund"
                        print(sentence_structure)
                        exit(0)
                for iobj_i in range(len(l3)):
                    if(l3[iobj_i][0] == 'iobj'):
                        iobj_A = l3[iobj_i][1]
                        iobj_B = l3[iobj_i][2]
                        sentence_structure ="SVIODO"
                        print(sentence_structure)
                        exit(0)
                for advmod_i in range(len(l3)):
                    if(l3[advmod_i][0] == 'advmod'):
                        advmod_A = l3[advmod_i][1]
                        advmod_B = l3[advmod_i][2]
                        sentence_structure = "SVDOAdverbial"
                        print(sentence_structure)
                        exit(0)
                for case_i in range(len(l3)):
                    if(l3[case_i][0] == 'case'):
                        case_A = l3[case_i][1] 
                        case_B = l3[case_i][2]
                        for nmod_i in range(len(l3)):
                            if(l3[nmod_i][0] == 'nmod'):
                                nmod_A = l3[nmod_i][1]
                                nmod_B = l3[nmod_i][2]
                                for acl_i in range(len(l3)):
                                    if(l3[acl_i][0] == 'acl'):
                                        acl_A = l3[acl_i][1]
                                        acl_B = l3[acl_i][2]
                                        sentence_structure = "SVDOPastPart"
                                        print(sentence_structure)
                                        exit(0)

                                sentence_structure = "SVDOPO"
                                print(sentence_structure)
                                exit(0)
                for compound_i in range(len(l3)):
                    if(l3[compound_i][0] == 'compound'):
                        compound_A = l3[compound_i][1]
                        compound_B = l3[compound_i][2]
                        compound_i = compound_i + 1
                        for compound_i2 in range(compound_i,len(l3)):
                            if(l3[compound_i2][0] == 'compound'):
                                compound_A_2 = l3[compound_i2][1]
                                compound_B_2 = l3[compound_i2][2]
                                sentence_structure = "SVDO"
                                print(sentence_structure)
                                exit(0)
                        for aux_i in range(len(l3)):
                            if(l3[aux_i][0] == 'aux'):
                                aux_A = l3[aux_i][1]
                                aux_B = l3[aux_i][2]
                                sentence_structure = "SAuxVDO"
                                print(sentence_structure)
                                exit(0)
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
                                exit(0)
                        for n2 in range(n1,len(l3)):
                            if(l3[n2][0] == 'nsubj'):
                                nsubj_2_A = l3[n2][1]
                                naubj_2_B = l3[n2][2]
                                for cop_i in range(len(l3)):
                                    if(l3[cop_i][0] == 'cop'):
                                        cop_A = l3[cop_i][1]
                                        cop_B = l3[cop_i][2]
                                        sentence_structure = "SVConjClause"
                                        print(sentence_structure)
                                        exit(0)
                for cc_i in range(len(l3)):
                    if(l3[cc_i][0] == 'cc'):
                        cc_A = l3[cc_i][1]
                        cc_B = l3[cc_i][2]
                        for conj_i in range(len(l3)):
                            if(l3[conj_i][0] == 'conj'):
                                conj_A = l3[conj_i][1]
                                conj_B = l3[conj_i][2]
                                sentence_structure = 'SVAdverbialADjunct'
                                print(sentence_structure)
                                exit(0)
        for cop_i in range(len(l3)):
            if(l3[cop_i][0] == 'cop'):
                cop_A = l3[cop_i][1]
                cop_B = l3[cop_i][2]
                for compound_i in range(len(l3)):
                    if(l3[compound_i][0] == 'compound'):
                        compound_A = l3[compound_i][1] 
                        compound_B = l3[compound_i][2]
                        for mark_i in range(len(l3)):
                            if(l3[mark_i][0] == 'mark'):
                                mark_A = l3[mark_i][1]
                                mark_B = l3[mark_i][2]
                                sentence_structure = "Conditional"
                                print(sentence_structure)
                                exit(0)
                sentence_structure = "SVPredicative"
                print(sentence_structure)
                exit(0)
        for case_i in range(len(l3)):
            if(l3[case_i][0] == 'case'):
                case_A = l3[case_i][1]
                case_B = l3[case_i][2]
                for nmod_i in range(len(l3)):
                    if(l3[nmod_i][0] == 'nmod'):
                        nmod_A = l3[nmod_i][1]
                        nmod_B = l3[nmod_i][2]
                        for nummod_i in range(len(l3)):
                            if(l3[nummod_i][0] == 'nummod'):
                                nummod_A = l3[nummod_i][1]
                                nummod_B = l3[nummod_i][2]
                                sentence_structure = "SVForComp"
                                print(sentence_structure)
                                exit(0)
                        sentence_structure = "SVPO"
                        print(sentence_structure)
                        exit(0)
        sentence_structure = "SV"
        print(sentence_structure)
        exit(0)
for nsubj_p in range(len(l3)):
    if(l3[nsubj_p][0] == 'nsubjpass'):
        nsubj_p_A = l3[nsubj_p][1]
        nsubj_p_B = l3[nsubj_p][2]
        for auxpass_i in range(len(l3)):
            if(l3[auxpass_i][0] == 'auxpass'):
                auxpass_p_A = l3[auxpass_i][1]
                auxpass_p_B = l3[auxpass_i][2]
                for case_i in range(len(l3)):
                    if(l3[case_i][0] == 'case'):
                        case_A = l3[case_i][1]
                        case_B = l3[case_i][2]
                        for compound_i in range(len(l3)):
                            if(l3[compound_i][0] == 'compound'):
                                compound_A = l3[compound_i][1]
                                compound_B = l3[compound_i][2]
                                for nmod_i in range(len(l3)):
                                    if(l3[nmod_i][0] == 'nmod'):
                                        nmod_A = l3[nmod_i][1]
                                        nmod_B = l3[nmod_i][2]
                                        for aux_i in range(len(l3)):
                                            if(l3[aux_i][0] == 'aux'):
                                                aux_A = l3[aux_i][1]
                                                aux_B = l3[aux_i][2]
                                                sentence_structure = 'SAuxVPassPO'
                                                print(sentence_structure)
                                                exit(0)
                                        sentence_structure = 'SVPassPO'
                                        print(sentence_structure)
                                        exit(0)


