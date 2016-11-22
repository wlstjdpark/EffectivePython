# 메타클래스와 속성
# 메타클래스를 이용하면 파이썬 class 문을 가로채서 클래스가 정의될 때마다 특별한 동작을 제공할 수 있다.
# 속성 접근을 동적으로 사용자화하는 파이썬의 내장 기능이 있다.
# 동적 속성을 오버라이드 하다가 예상치 못한 부작용을 일으킬 수 있고,
# 메타클래스는 내부적으로 동작하는게 많기 때문에 최소한으로 사용하는 것이 좋다.

# 게터와 세터 메서드 대신에 일반 속성을 사용하자.


class OldResistor(object):
    def __init__(self, ohms):
        self._ohms = ohms

    def get_ohms(self):
        return self._ohms

    def set_ohms(self, ohms):
        self._ohms = ohms

print('OldResister')
r0 = OldResistor(3)
print('Before: %5r' % r0.get_ohms())
r0.set_ohms(10)
print('After:  %5r' % r0.get_ohms())
# 아래와 같이 사용하기엔 불편하다.
r0.set_ohms(r0.get_ohms() + 10)


# 아래와 같이 속성을 사용하면 편하다.
class Resistor(object):
    def __init__(self, ohms):
        self.ohms = ohms
        self.voltage = 0
        self.current = 0

print('Resister')
r1 = Resistor(3)
print('Before: %5r' % r1.ohms)
r1.ohms = 20
print('After:  %5r' % r1.ohms)
# 속성을 이용하여 += 연산도 쉽게 사용
r1.ohms += 20
print('After adding: %5r' % r1.ohms)


# 상위 클래스의 속성에 대해 property를 제공하고 하위 클래스에서 _voltage 속성을 사용한다.
class VoltageResistance(Resistor):
    def __init__(self, ohms):
        super().__init__(ohms)
        self._voltage = 3

    @property
    def voltage(self):
        return self._voltage

    @voltage.setter
    def voltage(self, voltage):
        self._voltage = voltage
        self.current = self._voltage / self.ohms

# 속성을 @property로 사용하여 원하는 동작을 할 수 있다. (current 자동 셋팅)
print('VoltageResistance')
r2 = VoltageResistance(3)
print('Before: %5r amps' % r2.current)
r2.voltage = 10
print('After: %5r amps' % r2.current)


# property의 setter를 이용하여 범위 체크도 가능하다.
class BoundedResistance(Resistor):
    def __init__(self, ohms):
        super().__init__(ohms)

    @property
    def ohms(self):
        return self._ohms

    @ohms.setter
    def ohms(self, ohms):
        if ohms <= 0:
            raise ValueError('%f ohms must be > 0' % ohms)
        self._ohms = ohms

r3 = BoundedResistance(3)
#r3.ohms = 0

# 생성자에도 잘못된 값이 오는 순간 바로 캐치가 가능하다.
#r3 = BoundedResistance(-3)
# super().__init__(ohms) -> self.ohms = ohms -> ohms.setter 호출

#property setter 속성을 사용하여 omhs 속성에 대해 immutable 설정이 가능하다.
class FixedResistance(Resistor):
    def __init__(self, ohms):
        super().__init__(ohms)

    @property
    def ohms(self):
        return self._ohms

    @ohms.setter
    def ohms(self, ohms):
        if hasattr(self, '_ohms'):
            raise AttributeError("Can't set attribute")
        self._ohms = ohms

r4 = FixedResistance(3)
#r4.ohms = 3


# property에서 다른 속성의 값을 변경하는 것은 사용자 입장에서 의도하지 않는 일이라 볼 수도 있다.
class MysteriousResistor(Resistor):
    def __init__(self, ohms):
        super().__init__(ohms)

    @property
    def ohms(self):
        self.voltage = self._ohms * self.current
        return self._ohms

    @ohms.setter
    def ohms(self, ohms):
        self._ohms = ohms;

print('MysteriousResistor')
r7 = MysteriousResistor(20)
r7.current = 0.01
print('Before: %5r' % r7.voltage)
r7.ohms
print('After:  %5r' % r7.voltage)



# 객체의 상태를 수정하는 일은 setter에서 수행하자.
# 모듈을 동적으로 임포트하거나, 느린 헬퍼 함수를 실행하거나, 비용이 많이 드는 작업처럼
# 호출부에서 에측하지 못할만한 부작용은 피하자.
# 느리거나 복잡한 작업은 메서드가 하도록하자.
