# Ormi_3rd

-오르미 3기 학습 내용

## 230908

### python 기초 강의

파이썬의 장점
- 1. Python-Django 는 Java-Spring에 비해 빠르게 MVP까지 올릴 수 있다.
- 2. 속도
- 3. 부하분산
- 4. 스케일업 - 요기요 Django

#### 입출력, 변수, 자료형(정수,실수,문자열)

중점사항
함수의 주석은 보통 함수 선언문 내부에 단다.

변수는 포스트잇이다! 다른 언어와 다르다.
변수 표기법은 보통 스네이크식. (ex: col_num, row_num)

새로운 자료형을 만났을 땐 print(type(x))와 print(dir(x))를 해보자

실수 자료형엔 무한대? 가 있다. float('inf')

복소수에서 보통 쓰는 i는 여기선 j를 쓴다. 3+4j

문자열 메소드는 기억해두면 좋다, 알고리즘 문제에서도 많이 쓰인다 zfill등

알고리즘 문제를 풀땐 입출력을 먼저 보면 좋다

수업시간에 연습문제로 카카오 코딩테스트를 부분적으로 풀어봄
https://school.programmers.co.kr/learn/courses/30/lessons/17681?language=python3
https://school.programmers.co.kr/learn/courses/30/lessons/72410



## 230911


### python 기초 강의

#### 논리자료형

True, False, None이 있으며 True는 1, False는 0과 같이 취급된다.

None을 확인할때는 == 보다는 is 로 확인하는것이 좋다.
is 는 id값을 기준으로 판단한다.

#### 메소드 체이닝

STR.Foo().Foo2().Foo3() 식으로 이어나가기

#### 형변환

float에서 str은 되지만, 그것을 바로 int로 할 수는 없다('.' 때문)

#### 연산과 구문

'-'가 여러개 붙어도 연산이 된다? '--' 는 '+' 취급?
python에서 '//' 는 몫이 아니다! '나눈 수의 내림' 이다. (음수연산에서 확인가능)

#### 단락회로평가

A or B 혹은 A and B 일때, A만으로 True, 혹은 False의 판별이 날 경우 A 뒤로는 쳐다도 보지 않는다.

## 230912

### python 기초 강의

#### 함수

기본값을 주려 할땐 없는 것을 앞에 두기
```python

def f(a=10, b=20, c): # c만 default value를 안주게 되면 error, 순서대로 안주어야 합니다.
    print(a, b, c)

# f() # error
# f(100, 10) # error
# f(a=100, b=200, c=300) # error
# f(c=300, a=100, b=200) # error
# f(c=300) # error

def f(a=10, b=20, c): # 이 코드는 가능하지 않습니다.
    print(a, b, c)

def f(a, b=20, c=30): # 이 코드는 가능합니다.
    print(a, b, c)

```
함수도 변수처럼 취급하기

```python
# a와 b를 더한 값과 a와 b를 뺀 값을 곱하는 함수 만들기

a,b = 2,3
#maybe....
def mul(a=0,b=0):
    return a*b
def sum(a=0,b=0):
    return a+b
def subs(a=0,b=0):
    return a-b

mul(sum(a,b),subs(a,b))
```

어지간하면 재귀함수 보다는 반복문을 쓰자. 무한 반복위험

람다 스타일은 재사용안할 것? 에는 편하게 한번쓰고 마는 느낌

## 230913

### python 기초강의

#### 리스트
x = [1,2,3]

리스트는 시퀀스 형 자료형

reversed()와 reverse(), sorted()와 sort()의 차이 : ed가 붙은 애들은 원본을 건들지 않음

#### 튜플

x = (1,2,3)
튜플은 참조 불변이다.

불변이라 그런지 리스트 보다 처리 속도가 좀 더 빠르다

#### 딕셔너리

x = {'b':1, 'c':2}
이제 삽입 순서가 보장된다. (과거엔 보장되지 않았음)

#### 집합
x = {1,2,3}
중복이 허용되지 않으며 순서가 없다
연산은 교집합, 차집합, 합집합으로 한다.

#### 리스트 컴프리헨션

```python
l = [i for i in range(10)]

```

간단하게 반복문을 만들때 사용(안의 for나 if가 2회 초과일때는 사용이 권장되지 않음)

## 230914

### python 기초강의

#### 조건문

if에 붙는 조건도 '단락평가' 를 거친다. (앞부분만 보고 생략하기 가능?)

if, elif, else는 다른 시선으로 보면 긴 if의 조건을 풀어쓴 느낌
```
if (A and B and C and ...)

if A:
    elif B:
        elif C:
            ...

```
이렇게 전환할 때는 꼭 순서를 맞춰서!


match는 switch 같은 기능 (최근에 추가됨)

#### 반복문

파이썬에서 for 문은 언제나 in과 함께 다닌다

while True: 스타일의 무한반복은 OS나 쉘 등에서 사용한다

#### 클래스

클래스는 설계 도면 or 공장이다

생산방식은 

인스턴스 = 클래스()
