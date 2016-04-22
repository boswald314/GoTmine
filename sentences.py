import nltk

charFile = open("characters.txt",'r')
characters = charFile.read().split('\n')
charFile.close()


def ie_preprocess(document):
    sentences = nltk.sent_tokenize(document)
    sentences = [nltk.word_tokenize(sent) for sent in sentences]
    sentences = [nltk.pos_tag(sent) for sent in sentences]

book = open("1-AGameofThrones/gameofthrones.txt")
#res = ie_preprocess(book.read())
sent = nltk.sent_tokenize(book.read())
book.close()

out = open("sentences.txt",'w')
for x in sent:
    if x[-1] != '"':
        out.write(x+'\n')
    elif (x[0] == '"'):
        out.write('\n' + x)
    else:
        out.write(" "+x)
out.close()

