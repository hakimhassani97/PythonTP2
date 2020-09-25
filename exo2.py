'''
    EXO 2
'''

# 1
l = [1]
print('Liste vide' if len(l)==0 else 'Liste non vide')

# 2
l = [1, 4, 6, 7, 8]
for i in l:
    print(i, '', end='')
print('')
for i in l:
    if i<5:
        print(i, '', end='')
print('')
n = int(input('Saisir un nombre : '))
for i in l:
    if i<n:
        print(i, '', end='')
print('')

# 3
l = []
print('Saisir la liste d\'entiers, inserez un vide pour la fin de saisir')
while True:
    v = input('v['+str(len(l))+'] = ')
    if v=='':
        break
    l.append(int(v))
s = 0
for i in l:
    s += i
print('somme =', s)