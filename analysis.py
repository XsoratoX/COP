import os.path
import csv
import numpy as np
import pandas as pd
import MeCab
from gensim.models.doc2vec import Doc2Vec
from sklearn import tree
import graphviz


#initialize MeCab
mecab = MeCab.Tagger()
mecab.parse("")

def read_book(filename):

    if not os.path.exists(filename):
        print("not exist the file")
    #open and read file
    with open(filename, "r+", encoding="shift-jis") as rf:
        return rf.read()

#split words and store an array(morphological analysis)
def split_words(filename):
    node = mecab.parseToNode(filename)
    sp_words = []
    while node is not None:
        part_of_speech = node.feature.split(",")[0]
        if part_of_speech in ["名詞"]:
            sp_words.append(node.surface)
        elif part_of_speech in ["動詞", "形容詞"]:
            sp_words.append(node.feature.split(",")[6])
        node = node.next
    return sp_words

def transfer_csv_from_txt_v1(filename):
    source = filename + ".txt"
    target = filename + ".csv"
    pd.DataFrame(source).to_csv(target)

def transfer_csv_from_txt_v2(filename, dic):
    with open(filename, 'w') as f:
        writer = csv.writer(f)
        for k, v in dic.items():
            writer.writerow([k, v])

def calc_cos(textA, textB):
    #caluculate magnitude of a vector in textA
    lengthA = sum(textA[word] ** 2 for word in textA) ** 0.5

    #caluculate magnitude of a vector in textB
    lengthB = sum(textB[word] ** 2 for word in textB) ** 0.5

    #caluculate a dot vector of textA and textB
    #dotProduct = sum(textA[word] * textB[word] for word in textA.items() & textB.items())
    dotProduct = 0.0
    for keyA,valueA in textA.items():
        for keyB,valueB in textB.items():
            if keyA==keyB:
                dotProduct = dotProduct + valueA*valueB

    #caluculate cosine similarity
    cos = dotProduct / (lengthA * lengthB)
    return cos

def words_to_freqdict(words):
    freqdict = {}
    for word in words:
        if word in freqdict:
            freqdict[word] = freqdict[word] + 1
        else:
            freqdict[word] = 1
    return freqdict

#transfer text to the vector
model = Doc2Vec.load("/Users/iimoritensho/Desktop/programs/python/MachineLearning/NLP/Doc2Vec/aozora.model")
def calc_vecs_d2v(docs):
    vecs = []
    for d in range(docs):
        vecs.append(model.infer_vector(mecab_seq(d)))

def main():
    text1 = []
    freqdic1 = []
    text2 = []
    freqdic2 = []

    path1 = ["./miyazawa_kenji/chumonno_oi_ryoriten.txt", "./miyazawa_kenji/gingatetsudono_yoru.txt", "./miyazawa_kenji/futagono_hoshi.txt"]
    path2 = ["./akutagawa_ryunosuke/rashomon.txt", "./akutagawa_ryunosuke/haruno_yo.txt", "./akutagawa_ryunosuke/katakoi.txt"]
    for i in range(len(path1)):
        text1.insert(i ,split_words(read_book(path1[i])))
        freqdic1.insert(i, words_to_freqdict(text1[i]))

    for j in range(len(path2)):
        text2.insert(j, split_words(read_book(path2[j])))
        freqdic2.insert(j, words_to_freqdict(text2[j]))
    
    freqdic = freqdic1 + freqdic2

    transfer_csv_from_txt_v2("chumonno_oi_ryoriten2.csv", text1[0])

    #cosigne similarity
    cos = []
    for i in range(len(freqdic)):
        for j in range(i+1, len(freqdic)):
            cos.append(calc_cos(freqdic[i], freqdic[j]))

    print("cosign similarity = ", cos)

if __name__ == '__main__':
    main()
