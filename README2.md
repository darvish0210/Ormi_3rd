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





## 230925

### python 기초강의

오전 회고


#### 자료구조 - 스택

스택은 나중에 들어온 data가 먼저 나간다

LIFO Last in First out 후입선출




연습문제 https://pyalgo.co.kr/?page=6#

231004 오전 파이썬 시험예정 - 2시간, 50점 만점, 총 15문제


## 230926

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

## 230927

### python 기초강의

#### 정렬

정렬 알고리즘 3대장 비교(Bset, Worst)
* 병합 정렬 : nlogn, nlogn
* 퀵 정렬 : nlogn, n**2
* 팀소트 : n, nlogn

선택정렬 : 하나씩 선택 해서 ans에 넣기
삽입정렬 : 순서대로 넣어가기 (나보다 크면 그 앞에 들어가자)

병합정렬 : divide and Conquer
퀵정렬 : 피봇을 정하고 그 기준으로 정렬

#### 페이지 교체 

FIFO : 순서대로 교체
LRU : Hit가 가장 오랫동안 맞지 않은 것 먼저 교체




## 231002

### python 문제풀이 복습

https://pyalgo.co.kr/?page=2 암호문 - 정규표현식 사용
https://pyalgo.co.kr/?page=3 인원선발 - 정렬

## 231003

### python 문제풀이 복습

https://pyalgo.co.kr/?page=4 꿈의설계 - 정규표현식 사용
그런데 어째서인지 통과가 안된다? 질문해봐야할거같음 (에러a)만 표시됨


## 231004

### python test
외부유출 금지! 

### Django
Django의 장점은?
배포가 쉽다!
단점은 아마도 속도?

MVT 패턴 = Model Template View
Model : 데이터베이스와 상호작용
Template: 사용자에게 보여지는 HTML,CSS,JS등
View: HTTP 요청 처리 및 모델과 템플릿 연결

Django는 가상환경에서 실행하자. -> 라이브러리 버전 관리등의 이점.

가상환경 생성 및 프로젝트 생성 연습



## 231004

### Django

```
# urls 기획
1. (어제 과제) 다음 url이 작동하도록 해주세요.
1.1 ''
1.2 'about/'
1.3 'contact/'
1.4 'accounts/login'
1.5 'accounts/logout'
1.6 'blog/'
1.7 'blog/1'
1.8 'blog/2'
1.9 'blog/3'


앱이름: main	views 함수이름	html 파일이름	비고
''		index		index.html
'about/'		about
'contact/'		contact

앱이름: accounts	views 함수이름	html 파일이름	비고
'accounts/'	404
'accounts/login'	login		login.html
'accounts/logout'	logout		logout.html
'accounts/<str:s>'	404				login, logout을 제외하고 404로

앱이름: blog	views 함수이름	html 파일이름	비고
'blog/'		blog		blog.html
'blog/<int:pk>'	post		post.html		게시물이 없을 경우에는 404로 연결
```

```python
# main > urls.py
from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
]

# blog > urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog, name='blog'),  # 실제로는 blog/
    path('<int:pk>/', views.post, name='post'), # 실제로는 blog/1, blog/2, blog/3...
]
# accounts > urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name='login'), # accounts/login
    path('logout/', views.logout, name='logout'), # accounts/logout
]

#blog > views.py

from django.shortcuts import render

def blog(request):
    # db = Cafe.objects.all()를 하면 아래와 같이 값을 가져오게 됩니다.
    db = {
        1: {
            'title': '제목 1', 
            'contents': 'Post 1 body', 
            'img': 'https://picsum.photos/200/300'
            },
        2: {
            'title': '제목 2', 
            'contents': 'Post 2 body', 
            'img': 'https://picsum.photos/200/300'
            },
        3: {
            'title': '제목 3', 
            'contents': 'Post 3 body', 
            'img': 'https://picsum.photos/200/300'
            },
    }
    return render(request, 'blog/blog.html', {'db': db})

def post(request, pk):
    # db = Cafe.objects.get(pk=pk)
    return render(request, 'blog/post.html')

def bookinfo(request):
    '''
    교육용 크롤링 페이지입니다.
    '''
    return render(request, 'blog/bookinfo.html')
```
name으로 관리하는이유? name을 안쓸 시 혹시 도메인이 바뀌면 일일히 h태그가서 바꿔야 한다.


템플릿

변수 사용 ->중괄호 두개씀
html 내에서 파이썬 문법 사용시 중괄호 한개와 퍼센트{%%}

for문,if문 사용시엔 {% endfor %}{% endif %}로 마무리



## 231005

### git 기초강의

https://paullabworkspace.notion.site/GitHub-435ec8074bcf4353afb947f601a030df

- git 과 github의 차이는??

git 은 분산버전 관리 시스템

github는 git을 관리해주는 웹 서비스

왜 git이 쓸까? - 버전관리에 굉장히 편리하다 = 형상 관리

```
파일의 상태에 따라 **Untracked 와 Tracked 로 분류

1) **Untracked**(관리 대상이 아님) : 파일 생성 후 한번도 `git add`하지 않은 상태를 말합니다.

2) **Tracked**(관리 대상임) : git이 관리하는 파일임을 의미합니다.

- `Unmodified` : 최근의 커밋과 비교했을 때 바뀐 내용이 없는 상태
- `Modified` : 최근 커밋과 비교했을 때 바뀐 내용이 있는 상태
- `Staged` : 파일이 수정되고 나서 스테이지 공간에 올라와 있는 상태이며, `git add` 후의 상태
```

add : git이 관리할 대상으로 파일을 등록
commit : Staged 된 상태를 등록
push : 원격저장소로 업로드
pull : 원격저장소의 이력을 받아옴


etc)면접용 참고사이트
https://github.com/JaeYeopHan/Interview_Question_for_Beginner
https://github.com/gyoogle/tech-interview-for-developer
https://github.com/ksundong/backend-interview-question#CS-%EA%B4%80%EB%A0%A8-%EC%A7%80%EC%8B%9D
https://github.com/4z7l/tech_interview.zip

## 231010

### Django

#### bootstrap

부트스트랩은 무엇? : 웹사이트를 쉽게 만들 수 있게 도와주는 오픈소스 프레임워크. 
장점은? : 반응형 웹페이지 구현에 쓰기 편하다.

예시

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.0/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body>
    <div id="carouselExampleControls" class="carousel slide" data-bs-ride="carousel">
        <div class="carousel-inner">
          <div class="carousel-item active">
            <img src="jeju.jpg" class="d-block w-100" alt="...">
          </div>
          <div class="carousel-item">
            <img src="jeju.jpg" class="d-block w-100" alt="...">
          </div>
          <div class="carousel-item">
            <img src="jeju.jpg" class="d-block w-100" alt="...">
          </div>
        </div>
        <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleControls" data-bs-slide="prev">
          <span class="carousel-control-prev-icon" aria-hidden="true"></span>
          <span class="visually-hidden">Previous</span>
        </button>
        <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleControls" data-bs-slide="next">
          <span class="carousel-control-next-icon" aria-hidden="true"></span>
          <span class="visually-hidden">Next</span>
        </button>
      </div>
    <div class="container">
        <div class="row">
            <div class="col-md-4">
                <div class="card" style="width: 100%">
                    <img src="jeju.jpg" class="card-img-top" alt="...">
                    <div class="card-body">
                      <h5 class="card-title">Card title</h5>
                      <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
                      <a href="#" class="btn btn-primary">Go somewhere</a>
                    </div>
                  </div>
            </div>
            <div class="col-md-4">
                <div class="card" style="width: 100%">
                    <img src="jeju.jpg" class="card-img-top" alt="...">
                    <div class="card-body">
                      <h5 class="card-title">Card title</h5>
                      <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
                      <a href="#" class="btn btn-primary">Go somewhere</a>
                    </div>
                  </div>
            </div>
            <div class="col-md-4">
                <div class="card" style="width: 100%">
                    <img src="jeju.jpg" class="card-img-top" alt="...">
                    <div class="card-body">
                      <h5 class="card-title">Card title</h5>
                      <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
                      <a href="#" class="btn btn-primary">Go somewhere</a>
                    </div>
                  </div>
            </div>
            <div class="col-md-4">
                <div class="card" style="width: 100%">
                    <img src="jeju.jpg" class="card-img-top" alt="...">
                    <div class="card-body">
                      <h5 class="card-title">Card title</h5>
                      <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
                      <a href="#" class="btn btn-primary">Go somewhere</a>
                    </div>
                  </div>
            </div>
            <div class="col-md-4">
                <div class="card" style="width: 100%">
                    <img src="jeju.jpg" class="card-img-top" alt="...">
                    <div class="card-body">
                      <h5 class="card-title">Card title</h5>
                      <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
                      <a href="#" class="btn btn-primary">Go somewhere</a>
                    </div>
                  </div>
            </div>
            <div class="col-md-4">
                <div class="card" style="width: 100%">
                    <img src="jeju.jpg" class="card-img-top" alt="...">
                    <div class="card-body">
                      <h5 class="card-title">Card title</h5>
                      <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
                      <a href="#" class="btn btn-primary">Go somewhere</a>
                    </div>
                  </div>
            </div>
        </div>
    </div>
    
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.0/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>
```


## 231011

### Django

가상환경 django 연습하기 - 이미지 삽입

pillow : 이미지 관련 라이브러리

```python
class Post(models.Model):
    title = models.CharField(max_length=100)
    contents = models.TextField()
    # main_image = models.ImageField(upload_to='blog/', blank=True, null=True) # upload_to='blog/' : blog 폴더 안에 저장
    main_image = models.ImageField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

```
* blank=True는 '이 필드는 필수가 아니다'라는 내용입니다.
* null=True는 '이 필드는 새로 생성되어도 DB 비어있어도 된다.'

이미지는 그냥 넣으면 보이지 않는다?
static 선언으로 경로지정을 해줘야함

연습문제는 검색과 삭제가 들어간 버전

## 231012

### Django

crud 연습

CREATE,READ,UPDATE,DELETE

{% csrf_token %} : Django의 기본적인 CSRF 방지 메커니즘은 CSRF 토큰을 쿠키(세션이 아니라)에 저장하는 방식
브라우저의 기본적인 보안 정책에 따르면, JavaScript를 이용하여 다른 도메인의 쿠키를 설정하는 것은 불가능
다른 프레임워크에서는 세션에 저장한다고 한다.

- CSRF란? 
권한을 가진 사용자가 의도와 무관하게 공격?을 하게 유도하는 해킹기법



## 231012

### 특강

이스트소프트 테크센터장 변형진님

주제 : 딥러닝 언어모델 이해와 활용

RNN: Recurrent Neural Network = 순환 신경망

Backpropagation : 역전파
- 원하는 target과 output의 차이를 구한 뒤, 그 오차값을 뒤로 전파해가면서 변수들을 갱신


## 231016

오전 회고 

장애복구의 핵심은 서비스의 정상화
빠른복구 => 피해 최소화
롤백, 핫픽스, 장비증설, 장비교체
스케일 아웃: 서버를 여러대 추가
스케일 업: 서버에 CPU나 RAM 등을 추가하거나 고성능의 부품, 서버로 교환

### Django

gitignore.io -> django 입력시 기본적인 ignore 리스트 싹 나옴

이제부터 클래스기반 뷰로 시작. 여태까지는 함수형 뷰

requirements.txt로 설치하기 : pip install -r requirements.txt

#############################################################
```html
Django에서 ListView와 같은 일반적인 Class-Based Views (CBV)를 사용할 때, 템플릿 이름은 기본적으로 다음과 같은 규칙을 따라 자동으로 생성됩니다

PostList (ListView)
템플릿 이름 규칙: <app_name>/<model_name_소문자>_list.html
여기서의 기본 템플릿: <app_name>/post_list.html
템플릿 접근 방법:
{% for post in object_list %}
    {{ post.title }}
{% endfor %}


PostDetail (DetailView)
템플릿 이름 규칙: <app_name>/<model_name_소문자>_detail.html
여기서의 기본 템플릿: <app_name>/post_detail.html
템플릿 접근 방법: 
{{ object.title }}


PostCreate (CreateView)
템플릿 이름 규칙: <app_name>/<model_name_소문자>_form.html
여기서의 기본 템플릿: <app_name>/post_form.html
템플릿 접근 방법:
<form method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Create</button>
</form>


PostUpdate (UpdateView)
템플릿 이름 규칙: <app_name>/<model_name_소문자>_form.html
여기서의 기본 템플릿: <app_name>/post_form.html
템플릿 접근 방법:
<form method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Update</button>
</form>


PostDelete (DeleteView)
템플릿 이름 규칙:  <app_name>/<model_name_소문자>_confirm_delete.html
여기서의 기본 템플릿: <app_name>/post_confirm_delete.html
템플릿 접근 방법:
<form method="post">
    {% csrf_token %}
    Are you sure you want to delete "{{ object.title }}"?
    <button type="submit">Delete</button>
</form>


* CreateView와 UpdateView는 같은 템플릿 이름 규칙을 사용합니다. 그래서 둘 다 _form.html을 기본으로 사용합니다.


view 리스트
Base views
View
TemplateView
RedirectView
Generic display views
DetailView
ListView
Generic editing views
FormView
CreateView
UpdateView
DeleteView
Generic date views
ArchiveIndexView
YearArchiveView
MonthArchiveView
WeekArchiveView
DayArchiveView
TodayArchiveView
DateDetailView


```
########################################################

## 231017

### Django

댓글 생성,태그 생성,연결, 지우기 실습


한 게시글에는 댓글이 0개 달릴수 있고, 여러개 달릴수도 있지만,글 없이는 댓글이 있을 수 없다 -> 1:N 관계

다만 운영정책? 등에 따라서 글이 삭제, 차단 된 경우에는 댓글을 자동 삭제하는 것이 아닌 보관 해야 할 수도?

https://www.notion.so/Model-RDB-ERD-1-N-N-M-1-1-f34426c3b50c49c1adcda1a652dfa2c1

RDB : relational DB
ERD : Entity Relation Diagram


## 231018

### Django

admin 사이트 커스터마이징

모놀리식 : 템플릿 문법 써서 사용자에게 html,css,js코드를 주는 방법
API 명세표가 따로 필요 없다. 렌더링은 Server에서 다 함.

- 장점 : 규모가 있지 않은 서비스의 경우 빠른 개발 가능, 소규모 팀인 경우 선택하기 좋다.
- 단점 : 규모가 커질 경우 BE, FE에 역할이 혼재됨.


마이크로식(django서버, fe서버가 별도로 운영)
 - 장점 : 서버엔지니어와 프론트엔드 개발자는 API 명세서로 소통하면 됨.
 - 단점 : 소규모 프로젝트에서는 비용이 Too much.


## 231019

### Django

DRF란? : Django REST Framework

Django 안에서 RESTful API 서버를 쉽게 구축할 수 있도록 도와주는 오픈소스 라이브러리

Serializer : 직렬화? 

Serializer는 클라이언트와 서버 간에 데이터를 주고 받을 때 복잡한 데이터 구조를 쉽게 변환하고 검증하는 역할을 수행합니다.

직렬화 : 추상적인 object를 구체적이고, 저장가능하고, 전송가능한 텍스트파일 (연속된 byte파일 = stream of bytes)로 바꿔주는 것

역직렬화 : 직렬화의 reverse

그럼 직렬화가 필요한 이유는?
Django 내부의 데이터를 json이나 xml등으로 변환시켜서 보내주기 위해?


## 231020

### Django

DRF 회원가입 및 인증요구절차 실습하기

회원가입과 로그인 확인은 serializers에서 체크

인증 확인은 토큰으로

그럼 토큰확인은 어떻게? : 로그인된 대상만이 가질 수 있는 토큰이 있다.



## 231023

### DB

Django는 기본적으로 SQLite가 내장되어있다.

DB관련 설정은 settings.py 에서 가능

직접 SQL 쿼리를 날리기도 가능 (cursor.execute)

데이터덤프: DB의 데이터 추출
데이터로드: 데이터를 읽고 DB에 저장

## 231024

### DB

SQL 쿼리 실습 https://sqlschool.co.kr/

inner join : 교집합


outer join : 합집합 
빈 값은 null

left outer join - 왼쪽을 기준으로 합치기 : 왼쪽에 없으면 표시되지 않음
right outer join - 오른쪽을 기준으로 합치기 : 오른쪽에 없으면 표시되지 않음

full outer join - 모두 다 합치기

## 231025

### DB

www.dbdiagram.io : DB 모델링

https://www.mindmeister.com/ 마인드맵 시각화




### 미니 프로젝트 시작 - 기술 blog 만들기

https://paullabworkspace.notion.site/Blog-2a8f9a53e2aa4c7280160ac770cdbdff

10월 26일(목) ~ 11월 7일(화) , 11월 8일 개별 발표(개인당 5분)

단계별 목표도 마련되어있다.

drf 사용 x

발표시 시연은 따로 하지 않음 -> 혹시나 필요하면 gif로 

## 231103
### 기술특강 :이진석 강사님
#### Chat GPT API를 활용한 영어 상황극 채팅 서비스 구현

Django 수업시간에 했던 과정을 오늘 하루만으로 쭉 진행해 나가면서 완성해나가는 모습이 굉장했다.
놀랍게도 강의과정이 여태 배웠던것과 거의 유사함.


## 231109

### 취업특강

자소서 는 직무선정이 가장 먼저
자소서와 면접은 연계된다

한눈에 보이게 두괄식, 한줄 이내, 소제목과 문단구분
경험/경력에는 나름의 이유가 있어야 한다

우대사항? : 완전 필수는 아니지만, 그럼 모집공고에 왜썼을까? 
지원동기? : 이왕이면 '근거가 있는' 의욕 -자아실현, 명예와 인정 류
- 지원기업에 관심이 있는가? , 기업과 직무에 이해도가 있는가?

과거대비? 상대적으로 중요도는 줄었다 라고는 함


성공/협업/개선/갈등 등의 경험

결국은 in-output 이 나오고, 수치로 나오는게 제일 좋다

## 231110

### 취업특강

나에게 일이란 어떤 의미? : 회사에서는 늘 이걸 물어본다 

좋아하는일? 해야하는 일? 잘하는일? : 객관적으로 파악하자

STAR 기법
- Sitiuaion 내가 처한 상황에 대해 말하기
- Task 내가 수행한 과제, 과업은?
- Action 어떤 행동을?
- Result 그 행동의 결과는?

모든 출구는 어딘가로 들어가는 입구다

경험 - 인식 - 실천 - 결과 로 이어지는 순환학습하기