from stanfordcorenlp import StanfordCoreNLP
import sys


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



def tr1(sentence):
    nlp = StanfordCoreNLP(r'H:\stanford parser\stanford-corenlp-full-2018-10-05')

# sentence = 'They refuse to permit us to obtain the refusal permit'    
    #sentence = "ATM customer enters the ATM card pin number."
    l = sentence.split()

    pos = nlp.pos_tag(sentence)

    #print(pos)    # Printing pos tags of sentence

    pos_2 = [list(tup) for tup in pos]       #list of tuple to list of list conversion
    
                              #Printing modified pos tags of sentence                       
    pos_2.pop(-1) 
    print((pos_2))                            #removing the full stop
    s= len(pos)
    x=[]
    k=[]

    for i in range(len(pos_2)):
        if (pos_2[i][1].startswith("NN")):
            if((i+1)==len(pos_2)):
                break

            elif((i+1<s) and pos_2[i+1][1].startswith("NN")):

                if((i+2)==len(pos_2)):
                    goto(74)    
            
                elif((i+2<s) and pos_2[i+2][1].startswith("NN") ):

                    if((i+3)==len(pos_2)):
                        goto(68)
                 
                    elif((i+3<s) and  pos_2[i+3][1].startswith("NN")):
                        x.append(pos_2[i][0]+pos_2[i+1][0]+pos_2[i+2][0]+pos_2[i+3][0])
                        k.append([i,i+3])
                        i=i+3
                        if((i+1)==len(pos_2)):
                            break

                    x.append(pos_2[i][0]+pos_2[i+1][0]+pos_2[i+2][0])
                    k.append([i,i+2])
                    i=i+2
                    if((i+1)==len(pos_2)):
                        break

                x.append(pos_2[i][0]+pos_2[i+1][0])
                k.append([i,i+1])
                i=i+1
                if((i+1)==len(pos_2)):
                    break

            if((i+1)==len(pos_2)):
                    break

    #print(k) 
    #print(x)

    i=0

    for [a,b] in k:
        
        for q in range(a,b):
            l.pop(q)
            l.insert(q,"x")
        l[b]=x[i]
        i=i+1       

    #print(l) 
 
    for i in range(len(l)):
        if "x" in l:
            l.remove("x")

    print("")
    print("OUTPUT OF TR1:")
    print(l)
    print("")
    print("")

    k=None
    for i in range(len(l)):
        k=str(k)+" "+l[i]
    k=k+"."    
    t=k[5:]

    #print(k)
    #print(t)

    pos = nlp.pos_tag(t)

    #print(pos)
    nlp.close()
    return t


#tr1("The withdrawer has withdrawl ammount.")