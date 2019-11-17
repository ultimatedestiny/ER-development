from stanfordcorenlp import StanfordCoreNLP

def tr4(sen):
        nlp = StanfordCoreNLP(r'H:\stanford parser\stanford-corenlp-full-2018-10-05')

#sen = "The customer withdrawl with withdrawlamount."

        pos = nlp.pos_tag(sen)

        pos_2 = [list(tup) for tup in pos]

        print(pos_2)

        list_of_nouns = []
        for i in pos_2:
            if i[1].startswith("NN"):
                list_of_nouns.append(i[0])

        print(list_of_nouns)

        attributes_list = []
        for i in range(len(list_of_nouns)):
            for j in range(i+1,len(list_of_nouns)):
                if list_of_nouns[j].startswith(list_of_nouns[i],0,len(list_of_nouns[i])):
                        ct=0
                        for k in attributes_list:
                                if k[0]==list_of_nouns[i]:
                                        k.extend(list_of_nouns[j])
                                        ct=1
                                        break
                        if ct==0:
                                attributes_list.append([list_of_nouns[i],list_of_nouns[j]])

                elif list_of_nouns[i].startswith(list_of_nouns[j],0,len(list_of_nouns[j])):
                        ct=0
                        for k in attributes_list:
                                if k[0]==list_of_nouns[j]:
                                        k.extend(list_of_nouns[i])
                                        ct=1
                                        break
                        if ct==0:
                                attributes_list.append([list_of_nouns[j],list_of_nouns[i]])
        
        print(attributes_list)
        nlp.close()
        return attributes_list