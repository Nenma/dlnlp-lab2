import nltk


grammar1 = nltk.data.load('file:grammar.cfg')

sentence = 'Papa eats octopus in pajamas'
# sentence = 'John often eats sea food or octopus'
# sentence = 'John and Mary eat often together'

sent = sentence.split()
rd_parser = nltk.RecursiveDescentParser(grammar1)
for tree in rd_parser.parse(sent):
    print(tree)
