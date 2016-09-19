map과 filter 대신 리스트 컴프리헨션을 사용하자
=============

파이썬에는 한 리스트에서 다른 리스트를 만들어내는 간결한 문법이 있다.

이 문법을 사용한 표현식을 __컴프리헨션__(list comprehension; 리스트 함축 표현식)이라 한다.
<br /><br />

예를 들어 리스트에 있는 각 숫자의 제곱근을 구할 때, 아래와 같이 계산식과 루프로 돌릴 입력 시퀀스를 작성해서 이 계산을 수행할 수 있다.
```py
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squares = [x**2 for x in a]
print(squares)

>>>
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
```

map을 쓰려면 계산에 필요한 lambda 함수를 생성해야해서 직관적이지 않다.
```py
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squares = map(lambda x: x ** 2, a)
print(list(squares))

>>>
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
```
###### *map을 사용하면 임시로 map 인스턴스를 만드는 비용이 추가된다. (http://www.pythontutor.com/)*
<br />

만약 2로 나누어 떨어지는 숫자의 제곱만 계산한다고 할 때, __컴프리헨션__에서는 루프 뒤에 조건식을 추가할 수 있다.
```py
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_squares = [x**2 for x in a if x % 2 == 0]
print(even_squares)

>>>
[4, 16, 36, 64, 100]
```

map의 경우는 __filter__와 연계해서 사용하여 같은 값을 얻을 수 있지만 읽기가 어렵다.
```py
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_squares = map(lambda x: x*2, filter(lambda: x: x%2 == 0, a))
```
<br />

딕셔너리와 셋에서도 리스트 컴프리헨션에 해당하는 문법이 있다.
컴프리헨션 문법을 쓰면 알고리즘을 작성할 때 파생되는 자료구조를 쉽게 생성할 수 있다.
```py
chile_ranks = {'ghost': 1, 'habanero': 2, 'cayenne': 3}
rank_dict = {rank: name for name, rank in chile_ranks.items()}
chile_len_set = {len(name) for name in chile_ranks}
print(rank_dict)
print(chile_len_set)

>>>
{1: 'ghost', 2: 'habanero', 3: 'cayenne'}
{8, 5, 7}
```

<br />
## 핵심 정리
1. 리스트 컴프리헨션은 lambda 표현식이 필요 없어서 내장 함수인 map이나 filter를 사용하는 것보다 명확하다.
2. 리스트 컴프리헨션을 사용하여 map의 filter보다 편리하게 조건식을 작성할 수 있다.
3. 딕셔너리와 세트로 컴프리헨션 표현식을 지원한다.<br />
*4. map을 사용하고 list로 변경할 때는 map 인스턴스 생성 비용이 추가로 든다.*
