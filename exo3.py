'''
    EXO 3
'''

# 1
l = [1, 6, 11, 18, 27, 38, 51, 66, 91, 120]
t = [i for i in l if i%2==0]
print(t)

# 2
l1 = [i**2 for i in range(0, 16)]
l2 = [i for i in range(0, 30) if i%2==1]
voyelles = ['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U', 'y', 'Y']
s = 'MATHEMATIQUES'
l3 = [i for i in s if i in voyelles]
print(l1)
print(l2)
print(l3)

# 3
s = 'Une phrase de test ici'
l = [i for i in s if i not in voyelles]
s = ''.join(l)
print(s)

# 4
l = [
    [1, 2, 3],
    [4, 5 ,6],
    [7, 8, 9, 10]
]
l = [y for x in l for y in x]
print(l)

# 5
s = 'Une phrase de test ici'
l = [len(x) for x in s.split(' ')]
print(l)