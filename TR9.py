from stanfordcorenlp import StanfordCoreNLP

def tr9(sen,POS):
    nlp = StanfordCoreNLP(r'H:\stanford parser\stanford-corenlp-full-2018-10-05')

    #sen = "The system informs the interested user"

    tokenized=['ROOT-0']
    for word in nlp.word_tokenize(sen):
        tokenized.append(word)

    print(tokenized)    
    parsed = nlp.dependency_parse(sen)
    print(parsed)

    k=0
    l=0
    count=0
    attribute_list=[]

    parsed_2 = [list(i) for i in parsed]
    print(parsed_2)
    

    for i in range(len(parsed_2)):

        if(parsed_2[i][0]=="amod"):
            count=1
            k=parsed_2[i][1]
            l=parsed_2[i][2]
            attribute_list.append([tokenized[k],tokenized[l]])
    nlp.close()
    if count==0:
        attribute_list = []
    
    print("")
    print("OUTPUT OF TR9")
    print(attribute_list)  
    print("")
    print("")    
    return attribute_list

#tr9("The system informs the interested user.")