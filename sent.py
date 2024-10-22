import nltk
import final_sent_struc
from nltk.tokenize import PunktSentenceTokenizer
import nlp_gui
#PunktSentenceTokenizer is used to tokenize sentence, and each token of sentence is itself a sentence, tokens are returned as elements of list.
#Here we also obtain POS tags
#   A team has number of players, not all of whom participate in each game. It is desired to keep track of the players participating in each game for each team, the positions they played in that game and the result of that game.

def call_sent(input_spec):
    #test = input("Enter the specification.")
    test = input_spec

    train_text = test     #text used to train the PunktSentenceTokenizer
    sample_text = test     #text on which PunktsentenceTokenizer is applied after training it.
    
    custom_sent_tokenizer = PunktSentenceTokenizer(train_text)  #PunktSentenceTokenizer gets trained from train_text and stores it's observations
                                                                #in an object called custom_sent_tokenizer
    tokenized = custom_sent_tokenizer.tokenize(sample_text)     #custom_sent_tokenizer is then used to tokenize the sample text.
                                                                #sample_text is a single sentence, hence output is also a single sentence.
    print(tokenized)                      
    final_sent_struc.sent_token(tokenized)  
            