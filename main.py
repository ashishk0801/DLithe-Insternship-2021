
l1 = ['Y','Z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','A','B']
l3=[]
inp1 = input('Enter message to be encoded: ')
inp2 = input('Enter message to be decoded: ')
if inp2 == '':
    for i in inp1:
        if i in l1:
            i=l1[l1.index(i)+2]
            l3.append(i)
    l2s=''.join([str(j) for j in l3])
    print('Encoded message: ',l2s)

elif inp1 == '':
    for i in inp2:
        if i in l1:
            i=l1[l1.index(i)-2]
            l3.append(i)
    l2s=''.join([str(j) for j in l3])
    print('Decoded Message: ',l2s)