import nltk
from nltk.tokenize import PunktSentenceTokenizer
from stanfordcorenlp import StanfordCoreNLP
nlp = StanfordCoreNLP(r'H:\stanford parser\stanford-corenlp-full-2018-10-05')

sentence = 'Repeat'

tokenized=['ROOT-0']
for word in nlp.word_tokenize(sentence):
    tokenized.append(word)
print(tokenized, )

parsed = nlp.dependency_parse(sentence)
print('parsed = ',parsed)
nlp.close()

train_text = sentence     #text used to train the PunktSentenceTokenizer
sample_text = sentence     #text on which PunktsentenceTokenizer is applied after training it.

custom_sent_tokenizer = PunktSentenceTokenizer(train_text)  #PunktSentenceTokenizer gets trained from train_text and stores it's observations
                                                            #in an object called custom_sent_tokenizer
tokenized = custom_sent_tokenizer.tokenize(sample_text)     #custom_sent_tokenizer is then used to tokenize the sample text.
                                                            #sample_text is a single sentence, hence output is also a single sentence.
                                                            #sentence is returned as a single element of the list.

def process_content():
    try:
        for i in tokenized:                 # i represents element of list named tokenized, and this element is a sentence
            words = nltk.word_tokenize(i)   # words is a list storing words of the sentence as elements. 
            tagged = nltk.pos_tag(words)    # determine pos_tag of each element of the list words and returns as a list of tuples
                                            # each tuple comtains 2 elements, word and the pos_tag for it.
            print(tagged)
    except Exception as e:                  # in case an exception arises it is stored in variable e.
            print(str(e))                   # exception printed as a string.

process_content()