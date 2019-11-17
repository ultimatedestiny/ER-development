from stanfordcorenlp import StanfordCoreNLP

def tr48(sen):
    nlp = StanfordCoreNLP(r'H:\stanford parser\stanford-corenlp-full-2018-10-05')

    #sen = "Memory has types RAM and ROM."

    pos = nlp.pos_tag(sen)

    #print(pos)

    pos_2 = [list(tup) for tup in pos]
    print(pos_2)

    l = sen.split()
    print(l)

    k=0
    t=0
    for i in range(len(l)):
        if l[i]=="has":
            if l[i+1]=="types":
                k=1
                t=i 


    """All this overhead below is for removing coma"""

    o=[]
    for i in range(len(pos_2)):
        if pos_2[i][0]==',':                             
            o.append(i)
    print(o)
    for i in range(len(o)):
        pos_2.pop(o[i])
        for j in range(i,len(o)):
            o[j]=o[j]-1
    """ till here """

    m=[]
    if k==1:
        for j in range(0,t):
            if (pos_2[j][1].startswith("NN")):
                m.append(pos_2[j][0])
                break    
        for i in range(t+2,len(pos_2)):
            if (pos_2[i][1].startswith("NN")):
                m.append(pos_2[i][0])

        print(m)
    nlp.close()
    return m
    
#tr48("Memory has types RAM and ROM.")
