'''
    EXO1
'''
# 1
s = 'Une chaine de test ici'
n = 0
for i in s:
    n += 1
print('n =', n, ', len =', len(s))

# 2
s = 'Une chaine de test ici'
while len(s)>0:
    n = 0
    for i in s:
        if i==s[0]:
            n += 1
    print(s[0]+'('+str(n)+')', ',', end='')
    s = s.replace(s[0], '')
print('')

# 3
s = input('La chaine = ')
if len(s)<2:
    r = ''
else:
    r = s[0:2]+s[-2:]
print(r)

# 4
s = input('La chaine a remplacer = ')
s = s[0] + s[1:].replace(s[0], '$')
print(s)

# 5
s1 = input('La 1ere chaine = ')
s2 = input('La 2eme chaine = ')
s = s2[:2] + s1[2:] + ' ' + s1[:2] + s2[2:]
print(s)

# 6
s = input('s = ')
if len(s)>=6:
    if s[-2:]=='is':
        s += 'sement'
    else:
        s += 'is'
print(s)

# 7
n = int(input('Donnez n : '))
s = input('s : ')
if n<=len(s):
    s = s[:n-1] + s[n:]
    print(s)

# 8
s = 'hakimhassani'
l = list(s)
l = [l[i] for i in range(0, len(l)) if i%2==0]
s = ''.join(l)
print(s)

# 9
s = 'un paragraphe un paragraphe un un test'
l = s.split(' ')
while len(l)>0:
    n = 0
    for w in l:
        if l[0]==w:
            n += 1
    l = [x for x in l if x!=l[0]]
    print(w[0]+'('+str(n)+')')

# 10
s = input('Une phrase : ')
print(s.upper())
print(s.lower())
print(s[0].upper()+s[1:].lower())
l = s.split(' ')
for i in range(0, len(l)):
    l[i] = l[i][0].upper()+l[i][1:].lower()
s = ' '.join(l)
print(s)

# 11
s = input('List avec des virgules : ')
l = s.split(',')
l.sort()
s = ','.join(l)
print('sorted :', s)

# 12
s = 'https://docs.python.org/fr/3/tutorial/introduction.html#strings'
c = '/'
for i in range(len(s)-1, -1, -1):
    if s[i]!=c:
        s = s[0:i]
    else:
        s = s[0:i]
        break
print(s)

# 13
s = 'aBzKZCb'
l = list(s)
l.sort(key=lambda s: s.lower())
s = ''.join(l)
print(s)