from spam import *
from hham import *
from eham import *
#words > 14 charachters are probably non english meaningful  words
#and counts number of all words(excluding filtered ones) in spam/eham/hham mails (summation of occurrences of all words)
def remove_big_words_from_list():
    ehamCounter,hhamCounter,spamCounter=0,0,0
    for i in eham:
        if len(i[0]) > 14:
            eham.remove(i)
        else:
            ehamCounter+=int(i[i])

    for i in spam:
        if len(i[0]) > 14:
            spam.remove(i)
        else:
            spamCounter+=int(i[i])

    for i in hham:
        if len(i[0]) > 14:
            hham.remove(i)
        else:
            hhamCounter+=int(i[i])
    return eham,hham,spam,ehamCounter,hhamCounter,spamCounter









