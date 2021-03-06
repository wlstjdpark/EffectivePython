한 슬라이스에 start, end, stride를 함께 쓰지 말자.
=======

<br />
somelist[::stride]

위와 같이 슬라이스에 간격 줄 수 있다.


이를 이용하여 쉽게 홀수 또는 짝수 인덱스의 아이템을 얻을 수 있다.
```py
a = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
odds = a[::2]
evens = a[1::2]
print(odds)
print(evens)

>>>
['red', 'yellow', 'blue']
['orange', 'green', 'purple']
```

또한 바이트 문자열을 쉽게 역순할 수 있다.
```py
x = b'mongoose'
y = x[::-1]
print(y)

>>>
b'esoognom'
```

그러나 바이트 문자열이나 아스키에는 잘 동작하지만 utf-8 바이트 문자열로 인코드된 유니코드 문자에서는 원하는 대로 동작하지 않는다.
```py
w = '안녕하세요'
x = w.encode('utf-8')
y = x[::-1]
z = y.decode('utf-8')
```
그냥 아래와 같이 사용하면 된다.

```py
w = '안녕하세요'
print(w[::-1])
```

```py
a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
a[::-2]     # ['h', 'f', 'd', 'b']
a[::2]      # ['a', 'c', 'e', 'g']
```
음수를 이용하여 역순을하여 값을 얻을 수도 있다.

```py
a[2::2]     # ['c', 'e', 'g']
a[-2::-2]   # ['g', 'e', 'c', 'a']
a[-2:2:-2]  # ['g', 'e']
a[2:2:-2]   # []
```
start, end와 같이 사용하니 가독성이 매우 떨어진다.

차라리 스트라이드, 슬라이드를 각각 적용하여 사용하는 편이 가독성 면에서 훨씬 낫다.
```py
b = a[::2]      # ['a', 'c', 'e', 'g']
c = b[1:-1]     # ['c', 'e']
```
__슬라이싱부터 하고 스트라이딩을 하게되면 데이터의 얕은 복사복이 생기니 주의하자.__

*시간과 메모리가 충분하지 않다면 내장 모듈 itertools의 islice 메서드를 사용해보자.*

<br />
## 핵심 정리
- 한 슬라이스에 start, end, stride를 지정하면 매우 보기 어렵다.
- 가능하면 stride는 양수로 사용하자.
- start, end, stride 를 모두 사용할 필요가 있다면 스트라이딩을 먼저하고 슬라이딩을 하던가, 내장 모듈인 itertools의 islice를 이용하자.


