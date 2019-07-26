import random

# print()
print('test')

#input()
#test = input('아무거나 입력하세요 \n')
#print(test)
 
# Variable 변수
# 타입이 없는 것 같음, 대문자 소문자를 다 다르게 인식한다. test = 1, Test = 1 두개는 다르다.
# 숫자로 시작하면 안된다.
my_int = 1
print(my_int)
print(my_int * 10)

#Data Type
# type()
# Numeric
# 정수형, 실수형
my_float = 3.14
print(type(my_float))
print(type(my_int))
# String '' 혹은 "" 로 가능
print("Hello World")
# Boolean
my_boolean = True
print(my_boolean)

# 9. 리스트, 튜플, 딕셔너리
my_list = [1, 2, 3]
print(my_list)

my_list_name = ['1', '2', '3']
print(my_list_name)

for i in my_list_name:
    print(i)

print(random.choice(my_list))

my_list.append('test')
print(my_list)

# 튜블로 만들며 안에 있는 값을 변경할 수 없다.
my_list[0] = 'a'
print(my_list)

my_tuple = ('a', 'b', 'c')
print(my_tuple)

# 딕션어리는 key: value
my_dict = {'age':32, 'name': 'rs'}
print(my_dict)
my_dict['age'] = 30
print(my_dict)

# 10. 자료형 변환하기
print(float(my_int))
print(str(my_int))
print(type(str(my_int)))
my_str = "coding"
print(list(my_str))

# 11 주석
# 12 문자열
my_str = "김씨가족"
print(my_str)
my_str = '김씨가족'
print(my_str)
my_str = """김씨가족
토미
메타
"""
print(my_str)
my_str = '''김씨가족
토미
메타
'''
print(my_str)

# 13 문자열 포맷팅
# %d, %f, %s
my_str = 'My name is %s' % 'Jung'
print(my_str)
my_str = '%d, %d' % (3, 5)
print(my_str)
my_str = '%f, %f' % (3.2, 5.1)
print(my_str)

# 14 format()
# '{ }'.format() 

print('My name is {}'.format('Jung'))
a = 3
b = 5
c = a*b
print('{} X {} = {}'.format(a, b, c))

print('{1} X {0} = {2}'.format(a, b, c))

# 15 문자열 인덱싱

my_list_name = ['1', '2', '3']
print(my_list_name[1])
print(my_list_name[-1])
print(my_list_name[-2])
print(my_list_name[-3])

# 16 문자열 슬라이싱
my_list_name = ['1', '2', '3', '4', '5']
print(my_list_name[1:4])
print(my_list_name[2:])
print(my_list_name[:3])

# 17 문자열 메서드

my_str = 'My name, is %s' % 'Jung'
print(my_str.split(','))

# 18 독스트링 Docstring

""" 이것도 주석이다 """

# 19 end, 이스케이프 코드
print('Hello ', end='World')
# 이스케이프 코드
# \n, \t
print('Hello\tWorld\n')

# 한 줄에 여러개의 명령어가 필요할 떄는 ;를 쓴다. 근대 ;를 쓰면 기본적으로 \n이 붇는 것 같다.
print('Hello\tWorld'); print('Hello ', end='World \n')


# 20 리스트
# immutable : 값을 변경이 안됨
# mutable : 값을 변경이 가능

my_list = [1, 2, 3]
print(type(my_list))
print(my_list)


# 21 리스트 값 추가하기
# 대신에 초기화된 변수가 있어야 한다.
my_list.append(4)
print(my_list)

# 22 리스트 인덱싱, 슬라이싱
my_list = [1, 2, 3, 4]
my_list.append(5)
print(my_list)
print(my_list[4])
del my_list[4]
print(my_list)

print(my_list[0:2])
print(my_list[:2])
print(my_list[1:])

# 23 리스트 메서드
my_list = [1, 3, 2, 4, 3]
my_list.sort()
print(my_list)
print(my_list.count(3))
print(len(my_list))

# 24 튜플 
# 값을 변경할 수 없음

my_tuple = ()
print(type(my_tuple))
my_tuple = (1,2,3)
print(my_tuple)
my_tuple = 4,5,6
print(my_tuple)

# 25 패킹, 언패킹
# 패킹은 여러개의 값을 묶는 것, 언패킹은 그 반대

my_tuple = 4,5,6 # 패킹
print(my_tuple)

n1, n2, n3 = my_tuple # 언패킹
print(n1)
print(n2)
print(n3)

n1, n2 = n2, n1 # 오른쪽에서 먼저 패킹이 되고, 왼쪽으로 주입할 때 언 패킹
print(n1)
print(n2)

# 26 for
my_list_name = ['1', '2', '3']

for i in my_list_name:
    print(i)

for str in "안녕하세요":
    print(str)

# 27 range()
range(3)

print(range(3))

print(type(range(3)))

for i in range(0, 4):
    print(i)

# 28 for x 2 : 이중 for 문

for i in range(2, 4):
    for j in range(1, 10):
        print('{} X {} = {}'.format(i, j, i*j))


# 29 컴프리헨션 : comprehension (이해력)
my_list = [1,2,3,4,5,6,7,8,9,10]
odd_my_list = []
odd_my_list1 = []

for i in my_list:
    if i % 2 == 1:
        odd_my_list.append(i)
    if i % 2 == 0:
        odd_my_list1.append(i)

print(odd_my_list)
print(odd_my_list1)

print(my_list)
# 이것이 for문에서 append하는 것보다 빠르다.
# 대용량 처리에는 comprehension이 더 좋다고 함. ML에서 많이 사용
my_comprehension = [i for i in my_list if i % 2 == 1]
print(my_comprehension)

# 30 할당 연산자
# =, +=, -=, *=, /=

count = 3
count /= 3
print(int(count))

# 31 산술 연산자
# + - * /
# 특수 연산자 **(제곱), //, %
print(3 ** 2)
print(7/3)
print(7//3)
print(7%3)
 
# 32 %로 홀짝 구분하기
for i in my_list:
    if i % 2 == 1:
        print(i, "는 홀수")
    if i % 2 == 0:
        print(i, "는 짝수")

# 33 문자열 연산자
my_str = '안녕' + '하세요' + ' ' + '하이'
print(my_str)
print(my_str * 2)

# 34 비교 연산자 : Comparison
# == != <= >= < >

# 35 논리 연산자 
# and, or, not
print(True and True)
print(True or False)
print(not True)

# 36 멤버쉽 연산자 Membership 그 안에 값이 있는지 없는지 확인하는 것 
# in, not in
my_list = [1,2,3,4,5]
print(3 in my_list)
print(10 in my_list)
print(3 not in my_list)
print(10 not in my_list)

# 37 if

if 'abc' == 'abc':
    print('같음')
else:
    print('다름')

# 38 else, elif 


if 'abc' == 'abcd':
    print('다름')
elif 'abc' == 'abc':
    print('같음')
else:
    print('아무것도 아님')

# 39 while
my_val = 0
while my_val < 3:
    my_val += 1
    print(my_val)

# 40 continue, break
count = 0
while count < 10:
    count += 1
    if count < 4 :
        continue
    print('횟수 : ', count)
    if count == 8:
        break

# 41 딕셔너리 : Dictionary
# key:value
my_dict = {'age':32, 'name': 'rs'}
print(my_dict)
print(type(my_dict))
my_dict['age'] = 30
print(my_dict)
my_dict[20] = 'age'
print(my_dict)
print(my_dict['age'])
del my_dict['age']
print(my_dict)

# 42 딕셔너리 메서드
my_dict = {'age':32, 'name': 'rs'}

for i in my_dict.values():
    print(i)
for i in my_dict.keys():
    print(i)
for key, val in my_dict.items():
    print(key, val)

# 43 함수, 44 함수를 사용하는 이유
def my_func(val1, val2):
    if val1 == 'a':
        print('a 입니다.')
    if val2 == 'b':
        print('b 입니다.')
    return val1 + val2

result = my_func('a', 'b')
print(result)

# 45 여러개 return 돌려주기

def my_func1(val1, val2):
    if val1 == 'a':
        print('a 입니다.')
    if val2 == 'b':
        print('b 입니다.')
    return val1, val2

result = my_func1('a', 'b')
print(result)
result1, result2 = result
print(result1)
print(result2)

# 46 모듈 
# import

# 47 랜덤
# import random
my_list = [1, 2, 3, 4, 5, 6]

print(random.choice(my_list))
print(random.sample(my_list, 2))

# 로또 추출기
print(random.sample(range(1, 46), 6))
print(random.randint(1,10)) # 1~10 중에서 무작위로 뽑는다.

# 48 객체
# 49 코딩 스타일 : PEP8
# 50 구글링
 





