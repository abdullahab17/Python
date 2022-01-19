europe = {'spain':'madrid','france':'paris','germany':'berlin','norway':'oslo'}
print(europe)
europe['italy'] = 'Rome'
print(europe)
europe['poland'] ='warsaw'
print(europe)
print('italy' in europe)

europe['austrailia'] ='canberra'
print(europe)

del europe['austrailia']
print(europe)