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

# 4
l = []
print('Saisir la liste d\'entiers pour chercher max min, inserez un vide pour la fin de saisir')
mx = -99999999999
mn = 99999999999
while True:
    v = input('v['+str(len(l))+'] = ')
    if v=='':
        break
    v = int(v)
    if v>mx:
        mx = v
    if v<mn:
        mn = v
    l.append(v)
print('max =', mx, ', max() =', max(l))
print('min =', mn, ', min() =', min(l))

# 5
mots = []
print('Saisir la liste des mots, vide pour arret')
while True:
    mot = input('mots['+str(len(mots))+'] = ')
    if mot=='':
        break
    mots.append(mot)
n = int(input('Donnez la taille du mot n : '))
for mot in mots:
    if len(mot)>n:
        print(mot)

# 6
mots = ['abc', 'xyz', 'aba', '1221']
n = 0
for i in mots:
    if len(i)>2 and i[0]==i[-1]:
        n += 1
print('Nombre :', n)

# 7
l = ['abc', 'xyz', 'aba', '1221']
l2 = ['abc', 'xyz', 'aba', '1221']
l.pop(-1)
l.extend(l2)
print(l)

# 8
lists = [
    [1, 2, 3, 4, 5],
    [2, 7, 9, 19, 10],
    [10, 100, 9],
    [0, 0]
]
mx = -9999999999
lmx = []
for l in lists:
    s = 0
    for i in l:
        s += i
    if s>mx:
        mx = s
        lmax = l
    print(s, mx)
print('max sum =', lmax)

# 9
lists =  [[15, 25], [45], [40, 57, 27], [15, 25], [32], [45]]
exist = []
for l in lists:
    if l not in exist:
        exist.append(l)
l = exist
print(l)

# 10
l = [{1:''}, {}, {'g':'hakim'}]
b = True
for i in l:
    if len(i)!=0:
        b = False
        break
if b:
    print('Tous les elements vides')
else:
    print('Sont pas tous vides')