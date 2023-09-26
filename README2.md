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


## 230915 

### 휴강이라 알고리즘 문제 1개 풀기


알고리즘 문제
from https://pyalgo.co.kr/
Q1. 자격증명 

+,-, 공백으로 이루어진 문자열 -> 이진수 -> 아스키코드와 매치 -> 문자열

아스키코드를 문자로 만들려면 chr() 함수

![통과](https://github.com/darvish0210/Ormi_3rd/assets/142385778/6361b901-462c-4f94-8f69-787d590c217a)




## 230918
민방위 훈련이라 조퇴함
### python 기초강의

#### 클래스 변수와 인스턴스 변수

global이 선언되지 않으면, 'def'에서는 전역변수 자체를 건드릴 수 없다.

#### 상속

이름이 같은 자식의 메소드로, 부모의 메소드를 '덮어' 버리는것이 오버라이딩


## 230919

### python 기초강의

#### 클래스 메소드와 스태틱 메소드

클래스 메서드는 클래스 상태를 변경하는데 사용
스태틱 메소드를 쓰는 이유? - 인스턴스 생성 없이 호출이 가능

#### 덕타이핑이란?

실제 타입이 아닌, 구현된 메소드로 객체의 타입을 결정?
오리처럼 행동하면 오리로 봐도 무방?



파이썬에는 변수 숨기는 것이 가능하지 않다!
비공개 속성이 조작 불가능한게 아닙니다!

#### 모듈, 패키지

모듈은 라이브러리.py
모듈이 모인 폴더가 패키지

#### 예외처리와 에러

예외처리는 try except finally 방식이 좋다
assert는 가정 설정문 
raise로 에러를 바로 일으킬 수 있다.

## 230920

### python 기초강의

#### 일급함수와 고차함수

일급함수: 함수를 다른 객체와 동일하게 취급 => 값, 주소로 취급
고차함수: 함수를 아규먼트로 받거나, 리턴으로 반환하는 함수

#### 고차함수 -> 클로저와 데코레이터

클로저: 휘발되었어야 하는 메모리 영역에 접근하여 함수나 데이터를 활용하는 일

데코레이터: 함수 또는 메소드를 꾸며주는 함수

#### 이터레이터 와 제네레이터

이터레이터: 값을 차례대로 꺼낼 수 있는 객체
iter 와 next 메소드가 정의되어야 한다

제네레이터: 이터레이터를 생성해주는 함수
yield 키워드를 쓴다.



## 230921

### python 기초강의

#### f-string 방식(3.6버전부터)

```python
something = '볼펜'
EA = 2
one_length = 5.343
scale = 'cm'

print(f'{something} {EA}개의 길이는 {one_length*EA}{scale} 입니다.')
```

```python
# 중괄호가 2개씩 증가할 때마다 출력은 1개씩 증가
value = 'hello'
print(f'{value}') # 중괄호 X
print(f'{{value}}') # 중괄호 1
print(f'{{{value}}}') # 중괄호 1
print(f'{{{{value}}}}') # 중괄호 2
print(f'{{{{{value}}}}}') # 중괄호 2
print(f'{{{{{{value}}}}}}') # 중괄호 3

```
3개라고 반올림해서 2개? 가 되지는 않음





#### 파일 다루기

```python
f = open('python.csv', 'w')
s = '''제목,평점,이미지,줄거리
무빙,5.0,img,줄거리
무빙,5.0,img,줄거리
무빙,5.0,img,줄거리
'''
f.write(s)
f.close()
```
w 쓰기, r 읽기, a 추가(append) = 수정이 가능한게 아니라 말 그대로 추가만 가능





## 230922

### python 기초강의


#### 정규표현식


대소문자를 구분함
^hello는 처음에 나오는 hello
hello$는 마지막에 나오는 hello
h.llo는 .자리가 any character

 _* : 앞에 있는 문자가 0개 ~ N개
 _+ : 앞에 있는 문자가 1개 ~ N개
 _? : 앞에 있는 문자가 0개 ~ 1개

/\w/gm : 워드
/\w{5} /gm : 5개의 글자와 스페이스 하나
/\W/gm : not 워드
/\d/gm : 숫자
/\D/gm : not 숫자
/\s/gm : 스페이스
/\S/gm : not 스페이스



#### 크롤링

##### 크롤링은 늘 조심할것! 비영리적이어도 불법의 여지 있음!

http 포트 80
https 포트 443 (http + security)


연습용 사이트 크롤링
```python
import requests
from bs4 import BeautifulSoup

response = requests.get('http://www.paullab.co.kr/stock.html')

response.encoding = 'utf-8'
html = response.text

soup = BeautifulSoup(html, 'html.parser')

#2019.10.23 거래량 출력하기

soup.select('.table>tbody>tr')[1].select('td')[6].text
```





## 230922

### python 기초강의

오전 회고


#### 자료구조 - 스택

스택은 나중에 들어온 data가 먼저 나간다

LIFO Last in First out 후입선출




연습문제 https://pyalgo.co.kr/?page=6#

231004 오전 파이썬 시험예정 - 2시간, 50점 만점, 총 15문제


## 230922

### python 기초강의

#### 자료구조 - 큐

큐는 먼저 들어온 data가 먼저 나간다

FIFO First in First out 선입선출

#### 연결 리스트

Node로 이루어진 리스트

Node에는 data와 다음 Node를 가리키는 next만 존재

왜 쓰는가?

성능이 기본적인 리스트와 비교하면, 훨씬 빠르기 때문

다른 자료구조를 만드는데 이걸로 밑바탕을 한다

#### 트리

하나의 Root Node를 지니고, 그 아래로 자식 Node들을 지닐 수 있는, 순환하지 않는 그래프 자료구조

