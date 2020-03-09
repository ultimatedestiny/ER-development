#from stanfordcorenlp import StanfordCoreNLP
# the function adds , elements as attributes to the entity

def newTr(sen,POS,PARSED,TOKENIZED):
#def newTr():
        #nlp = StanfordCoreNLP(r'H:\stanford parser\stanford-corenlp-full-2018-10-05')

        #sen = "The system warns the user."

        pos = POS
        #pos = nlp.pos_tag(sen)

        pos_2 = [list(tup) for tup in pos]

        print(pos_2)
        k=0
        o=[]
        for i in range(len(pos_2)):
            if pos_2[i][0]==',':                             
                o.append(pos[i-1][0])
                k=i
        if k!=0:
            o.append(pos[k+1][0])

        print(o)
   

        #tokenized = ['ROOT-0']
        #for word in nlp.word_tokenize(sen):   #TOKENIZATION
        #  tokenized.append(word)
        tokenized = TOKENIZED
        print(tokenized)
        parsed = PARSED
        #parsed = nlp.dependency_parse(sen)
        #nlp.close()
        print(parsed)
        parsed_2 = [list(par) for par in parsed]
        li=[]
        for y in parsed_2:
                if y[0]=='nsubj':
                        li.append(tokenized[y[2]])
        for x in o:
                li.append(x)
        print("")
        print("OUTPUT OF NEW TR :")
        print(li)
        print("")
        return li                       # return a list with 1st element entity and rest attributes     


#newTr()



