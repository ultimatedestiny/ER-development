from stanfordcorenlp import StanfordCoreNLP

def tr8(sen,POS):
    #nlp = StanfordCoreNLP(r'H:\stanford parser\stanford-corenlp-full-2018-10-05')

    #sen = "The system prompts for customer’s address."

    pos = POS
    #pos = nlp.pos_tag(sen)
    #nlp.close()
    pos_2 = [list(tup) for tup in pos]
    
    o=[]
    for i in range(len(pos_2)):
        if pos_2[i][0]==',':                             
            o.append(i)
    #print(o)
    for i in range(len(o)):
        pos_2.pop(o[i])
        for j in range(i,len(o)):
            o[j]=o[j]-1

    print(pos_2)
    attribute_list = []
    for i in range(len(pos_2)):
        if pos_2[i][1]=="POS":
            attribute_list.append([pos_2[i-1][0],pos_2[i+1][0]])

    print("")
    print("OUTPUT OF TR8")
    print(attribute_list)
    print("")
    print("")
    return attribute_list
        
#tr8("The system prompts for customer’s address.")