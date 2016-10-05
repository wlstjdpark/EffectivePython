a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
print('First four: ', a[:4])
print('Last four:  ', a[-4:])
print('Middle two: ', a[3:-3])

assert a[:5] == a[0:5]

assert a[5:] == a[5:len(a)]

print(a[:])     # ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
print(a[:5])    # ['a', 'b', 'c', 'd', 'e']
print(a[:-1])   # ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(a[4:])    #                     ['e', 'f', 'g', 'h']
print(a[-3:])   #                          ['f', 'g', 'h']
print(a[2:5])   #           ['c', 'd', 'e']
print(a[2:-1])  #           ['c', 'd', 'e', 'f', 'g']
print(a[-3:-1]) #                          ['f', 'g']


first_twenty_items = a[:20]
last_twenty_items = a[-20:]


b = a[4:]
print('Before:    ', b)
b[1] = 99
print('After:     ', b)
print('No Change: ', a)


print('Before:    ', a)
a[2:7] = [99, 24, 14]
print('After:     ', a)

b = a[:]
assert b == a and b is not a


b = a
print('Before:    ', b)
a[:] = [101, 102, 103]
assert a is b               # 여전히 같은 리스트 객체임
print('After:     ', a)      # 참조를 갖고있기 때문에 변화가 같다.
