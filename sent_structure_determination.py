import nltk
from stanfordcorenlp import StanfordCoreNLP
from nltk.tag import StanfordPOSTagger
from collections import defaultdict
from graphviz import Digraph
nlp = StanfordCoreNLP(r'H:\stanford parser\stanford-corenlp-full-2018-10-05')

#sentence = 'The system sends the user an email.'
#sentence = 'The system informs the user that the battery is full.'
#sentence = 'The system validates that the password is correct.'
#sentence = 'The customer selects not to fill the tank.'
#sentence = 'The system keeps the user waiting.'
#sentence = 'The system keeps the door open.'
#sentence = 'The system will eject the ATM card.'
#sentence = 'The system restarts.'
sentence = 'The system validates that the ATM has enough funds.'

tokenized = ['ROOT-0']
for word in nlp.word_tokenize(sentence):
    tokenized.append(word)
print(tokenized, )
parsed = nlp.dependency_parse(sentence)
print(parsed)
nlp.close()

l1 = []
for i in parsed:
    for j in i:
        l1.append(j)
print(l1)
l2 = defaultdict(list)
length = len(l1)
initial = 0
step = 3
for y in range(0, int(length/3)):
    for x in range(initial, step):
        l2[int(initial/3)].append(l1[x])
    initial = initial + 3
    step = step + 3
print(l2)
l3 = []
for i in range(len(l2)):
    l3.append(l2[i])
print(l3)

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
tagged_dictionary = defaultdict(list)
length = len(tagged_list)
initial = 0
step = 2
for y in range(0, int(length/2)):
    for x in range(initial, step):
        tagged_dictionary[int(initial/2)].append(tagged_list[x])
    initial = initial + 2
    step = step + 2
print(tagged_dictionary)
POS_tagged_list = []
for i in range(len(tagged_dictionary)):
    POS_tagged_list.append(tagged_dictionary[i])
print(POS_tagged_list)

# Function to draw the ER diagram


def ER_graph(source_ent, dest_ent, op_name):
    dot = Digraph(comment='sentence structure')
    dot.node('A', source_ent)
    dot.node('B', dest_ent)
    edgename = op_name
    dot.edge('A', 'B', label=edgename)
    dot.render('test-output/ER_Diagram.gv', view=True)


# Procedure to determine sentence structure starts
#global no_of_nsubj
#global no_of_dobj
for n1 in range(len(l3)):
    if(l3[n1][0] == 'nsubj'):
        #no_of_nsubj = 1
        #no_of_dobj = 0
        nsubj_A = l3[n1][1]
        nsubj_B = l3[n1][2]
        n1 = n1 + 1
        for n2 in range(n1, len(l3)):
            if(l3[n2][0] == 'nsubj'):
                # rules for 2 'nsubj'
                #no_of_nsubj = 2
                #no_of_dobj = 0
                nsubj_2_A = l3[n2][1]
                nsubj_2_B = l3[n2][2]
                for dob in range(len(l3)):
                    if(l3[dob][0] == 'dobj'):  # Rule for 1 'dobj'
                        #no_of_dobj = 1
                        dobj_A = l3[dob][1]
                        dobj_D = l3[dob][2]
                        for mark_i in range(len(l3)):
                            if(l3[mark_i][0] == 'mark'):
                                mark_A = l3[mark_i][1]
                                mark_B = l3[mark_i][2]
                                sentence_structure = 'SVDOThatClause'
                                print(sentence_structure)
                                source_ent = tokenized[nsubj_B]
                                dest_ent = tokenized[dobj_D]
                                op_name = tokenized[nsubj_A]
                                ER_graph(source_ent, dest_ent, op_name)
                                #exit(0)
                        if(tokenized[nsubj_A] == 'has' and tokenized[dobj_A] == 'has'):
                            source_ent = tokenized[dobj_D]
                            dest_ent = tokenized[nsubj_B]
                            op_name = "of"
                            ER_graph(source_ent, dest_ent, op_name)
                            exit(0)
                        elif(tokenized[nsubj_2_A] == 'has' and tokenized[dobj_A] == 'has'):
                            source_ent = tokenized[dobj_D]
                            dest_ent = tokenized[nsubj_2_B]
                            op_name = "of"
                            ER_graph(source_ent, dest_ent, op_name)
                            exit(0)
                for mark_i in range(len(l3)):
                    if(l3[mark_i][0] == 'mark'):
                        mark_A = l3[mark_i][1]
                        mark_B = l3[mark_i][2]
                        sentence_structure = 'SVThatClause'
                        print(sentence_structure)
                        source_ent = tokenized[nsubj_B]
                        dest_ent = tokenized[nsubj_2_B]
                        op_name = tokenized[nsubj_A]
                        ER_graph(source_ent, dest_ent, op_name)
                        exit(0)
                for dep_i in range(len(l3)):
                    if(l3[dep_i][0] == 'dep'):
                        dep_A = l3[dep_i][1]
                        dep_B = l3[dep_i][2]
                        sentence_structure = 'SVDOPresentPart'
                        print(sentence_structure)
                        source_ent = tokenized[nsubj_B]
                        dest_ent = tokenized[nsubj_2_B]
                        op_name = tokenized[dep_A]+" "+tokenized[dep_B]
                        ER_graph(source_ent, dest_ent, op_name)
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
                                    source_ent = tokenized[nsubj_B]
                                    dest_ent = tokenized[nsubj_2_B]
                                    op_name = tokenized[nsubj_A]
                                    ER_graph(source_ent, dest_ent, op_name)
                                    exit(0)

            else:  # Rules for 1 'nsubj'
                for dob in range(len(l3)):
                    if(l3[dob][0] == 'dobj'):  # Rule for 1 'dobj'
                        no_of_dobj = 1
                        dobj_A = l3[dob][1]
                        dobj_D = l3[dob][2]
                        for io in range(len(l3)):
                            if(l3[io][0] == 'iobj'):
                                iobj_A = l3[io][1]
                                iobj_C = l3[io][2]
                                sent_structure = 'SVIODO'
                                print(sent_structure)
                                source_ent = tokenized[nsubj_B]
                                dest_ent = tokenized[dobj_D]
                                op_name = tokenized[nsubj_A]
                                ER_graph(source_ent, dest_ent, op_name)
                                exit(0)
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
                                                sent_structure = 'SVNotToInf'
                                                print(sent_structure)
                                                source_ent = tokenized[nsubj_B]
                                                dest_ent = tokenized[dobj_D]
                                                op_name = tokenized[nsubj_A]
                                                ER_graph(
                                                    source_ent, dest_ent, op_name)
                                                exit(0)
                        for aux_i in range(len(l3)):
                            if(l3[aux_i][0] == 'aux'):
                                aux_A = l3[aux_i][1]
                                aux_B = l3[aux_i][2]
                                sent_structure = 'SAuxVDO'
                                print(sent_structure)
                                source_ent = tokenized[nsubj_B]
                                dest_ent = tokenized[dobj_D]
                                op_name = tokenized[nsubj_A]
                                ER_graph(source_ent, dest_ent, op_name)
                                exit(0)
                '''if(no_of_dobj==0):  # Rule for only 1 'nsubj'
                                        sent_structure = 'SV'
                                        print(sent_structure)
                                        source_ent_and_dest_ent = tokenized[nsubj_B]
                                        op_name = tokenized[nsubj_A]
                                        dot = Digraph(comment='sentence structure')
                                        dot.node('A',source_ent_and_dest_ent)
                                        edgename=op_name
                                        dot.edge('A','A',label=edgename)
                                        dot.render('test-output/sv.gv', view=True)
                                        exit(0)
                                '''
