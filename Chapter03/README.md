bytes, str, unicode의 차이점을 알자
============
<br />
파이썬3에서 byte는 8비트, str은 유니코드 문자를 사용한다.

파이썬2에서 str과 unicode 두 가지 타입으로 문자 시퀀스를 나타낸다.
str은 8비트, unicode 는 유니코드 문자를 저장한다.

<br />
유니코드 문자를 바이너리 데이터로 표현하는 방법은 많은데, 가장 일반적인 인코딩은 utf-8이다.

파이썬 프로그래밍에서 제공할 인터페이스에서는 유니코드를 인코드하고 디코드 해야한다.

문자 타입이 분리되어 있기 때문에 파이썬에서는 byte와 유니코드를 변환하는 헬퍼 함수가 필요하다.

```py
def to_str(bytes_or_str):
    if isinstance(bytes_or_str, bytes):
        value = bytes_or_str.decode('utf-8')
    else:
        value = bytes_or_str
    return value  # str 인스턴스
```

```py
def to_bytes(bytes_or_str):
    if isinstance(bytes_or_str, str):
        value = bytes_or_str.encode('utf-8')
    else:
        value = bytes_or_str
    return value  # bytes 인스턴스
```

<br />
파이썬2에서 str이 7비트 아스키 문자만 포함하고 있다면 unicode와 str 인스턴스가 같은 타입처럼 보인다.

파이썬3에서 내장 함수 open이 반환하는 파일 핸들을 사용하는 연산은 기본으로 utf-8을 사용한다.

파이썬2는 바이너리 인코딩을 사용한다.

이 때문에 파이썬3에서는 바이너리 파일을 오픈할 때는 ('wb')와 같은 모드로 오픈해야한다.

<br />
## 핵심 정리
- 파이썬3에서 byte는 8비트 값을 저장, str은 유니코드 문자를 저장한다.
- 파이썬2에서는 str은 8비트, unicode는 유니코드 문자를 저장한다.
- 파이썬2에서 str이 7비트 아스키 문자만 포함하고있다면 유니코드와 함께 사용할 수 있다.
- 헬퍼 함수를 통해서 원하는 문자 코드로 변환할 필요가 있다.
- 바이너리 파일을 읽거나 쓸 때는 바이너리 모드 ('rb 혹은 'wb')로 오픈한다.
