from stanfordcorenlp import StanfordCoreNLP
def tr5(sentence,POS):
    nlp = StanfordCoreNLP(r'H:\stanford parser\stanford-corenlp-full-2018-10-05')
    #sentence = 'The system validates that the ATM has enough funds'

    tokenized=['ROOT-0']
    for word in nlp.word_tokenize(sentence):
        tokenized.append(word)
    pos = POS
    #pos = nlp.pos_tag(sentence)
    pos_2 = [list(tup) for tup in pos]
    print(pos_2)

    o=[]
    for i in range(len(pos_2)):
        if pos_2[i][0]==',':                             
            o.append(i)
    #print(o)
    for i in range(len(o)):
        pos_2.pop(o[i])
        for j in range(i,len(o)):
            o[j]=o[j]-1
    pos_2.pop(-1)
    print(pos_2)

    Q=None
    for i in range(len(pos_2)):
        Q=str(Q)+" "+pos_2[i][0]    
    j=Q[5:]
    print(j)
    #print(pos_2)
    parsed = nlp.dependency_parse(j)
    parsed2 = [list(s) for s in parsed]
    print(parsed2)
    nlp.close()
    l=sentence.split()
    print(l)

    def check_has(a):
        if l[a-1]=="has":
            return 1
        else:
            return 0

    k=0
    m=[]
    for i in parsed2:
        if i[0]=="nsubj":
            m.append(i[2])
            k=check_has(i[1])
            if k==0:
                del m[0:]
                continue
            for j in parsed2:
                if j[0]=="dobj":
                    k=check_has(j[1])
                    m.append(j[2])
                else:
                    k=0
        

                

    A=[]
    if k!=0:
        for i in range(len(m)):
            A.append(l[m[i]-1])
    
    print("")
    print("OUTPUT OF TR5")
    print(A)
    print("")
    print("")
    return A

#tr5("The system validates that the ATM has enough funds.")