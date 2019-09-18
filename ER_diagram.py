from stanfordcorenlp import StanfordCoreNLP 
from graphviz import Digraph

nlp = StanfordCoreNLP(r'H:\stanford parser\stanford-corenlp-full-2018-10-05')#location of parser
dot = Digraph(comment='sentence structure') 	#initializing digraph

class entity_class:			#class to draw entity 
	def __init__(self):
		self.x = "A"
		self.y = "B"
		self.source_ent=""
		self.dest_ent=""
		self.op_name = ""

	def entity(self,source_ent,dest_ent): 
		self.source_ent = source_ent
		self.dest_ent = dest_ent
		dot.node(self.x,self.source_ent)
		dot.node(self.y,self.dest_ent)

	def operation(self,op_name):
		self.op_name = op_name
		dot.edge(self.x,self.y,label=self.op_name)
		dot.render('test-output/firsttry6.gv', view=True)

	
def sentence_structure():
	sentence = input("Enter the sentence.")
	#Tokenizing the sentence :
	tokenized = ['ROOT-0']
	for word in nlp.word_tokenize(sentence):
		tokenized.append(word)

	#Parsing the sentence to get dependencies
	parsed = nlp.dependency_parse(sentence)
	#parsed : contains dependencies in the form of tuple of 3 elements
	#parsed is a list in the form of indexes of word in the sentences with dependency number
	#This is not convenient so we store it in the form of dictionary with names in the below code.
	newsent= {}
	for(a,b,c) in parsed :
		newsent.update({a:(tokenized[b],tokenized[c])})
	
	print(newsent)	#newsent contains dependencies with names
	
	if(('nsubj')and('iobj')and('dobj')in newsent):
		#sent_structure ='SVIODO'
		source_ent=newsent['nsubj'][1]
		dest_ent=newsent['iobj'][1]
		op_name=newsent['dobj'][0]+'\n'+newsent['dobj'][1]
	#if(('nsubj')and('dobj')and('mark')and())
	del newsent['ROOT']
	#print(newsent)
	#sent_structure = 'SVIODO'
	
	#print(source_ent)
	#print(dest_ent)
	#print(op_name)
	obj1 = entity_class()
	obj1.entity(source_ent,dest_ent)
	obj1.operation(op_name)
	
sentence_structure()
nlp.close()
