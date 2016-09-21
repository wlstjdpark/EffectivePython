컴프리헨션이 클 때는 제네레이터 표현식을 고려하자
========

<br />
리스트 컴프리헨션의 문제는 입력 시퀀스에 있는 각 아이템별로 새 리스트를 생성하는 단점이 있다.

만약 이 값이 매우 크면 메모리가 부족한 현상이 발생할 수 있다.

다음은 입력 값이 적다고 가정하고 리스트 컴프리헨션을 사용한 예다.
```py
value = [len(x) for x in open('./tmp/my_file.txt')]
print(value)

>>>
[22, 6, 8, 7, 100, 45]
```

<br />
위와 같은 상황에선 __제네레이터 표현식(generator expression)__을 사용하자.

generator expression은 실행될 때 출력 시퀀스를 메모리에 로딩하지 않고, iterator를 통해 한 번에 한 아이템만 출력한다.

<br />
generator expression은 리스트 컴프리헨션과 유사하게 () 문자 사이에 문법을 넣는다.

이전 코드와 동일한 기능을 generator expression으로 작성한 예다.
```py
it = (len(x) for x in open('./tmp/my_file.txt'))
print(it)

>>>
<generator object <genexpr> at 0x016C3870>
```
generator expression의 경우 iterator로 평가되어 더는 진행되지 않는다.

iterator의 값을 얻으려면 아래와 같이 next를 사용하면 된다.
```py
print(next(it))
print(next(it))
print(next(it))

>>>
22
6
8
```

<br />
__generator expression의 추가적인 장점은 다른 generator expression과 함께 사용할 수 있는 점이다.__

위의 generator expression을 통해 얻은 iterator를 또 다른 generator expression의 입력으로 사용한 예다.
```py
it = (len(x) for x in open('./tmp/my_file.txt'))
roots = ((x, x**0.5) for x in it)
print(next(roots))
print(next(roots))
print(next(roots))

>>>
(22, 4.69041575982343)
(6, 2.449489742783178)
(8, 2.8284271247461903)
```
iterator를 전진시킬 때마다 루프 내부 iterator도 전진시키고 표현식을 계산하여 입력과 출력을 처리한다.

*for 루프에 iterator를 사용하면 내부적으로 iter(value)를 호출하고, iter은 value.\_\_iter\_\_를 호출한다.*

*\_\_iter\_\_ 메서드는 (\_\_next\_\_라는 메서드를 구현하는) iterator 객체를 반환해야한다.*

*그리고 for 루프는 StopIteration 예외가 발생할 때까지 next를 계속 호출한다.*


<br />
generator를 연결하면 매우 빠르게 실행할 수 있다.

큰 입력 스트림에서 기능을 결합할 때는 generator expression이 최선의 도구다.

## 핵심 정리
1. 리스트 컴프리헨션은 입력 값마다 메모리를 할당하기 때문에 메모리 고갈이 발생할 수 있다.
2. generator expression은 한 번에 한 출력만 하기 때문에 메모리 문제를 피할 수 있다.
3. generator expression에서 나온 iterator를 generator expression에 사용할 수 있다.
4. generator expression은 서로 연결되어 있을 때 매우 빠르게 실행된다.


