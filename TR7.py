from stanfordcorenlp import StanfordCoreNLP

def tr7(sen,POS):

    nlp = StanfordCoreNLP(r'H:\stanford parser\stanford-corenlp-full-2018-10-05')

    #sen = "The system prompts for the userName and password of the customer."

    tokenized=['ROOT-0']
    for word in nlp.word_tokenize(sen):
        tokenized.append(word)

    print(tokenized)    

    parsed = nlp.dependency_parse(sen)
    print(parsed)

    parsed2= [list(n) for n in parsed]

    print(parsed2)

    l=sen.split()

    def check_has(a):
        if l[a-1]=="of":
            return 1
        else:
            return 0

    k=0
    m=[]

    for i in parsed2:
        if i[0]=="prep":
            m.append(i[1])
            k=check_has(i[2])
            if k==0:
                del m[0:]
                continue
            for j in parsed2:
                if j[0]=="pobj":
                    k=check_has(j[1])
                    m.append(j[2])
                else:
                    k=0

    A=[]
    if k!=0:
        for i in range(len(m)):
            A.append(l[m[i]-1])
    print(A)
    nlp.close()
    return A