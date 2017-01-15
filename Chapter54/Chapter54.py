
'''
Chapter 54. 배포 환경을 구성하는 데는 모듈 스코프 코드를 고려하자

배포 환경
개발 환경
제품 환경

제품 실행 환경에 따라 다른 환경을 셋팅하려면 ConfigParser (configparser로 변경됨)을 사용하자.
'''
import configparser
config = configparser.ConfigParser()
config.read('config.conf')

section = 'REAL'

if config.getboolean(section, 'TESTING'):
    print('TESTING is True')
else:
    print('TESTING is False')

print(config.get(section, 'id'))

# 현재 플랫폼에 따라 다르게 동작할 땐..
import sys
print(sys.platform)