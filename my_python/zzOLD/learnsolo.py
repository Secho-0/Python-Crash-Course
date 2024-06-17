def CracklePop(x):
    for  i in range(x):
        if i > 0:
            if  ((i % 5 == 0) & (i % 3 ==0)):
                print('CracklePop')
            elif (i % 3 == 0):
                print('Crackle')
            elif (i % 5 == 0) :
                print('Pop')
            else:
                print(i)

CracklePop(101)
