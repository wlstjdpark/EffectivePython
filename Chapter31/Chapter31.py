from weakref import WeakKeyDictionary


class Homework(object):
    def __init__(self):
        self._grade = 0

    @property
    def grade(self):
        return self._grade

    @grade.setter
    def grade(self, value):
        if not (0 <= value <= 100):
            raise ValueError('Grade must be between 0 and 100')
        self._grade = value


galileo = Homework()
galileo.grade = 95




class Exam(object):
    def __init__(self):
        self._writing_grade = 0
        self._math_grade = 0

    @staticmethod
    def _check_grade(value):
        if not (0 <= value <= 100):
            raise ValueError('Grade must be between 0 and 100')

    @property
    def writing_grade(self):
        return self._writing_grade

    @writing_grade.setter
    def writing_grade(self, value):
        self._check_grade(value)
        self._writing_grade = value

    @property
    def math_grade(self):
        return self._math_grade

    @math_grade.setter
    def math_grade(self, value):
        self._check_grade(value)
        self._math_grade = 0


# 같은 일을 하는 @property 중복 코드가 많다

# 디스크립터를 사용하여 한 클래스의 서로 다른 속성에 같은 로직을 재사용할 수 있다.
# 디스크립터 프로토콜 (descriptor protocol) 은 속성에 대한 접근을 언어에서 해석할 방법을 정의한다

'''
class Grade(object):
    def __get__(*args, **kwargs):
        # ...

    def __set__(*args, **kwargs):
        # ...
'''


class Grade(object):
    def __init__(self):
        self._value = 0

    def __get__(self, instance, owner):
        return self._value

    def __set__(self, instance, value):
        if not (0 <= value <= 100):
            raise ValueError('Grade must be between 0 and 100')
        self._value = value


class Exam(object):
    writing_grade = Grade()
    math_grade = Grade()
    science_grade = Grade()

first_exam = Exam()
first_exam.writing_grade = 5
first_exam.science_grade = 99
print('Writing', first_exam.writing_grade)
print('Science', first_exam.science_grade)

second_exam = Exam()
second_exam.writing_grade = 75
print('Second', second_exam.writing_grade, 'is right')
print('First', first_exam.writing_grade, 'is wrong')


# 문제는 속성에 대응하는 Grade 인스턴스는 프로그램에서
# Exam 인스턴스를 생성할 때마다 생생되는 게 아니라
# Exam 클래스를 처음 정의할 때 한 번만 생성 된다.


# 해결을 위해 딕셔너리 각 인스턴스의 상태를 저장해보자

class Grade(object):
    def __init__(self):
        self._values = {}

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return self._values.get(instance, 0)


    def __set__(self, instance, value):
        if not (0 <= value <= 100):
            raise ValueError('Grade must be between 0 and 100')
        self._values[instance] = value


# 여전히 이 클래스는 메모리 누수라는 문제가 있다
# 딕셔너리에는 모든 인스턴스의 참조가 있고 참조 개수가 절대로 0이 되지 않아 가비지 컬렉터가 정리를 못한다


# 파이썬 내장 모듈 weakref를 사용하여 이를 해결해보자
# 딕셔너리 대신에 WeakKeyDictionary를 사용하자.
# WeakKeyDictionary는 런타임에 마지막 남은 Exam 인스턴스의 참조를 갖고 있다는 사실을 알면 키 집합에서 Exam 인스턴스를 제거하한다.
# 파이썬에서 대신 참조를 관리해주고 모든 Exam 인스턴스가 사용되지 않으면 _values가 비어 있게 한다


class Grade(object):
    def __init__(self):
        self._values = WeakKeyDictionary()

    # ...

    def __get__(self, instance, instance_type):
        if instance is None:
            return self
        return self._values.get(instance, 0)

    def __set__(self, instance, value):
        if not (0 <= value <= 100):
            raise ValueError('Grade must be between 0 and 100')
        self._values[instance] = value


class Exam(object):
    writing_grade = Grade()
    math_grade = Grade()
    science_grade = Grade()


first_exam = Exam()
first_exam.writing_grade = 82
second_exam = Exam()
second_exam.writing_grade = 75
print('First ', first_exam.writing_grade, 'is right')
print('Second ', second_exam.writing_grade, 'is right')


exam = Exam()
exam.writing_grade = 40
print(exam.writing_grade)

Exam.__dict__['writing_grade'].__set__(exam, 40)
Exam.__dict__['writing_grade'].__get__(exam, Exam)



# ...