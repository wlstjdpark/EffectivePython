a = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
odds = a[::2]
evens = a[1::2]
print(odds)
print(evens)

x = b'mongoose'
y = x[::-1]
print(y)


w = '안녕하세요'
'''
x = w.encode('utf-8')
y = x[::-1]
z = y.decode('utf-8')
'''

print(w[::-1])

a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
a[::-2]     # ['h', 'f', 'd', 'b']
a[::2]      # ['a', 'c', 'e', 'g']


a[2::2]     # ['c', 'e', 'g']
a[-2::-2]   # ['g', 'e', 'c', 'a']
a[-2:2:-2]  # ['g', 'e']
a[2:2:-2]   # []


b = a[::2]      # ['a', 'c', 'e', 'g']
c = b[1:-1]     # ['c', 'e']


