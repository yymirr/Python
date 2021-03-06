#!/usr/bin/env python3
#
#
# date:     Thu 07 Dec 2017 04:56:40 PM CET
#
# descr:    Uebungsblatt 3


import matplotlib.pyplot as plt
from os import listdir
from os.path import isfile
from random import randint as rand
from functools import reduce



def isReflexive(menge,relation):
    if all((x,x) in relation for x in menge):
        print('ist reflexiv')
    else:
        print('nicht reflexiv')


def isSymmetric(menge,relation):
    if all(tuple(reversed(a)) in relation for a in relation):
        print('ist symmetrisch')
    else:
        print("nicht symmetrisch")


#def isTransitive(menge,relation):
#    pass
#
#def is_transitive(relation):
#    for a,b in relation:
#        for c,d in relation:
#            print(c,d)
#            if b == c and ((a,d) not in relation):
#                    # print (a,b),(c,d) # uncomment for tests...
#                    print('nicht trans')
#                    return False
#    print('trans')
#    return True
#

def teiler(n):
    return [ x for x in range(1,n+1) if n%x==0]



def plotD():

    xAxis = [x for x in range(1,1001)]
    yAxis = [len(teiler(x)) for x in xAxis]

    plt.plot(xAxis,yAxis,'bo')
    plt.show()




def plotBar():
    xAxis = [x for x in range(1,1001)]
    yAxis = [len(teiler(x)) for x in xAxis]

    width = 1/1.5
    plt.bar(xAxis, yAxis, width, color="brown")
    plt.show()



def flachKlopfer(output):
    return reduce(lambda x,y:x+y, map(list, output))


def  maxInList(lst):
    return reduce(lambda x,y: x if (x > y) else y, lst)


def hornerToDecimal(num):
    return reduce(lambda x,y: x+y ,
                 [list(reversed([int(d) for d in str(num)]))[i]*(3**i) for i in range(len(str(num)))])



if __name__ == "__main__":


#     isReflexive([1,2,3],[(1,2),(1,1),(2,2),(2,1),(3,3)])  # -> reflexiv
#     isReflexive([1,2,3],[(1,1),(2,2)])                    # -> nicht reflexiv


#     isSymmetric([1,2,3],[(1,2),(2,1),(2,2),(1,3),(3,1)])   # -> symmetrisch
#     isSymmetric([1,2,3],[(1,2),(2,1),(2,2),(1,3)])         # -> nicht symmetrisch (3,1 nicht enthalten)

    # isTransitive([[1,2,3,4],[(1,2),(2,1),(2,2),(2,3),(1,3),(3,1),(1,1),(3,3),(3,2)] # -> transitiv


    ###########################
    #
    #    Aufgabe 3.1
    #
    #   Python Ausdrücke - keine Kommandos
    #
    #########################


    # die Summe der Zahlen von 0 bis 100 berechnet.
    # sum([x for x in range])


    # die Summe aller durch 3 teilbarer Zahlen von 0 bis 100 berechnet.
    # print(sum([x for x in range(101) if x%3==0]))

    # die Liste aller Zahlen von 0 bis 100 erzeugt, die weder durch 11 noch durch 13 teilbar sind.
    # print([x for x in range(101) if x%11 != 0 and x%13 != 0])

    # Berechnet, wie viele Zahlen zwischen 0 und 1000 eine Quersumme haben, die durch 7 teilbar ist.
    # print(len(list(filter(lambda x: x%7==0,set([(x%10)+(x//10) for x in range(1000)])))))

    # wobei oben set() angewendet wird um zB die Quersummen von 23 und 32 filtern -> eigentlich nicht nötig

    # print(len(list(filter(lambda x: x%7==0,[(x%10)+(x//10) for x in range(1000)]))))



    # print(teiler(45)) # Aufgabe 3.3 A
    # print(teiler(72)) # Aufgabe 3.3 A
    # print(teiler(49)) # Aufgabe 3.3 A

    # print([x for x in range(1,1000) if len(teiler(x))==8 ]) # Aufgabe 3.3 B

    # print(len(max([teiler(x) for x in range(1,1000)], key=len))) # Aufgabe 3.3 C

    # plotD() # Aufgabe 3.3 D -> seltsames Bild

    # plotBar() # Aufgabe 3.3 E

    # listeMitTuplen = [(1,10), ('a','b'), ([1], [2])]
    # print(flachKlopfer(listeMitTuplen))
    # als allererst ist die map Funktion zu betrachten, hier wird für jeden Index der Liste
    # die list Funktion angewendet. Beispiel: (1,10) -> [1,10]; ([1],[2]) -> [[1],[2]]
    # danach folgt die Addition der Listen nach und nach. [1,10]+['a','b'] -> [1,10,'a','b']



    # print([rand(1,6) for x in range(10)]) # Aufgabe 3.2 a)

    # Aufgabe 3.2 b)
    # print(len(list(filter(lambda x: 1 not in x, [[rand(1,6) for x in range(10)] for x in range(100000)])))/100000)


    # print(maxInList([x for x in range(100)])) # -> 99

    # print(hornerToDecimal(110)) # Aufgabe 3.4 c)



    with open('test.txt', 'r') as f:
        # teilA = [len(line) for line in f.readlines()]
        # teilB = " ".join([next(f) for x in range(3)])
        # teilC = "".join(list(reversed(f.readline())))
        # teilD = [len(line[0])  for line in [line.split(" ") for line in f.readlines()]]
        # teilE = "\n".join([line for line in f.readlines() if line.startswith('A')])
        # teilF = [" ".join(zeile ) for zeile in [line.split(" ") for line in f.readlines()] if len(zeile)>6 and " ".join(zeile).startswith('A')]
        # teilH = [line for line in enumerate(list(map(lambda x: x.strip('\n'), f.readlines())), start=1) if len(line[1].split(" "))-1==0]

        # teilI = max([tuple(list(line)+[reduce(lambda x,y: x+y,map(line[1].lower().count, 'aeiou'))])\
                     # for line in enumerate(list(map(lambda x: x.strip('\n'), f.readlines())), start=1)], key=lambda x: x[2])

        # teilJ = max([(line[0],wort,reduce(lambda x,y: x+y, map(wort.lower().count, 'aeiou')))\
        #                       for line in enumerate(list(map(lambda x: x.strip('\n'), f.readlines())), start=1) for wort in line[1].split()],\
        #             key=lambda x: x[2])
        # teilK = [(line[0],line[1][0:2]) for line in enumerate(map(lambda x: x.strip('\n'),f.readlines()), start=1)]

        # teilL = len([wort for line in map(lambda x: x.strip('\n'),f.readlines()) for wort in line.split() if len(wort)>10])
        pass

    # print(teilA)                  # Aufgabe 3.5 a) liste mit den Länge jeder Zeile
    # print(teilB)                  # Aufgabe 3.5 b) die ersten drei zeilen
    # print(teilC)                  # Aufgabe 3.5 c) reversed first line
    # print(teilD)                  # Aufgabe 3.5 d) länge des ersten Wortes jeder Zeile
    # print(teilE)                  # Aufgabe 3.5 e) lines starting with 'A'
    # print(teilF)                  # Aufgabe 3.5 f) lines starting with 'A' and more than 6 words
    # print(teilH)                  # Aufgabe 3.5 h) lines without white spaces
    # print(teilI)                  # Aufgabe 3.5 i) line with the most vowels
    # print(teilJ)                  # Aufgabe 3.5 j) line with the most vowels in a word
    # print(teilK)                  # Aufgabe 3.5 k) only the first two letters of every line
    # print(teilL)                  # Aufgabe 3.5 l) how many words with more than 10letters in file

    # teilG = [(fname," ".join(line)) for fname in list(filter(isfile,listdir('.')))\
    #           for line in list(map(lambda x: x.strip().split(" "),open(fname).readlines()))\
    #          if all(list(map(lambda x: x.isalpha() and x.lower()[0] in 'aeiou', line)))]

    # print(teilG) # Aufgabe 3.5 g)

    # teilM = [fname for fname in filter(isfile,listdir('.')) if fname.endswith('.py')]
    # print(teilM)

    # teilN = [fname for fname in filter(isfile,listdir('.')) if len(fname)>10 and len(open(fname).readlines())>10 ]
    # print(teilN)



