print('foo bar')
print('%r' % 'foo bar')


print(5)
print('5')



print('%s' % 5)



print('%s' % 'test')
print('%r' % 'test')

a = '\x07'
print(a)
print(repr(a))

print(eval(repr(a)))


class TestClass(object):
    def __repr__(self):
        return 'zzzzzzz'

obj = TestClass()
print(obj)

print(obj.__dict__)