noMutant = [
    ['A','T','G','C','G','A'],
    ['C','A','G','T','G','C'],
    ['T','T','A','T','T','T'],
    ['A','G','A','C','G','G'],
    ['G','C','G','T','C','A'],
    ['T','C','A','C','T','G']
]
#case 1: first element
#HORIZONTAL,vertical,oblicuo
#ATGCGA,ACTAGT,AACCG
#case 2: last element
#HORIZONTAL,vertical,oblicuo
#AGCGTA,ACTGAG,AGTACT
#TODO: search in one position after - missing
adn = ['ATGCGA']
adn1 = ['ATGCGA','CAGTGC','TTATGT','AGAAGG','ACTGAG','GGTGCT']
def existnoMutant(sequence):
    if len(sequence) == 6:
        for a in sequence:
            for idxnm,nm in enumerate(noMutant):
                for idxn,n in enumerate(nm):
                    if  (a == n and idxn == 0 and idxnm == 0) or (a == n and idxn == 5 and idxnm == 5):
                        if idxn == 0 and idxnm == 0:
                            #SEARCH HORIZONTAL
                            mutant = ''.join([str(item)for item in noMutant[idxnm]])
                            if mutant == sequence:
                                print(mutant,sequence)
                                return True
                            #SEARCH VERTICAL
                            mutant = ''.join([str(item[0])for item in noMutant])
                            if mutant == sequence:
                                print(mutant,sequence)
                                return True
                            #SEARCH OBLICUA
                            mutant = []
                            i = 0
                            for idxn,n in enumerate(noMutant):
                                mutant.append(n[i])
                                i += 1
                                continue
                            mutant = ''.join([str(item)for item in mutant])
                            if mutant == sequence:
                                print(mutant,sequence)
                                return True
                        else:
                            #SEARCH HORIZONTAL INVERT
                            mutant = ''.join([str(item)for item in noMutant[0]])[::-1]
                            if mutant == sequence:
                                print(mutant,sequence)
                                return True
                            #SEARCH VERTICAL INVERT
                            mutant = ''.join([str(item[5])for item in noMutant])
                            if mutant == sequence:
                                print(mutant,sequence)
                                return True
                            #SEARCH OBLICUA INVERT
                            mutant = []
                            i = 5
                            for idxn,n in enumerate(noMutant):
                                mutant.append(n[i])
                                i -= 1
                                continue
                            mutant = ''.join([str(item)for item in mutant])
                            if mutant == sequence:
                                print(mutant,sequence)
                                return True
                            
                    
                    
    
isMutant = False
for sequence in adn:
    if existnoMutant(sequence):
        isMutant = True
    else:
        isMutant = False