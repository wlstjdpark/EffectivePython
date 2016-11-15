#@propery를 이용하면 호출부를 변경하지 않고 한 번에 새로운 동작으로 변경이 가능하다.

from datetime import datetime
from datetime import timedelta


class Bucket(object):
    def __init__(self, period):
        self.period_delta = timedelta(seconds=period)
        self.reset_time = datetime.now()
        self.quota = 0

    def __repr__(self):
        return 'Bucket(quota=%d)' % self.quota


def fill(bucket, amount):
    now = datetime.now()
    if now - bucket.reset_time > bucket.period_delta:
        bucket.quota = 0
        bucket.reset_time = now
    bucket.quota += amount


def deduct(bucket, amount):
    now = datetime.now()
    if now - bucket.reset_time > bucket.period_delta:
        return False
    if bucket.quota - amount < 0:
        return False
    bucket.quota -= amount
    return True


bucket = Bucket(60)
fill(bucket, 100)
print(bucket)


if deduct(bucket, 99):
    print('Had 99 quota')
else:
    print('Not enough for 99 quota')
print(bucket)


if deduct(bucket, 3):
    print('Had 99 quota')
else:
    print('Not enough for 99 quota')
print(bucket)


#할당량이 소진되어서 실패인지, 할당량이 없어서인지 알 수가 없다.
#max_quota와  quota_consumed를 추가, @property를 이용하여 quota의 값이 변경될 때 업데이트하여 정보를 주자


class Bucket(object):
    def __init__(self, period):
        self.period_delta = timedelta(seconds=period)
        self.reset_time = datetime.now()
        self.max_quota = 0
        self.quota_consumed = 0

    def __repr__(self):
        return ('Bucket(max_quota=%d, quota_consumed=%d)' %
                (self.max_quota, self.quota_consumed))

    @property
    def quota(self):
        return self.max_quota - self.quota_consumed

    @quota.setter
    def quota(self, amount):
        delta = self.max_quota - amount
        if amount == 0:
            # 새 기간의 할당량을 리셋함
            self.quota_consumed = 0
            self.max_quota = 0
        elif delta < 0:
            # 새 기간의 할당량을 채움
            assert self.quota_consumed == 0
            self.max_quota = amount
        else:
            # 기간 동안 할당량을 소비함
            assert self.max_quota >= self.quota_consumed
            self.quota_consumed += delta


bucket = Bucket(60)
print('Initial', bucket)
fill(bucket, 100)
print('Filled', bucket)

if deduct(bucket, 99):
    print('Had 99 quota')
else:
    print('Not enough for 99 quota')
print('Now', bucket)

if deduct(bucket, 3):
    print('Had 99 quota')
else:
    print('Not enough for 99 quota')
print('Still', bucket)


#사용처에서 Bucket.quota를 사용하는 코드를 변경하거나 Bucket에 대해 알 필요가 없다.
#max_quota, quota_consumed에 직접 접근이 가능하나 @property는 확장성이 좋다.

#@property를 과용하지말자. 만약 @property 메서드가 계속 확장되고 있다면 리팩토링할 시점이다.




