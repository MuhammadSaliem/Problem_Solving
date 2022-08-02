
def minion_game(txt):
    Vowels = ['A', 'E', 'I', 'U', 'O']
    Stuart = 0
    Kevin = 0
    for i, v in enumerate(txt):
        if v in Vowels:
            Stuart += len(txt) - i
        else:
            Kevin += len(txt) - i
        print("{} {} {}".format(txt[i:], Stuart, Kevin))
    if(Stuart == Kevin):
        print("Draw")
    else:
        print("Stuart {}".format(Stuart)) if Stuart > Kevin else print("Kevin {}".format(Kevin))

minion_game(input())
