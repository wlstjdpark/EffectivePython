복잡한 표현식 대신 헬퍼 함수를 작성하자
=========

```py
from urllib.parse import parse_qs
my_values = parse_qs('red=5&blue=0&green=', keep_blank_values=True)
print(repr(my_values))

>>>
{'blue': ['0'], 'green': [''], 'red': ['5']}
```
url에서 쿼리 문자열을 디코드하여 딕셔너리에 넣었다.


```py
print('Red:         ', my_values.get('red'))
print('Blue:        ', my_values.get('blue'))
print('Green:       ', my_values.get('green'))
print('Opacity:     ', my_values.get('opacity'))

>>>
Red:          ['5']
Blue:         ['0']
Green:        ['']
Opacity:     None
```
위에서 green은 값이 비어있고, opacity는 아예 존재하지 않는다.

<br />
__파이썬 문법에서는 빈 문자열, 빈 리스트, 0은 모두 암시적으로 False로 평가된다.__

<br />
만약 값이 존재하지 않거나 키가 비어있을 때는 디폴트 값을 넣는다고 할 때,
or 연산자를 사용할 수 있다.
```py
# 쿼리 문자열 red=5&blue=0&green=
red = my_values.get('red', [''])[0] or 0
blue = my_values.get('blue', [''])[0] or 0
green = my_values.get('green', [''])[0] or 0
opacity = my_values.get('opacity', [''])[0] or 0
print('Red:         %r' % red)
print('Blue:        %r' % blue)
print('Green:       %r' % green)
print('Opacity:     %r' % opacity)

>>>
Red:         '5'
Blue:        '0'
Green:       0
Opacity:     0
```
이는 첫 번째 서브 표현식이 False 일 때 or 연산자 뒤에 오는 서브 표현식의 결과가 온다.

이 표현식은 읽기가 어렵고 모든 파라미터 값이 정수가 되게할 경우에는 각 표현식을 int로 변환 해야한다.
```py
red = int(my_values.get('red', [''])[0] or 0)
```
이 코드는 읽기 매우 어렵고, 시각적 방해 요소가 너무 많다.
코드를 사용하기에도 쉽지 않아 보인다.

<br />
파이썬 2.5에 추가된 if/else 조건식 (삼항 표현식)을 사용하면 코드를 짧고 명확하게 표현할 수 있다.
```py
red = my_values.get('red', [''])
red = int(red[0]) if red[0] else 0
print(red)

>>>
5
```
하지만 여러 줄에 걸친 if/else 문을 대체할 정도로 명확하지는 않다.

아래처럼 모든 로직을 펼쳐서 보면 더 복잡해 보인다.
```py
green = my_values.get('green', [''])
if green[0]:
    green = int(green[0])
else:
    green = 0
```

그리고 같은 로직을 반복해서 사용한다면 헬퍼 함수를 만드는 게 좋다.
```py
def get_first_int(values, key, default=0):
    found = values.get(key, [''])
    if found[0]:
        found = int(found)
    else:
        found = default
    return found
```

호출할 때 훨씬 더 명확해졌다.
```py
green = get_first_int(my_values, 'green')
```
무조건 짧은 코드를 만들기보다는 가독성을 선택하는 편이 낫다.

<br />
## 핵심 정리
- 복잡한 표현식은 헬퍼 함수를 이용하자. 특히 중복 코드를 없앨 때 사용한다.
- if/else 표현식을 이용하면 or, and 같은 연산자보다 읽기 수월한 코드가 된다.
- 복잡한 문법을 한 줄에 표현하기보다 가독성을 선택하자.

