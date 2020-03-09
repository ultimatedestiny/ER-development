#from stanfordcorenlp import StanfordCoreNLP

def tr52_53(sen,POS):
    #nlp = StanfordCoreNLP(r'H:\stanford parser\stanford-corenlp-full-2018-10-05')

    #sen = "CardReader, CashDispenser and ReceiptPrinter are parts of ATM."
    pos = POS
    #pos = nlp.pos_tag(sen)

    #print(pos)

    pos_2 = [list(tup) for tup in pos]
    print(pos_2)

    l = sen.split()
    print(l)


    k=0
    t=0
    for i in range(len(l)):
        if (l[i]=="parts" or l[i]=="consists" or l[i]=="members" or l[i]=="made"):
            if l[i+1]=="of":
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
    print(pos_2)

    m=[]

    if k==1:
        for j in range(t+2,len(l)):
            if (pos_2[j][1].startswith("NN")):
                m.append(pos_2[j][0])
                break    
        for i in range(0,t):
            if (pos_2[i][1].startswith("NN")):
                m.append(pos_2[i][0])

        print("")
        print("OUTPUT OF TR52")
        print(m)
        print("")
        print("")
    #nlp.close()
    return m

#tr52_53("CardReader, CashDispenser and ReceiptPrinter are parts of ATM.")




