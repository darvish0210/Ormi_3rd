# Ormi_3rd

-오르미 3기 학습 내용

## 230816

VSC 설치, extension 환경설정 및 html 기초에 대해 학습

## 230817

### html 기본 강의
- 블록과 인라인 요소 : 한줄 차지+줄바꿈, 일정 공간만 차지
- 다양한 태그들 : div,span, header, article, section, h1,a,p, br, hr... etc
- 양식(form) : label, button, input, fieldset ... etc

### 연습문제

act1 : 게시판 글조회 페이지 만들어 보기
- footer, ul, ol 태그 사용

act2 : 로그인 페이지 만들어 보기
- form, label, input 태그 사용

act3 : 회원가입 양식 페이지 만들어 보기
- fieldset, radio, checkbox 태그 사용

## 230818

### html 기본 강의
- 양식(form) : select , option , fieldset, textarea
- 표(table) : tr, th, td

### css 기본 강의
- css의 정의 : cascade style sheet
- css 적용방법, 상속
- css 선택자, 선택자 우선순위
- css display 속성 : 블록, 인라인 요소는 그대로 시각적으로만 변화
- css 단위, box model

### 연습문제

act4 : 게시판 글목록 페이지 만들어보기
- table, tr, th, td 태그 사용

CSS 선택자 관련 문제풀이
- 외부 웹사이트(CSS DINER https://flukeout.github.io/) , CSS SPEEDRUN (https://css-speedrun.netlify.app/)


## 230819

### 연습문제

act5: 주말과제 - 로그인 페이지 (act2) 에 CSS입히기 
- margin과 padding 등의 수치를 바꿔가며 가운데로 위치시키려 했지만, 창 크기를 바꾸면 위치가 바뀌어 의미가 없었다.
- 가운데 정렬은 가장 큰 tag에서 'margin:auto'로 하는 편이 가장 편하고 세부적인 위치 조정은 각각 tag에서 조정 해주는 것이 최고다.


## 230821

### css 기본 강의
- float: block 요소가 아닌 것에 float를 주면 block이 된다. 해제는 clear로.
- flex : 'display:flex' 로 시작한다. 컨테이너에 선언하고 안에 내부의 item들의 배치를 조정하는 방식.

flex 관련 문제풀이
- 외부 웹사이트 (flexbox-froggy https://flexboxfroggy.com/#ko)

act5 주말과제 해설
- 내 코드와 다른점은 ? : 대부분의 태그에 class선언하고, 이를 css로 편집하는 방식. 코드의 재사용과 쉬운 편집을 위함?
- 중복된 선언은 최대한 묶어서 선언.

act6 회원가입 페이지(act3)에 css 입히기 : 시간초과

 왜 시간초과 했는가? 

- 1.fieldset에 flex가 먹히지 않아서 헤멨다. -> fieldset 태그를 빼버리고 section으로 전환 후 flex 먹이기 시도
-- 이런 경우엔 flaot를 쓰거나, fieldset 태그를 바꿔야 하는 것이 맞다

- 2. ul에 flex를 먹이니 까만점?이 남아있었다. -> 이를 없애기 위해 ul과 li 태그도 빼버리고 flex 먹이기 시도
-- list-style: none;을 입히면 까만점이 사라진다. 의외로 간단.

생각보단 사소한 곳에서 시간을 잡아먹어 고민하느라 오래걸렸다.


## 230822

### CSS 강의

글목록(act4) css 입히기, 게시판 글 작성 html+css 만들기, layout 만들기, chat 만들기 실습
아쉽지만 간단한 layout을 빼고는 시간내에 잘 만들지 못했다. (강사님의 완성본은 board 폴더)

왜 시간초과 했는가?
- 게시판 글 작성은 flex와 float등으로 이리 저리 해보려다 실패 -> 해설에선 table 사용
- chat은 배치와 이미지 경로? 에 신경쓰다가 헤멨다. -> 이미지 경로는 상대경로가 맞다



## 230823

### JavaScript 기초 강의

JavaScript는 웹페이지에서 '동작하는 프로그램'을 만들 때 사용

HTML과 연결은 body 태그 밑에<script src = ""> 형태로 연결 확장자는 .js

변수는 var, let, const로 선언한다.

var - 가장 유연한? 선언. init 안해도 된다. 키워드 생략시 기본적으로 var로 선언 (엄격모드에선 불가)

let과 const는 블록 레벨 선언. 블록 밖에서 접근 불가 (지역 변수 느낌?), 재정의 불가

const는 init 필수. 값 변경 불가(상수 취급)

#### 원시 타입

-타 언어처럼 자료형 선언 하지 않음(ex. 자바의 int a = 10;)
이 성질 때문에 타 언어에선 볼 수 없는 이상한 모습들이 나올 수 있다. (91-"1" = 90????)

1.문자열
따옴표로 선언. var a = '문자입니다.'
일종의 배열처럼 취급하여 그 성질이 그대로 있다.(불변성, 인덱스등의 메소드 등)


2.숫자 -> 기본적인 연산들이 다 가능하나, 소수 연산에선 부정확 할 수 있다.(소수 표현의 한계때문)
Infinity : 무한대. 0으로 나누기나 아주 큰 수에 나타남.
NaN : Not a Number. 연산이 아예 불가능한 타입과 연산하려 할 때 반환됨.

3.논리 자료형 -> true, false Boolean 계열
and(&&) or(||) not(!)과 관련됨.

4.undefined : 값이 '정의되지 않음' 을 나타냄

5.null : 값이 '없음'을 나타냄

undefined와 null의 차이는? 값의 '초기화'만을 목적으로 한다면 비슷할 수 있으나 undefined는 '아직 할당되지 않음' 에 더 가까움. 기본적으로 초기화는 null이 더 적당하다.




## 230824

### JavaScript 기초 강의
<<<<<<< HEAD


#### 함수
=======
>>>>>>> 7c0c89e (230911 ipynb upload AND README REWRITE)


#### 함수

함수는 fuction으로 선언하며, parameter(매개변수)를 받아 내부의 기능을 수행 후, return(반환값)을 반환해준다.
간단하게는 화살표 선언이나, 즉시실행식으로도 만들 수 있다.

화살표 선언 스타일 (==람다식)

let fun1 = (x,y)=>x+y;

즉시실행함수

function(x,y){return x+y})(1,7)

객체타입

1. 배열 Array
JS에선 빈 배열 선언도 가능. 배열 요소를 수정하는 것도 가능.
존재하지 않는 원소에도 접근가능(undefined로 뜨며 에러가 아니다!)

다만 sort()는 기본적으로 조금 이상하다. 숫자정렬이 str화 시킨 후, 유니코드 포인트 순으로 정렬되기 때문.

push(a) : 배열 끝에 a 추가후 길이 return
pop() : 마지막 요소 꺼낸 후 그 요소 return
shift() : 첫번째 요소를 꺼낸 후 그 요소 return
unshift(a) : 맨 앞에 a를 넣은 후 길이 return
splice(a,b,c) : a번 index에서 부터 b만큼 삭제 후 c 추가

예시
```jsx
const arr = [1,4,2,3,1,6]
arr.splice(2, 2, 5, 2, 4); //2번 index (2)부터 2개 지우고(2,3 삭제), 5 2 4 추가 
console.log(arr); // [1, 4, 5, 2, 4, 1, 6]
```

slice(a,b) : a번째 index부터 추출 시작하여 b번째 index에서 추출 하고 새로운 배열로 return (생략시 배열 끝까지 추출)

foreach(f) : arr의 각 요소에 함수f 실행
map(f) : arr의 각 요소에 함수f 실행 후 결과 return

foreach와 map의 차이는 ? -> map은 결과로 나온 배열을 return 해준다!

filter(x) : x를 만족하는 요소만 추출해서 새 배열을 return

reduce() : arr의 각 요소에 f를 실행하고, 그 결과가 누적된 하나의 값을 return

예시
```jsx
const arrrr = [1,2,3,4,5]
function reducer(x,y){
    return (x+y)
}
const resulttt = arrrr.reduce(reducer);
console.log(resulttt) // 총합구하기
```

includes(x) : x가 포함되면 true, 아니면 false
join(s) : 각 요소를 's' 로 연결 시켜주는 용 


객체에게는 기본적으로 key와 value가 있으며, 
이는 keys() 와 values()로 뽑아볼 수 있다.

```jsx
const babaYaga = {
  name: "John Wick",
  age: 53,
  from: "벨라루스",
	askingHim: function(){
		console.log("Yeah, I'm thinking I'm back!");
	}
};
```

## 230825
<<<<<<< HEAD
=======


### JavaScript 기초 강의
>>>>>>> 7c0c89e (230911 ipynb upload AND README REWRITE)


### JavaScript 기초 강의

#### 조건문 (if-else, switch)

삼항 연산자 : if-else를 간단하게 표현하는 방식
```jsx
let x = true ? console.log('참') : console.log('거짓');
console.log(x);
```

반복문 (for,while,do-while)

label : 특정 코드블록에 이름을 지정하여 블록 안에서 break나 continue의 대상으로 쓸 수 있다.
```jsx
outer: for (let i = 0; i < 3; i++) {
  for (let j = 0; j < 3; j++) {
    if (i + j === 3) {
      break outer;
    }
    console.log(i, j);
  }
}
```



전개구문


```jsx
const 과일들 = ['사과', '파인애플', '수박'];
const 생선들 = ['조기', '갈치', '다금바리'];
const 합치면 = [...과일들, ...생선들];

console.log(합치면); 
```
...으로 합치기 가능


구조 분해(디스트럭쳐링)

```jsx
let {one, two, three, four} = {one: 1,three:2,two:3}

console.log(one); //1
console.log(two); //3
console.log(three); //2
console.log(four); //undefined
```

갯수가 맞지 않아도, 순서가 틀려도 에러가 안난다!
즉, 각각 할당해줘야 할 것을 편하게 쓰는 방법


JSON(JavaScript Object Notation)
xml: 마크업 랭귀지

DOM - 문서 객체 모델

DOM 은 HTML 문서의 내용을 트리형태로 구조화하여 웹페이지와 프로그래밍 언어를 연결시켜주는 역할

실제로 document.head, document.body, document.body.childNodes 등으로 확인해 볼 수 있다.



## 230828

### 회고 시간 + JS 마지막시간

promise - '콜백지옥' 을 탈출하는데 도와준다.
```jsx
let p = new Promise(function(resolve, reject) {
  // 실행코드 
});

// resolve(value) — 작업이 성공적으로 마무리되면 호출, 결과는 value에 담김
// reject(error) — 작업이 실패시 호출, error는 error에 담김
```


```jsx
async function f() {
  return '완료';
}

console.log(f);
console.log(f().then(alert));

// 완료가 된 다음 실행해보세요.

f()
```
async는 함수의 앞에 붙이며, promise를 반환한다.
이 async 함수 안에서 쓸 수 있는것이 await인데, 이를 쓰면 promise가 끝날때 까지 기다리게 할 수 있다.

```jsx
async function f() {

  let promise = new Promise((resolve, reject) => {
    setTimeout(() => resolve("완료!"), 1000)
  });

  let result = await promise; // 프라미스가 이행될 때까지 기다림 (*)

  alert(result); // "완료!"
}

f();

```

## 230829 ~ 230906

필수과제 ChatGPT 연동 개인 프로젝트 (230906 까지)
- 주제: ChatGPT 를 이용한 자율주제 (API제공됨)
- 요구사항: 기본적으로 챗봇의 형태로, 질문 제출과 답변 출력이 나와야 함

- 1일차 : 프로젝트 개요 설명 + 예시 코드 확인. 주제는 고민좀 해야할듯



### 230901

기술특강 딥러닝 with 이스트소프트 권택순 CTO님

딥러닝은 어떤 방식인가? -> 점점 맞춰나가며 '가중치' 를 두어 fitting 해나가는 과정의 반복!

최근엔 어떻게 쓰이고 있는가? -> ChatGPT, 음성인식(speech to text), TTS(text to speech), Stable Diffusion 등

Stable Diffusion이란? -> text to image 인공지능 모델. 소위 말하는 AI 그림생성
-일종의 벡터 맞추기-> n차원의 keyword와 n차원의 image를 매칭 시켜나가는 과정?

### 230904

버튼을 없애는 방법? 에 대해서 생각하느라 조금 시간이 오래 걸렸다.

내가 프로젝트에서 해보고 싶은 방식이 

다수의 버튼 표시 -> 그중 하나의 버튼 클릭-> 클릭한 버튼이 무엇인지 데이터 저장? -> 버튼 삭제 -> 선택한 버튼을 텍스트로 출력 해주며 계속 진행

의 방식이었는데 document.getElementById 로 받아와서 display를 none으로 하는 방식을 처음에 생각하지 못해서 시간이 좀 걸렸던 것 같다.

### 230905

사용할 기본적인 스타일 추가
<<<<<<< HEAD
=======

### 230906

프로젝트 완성 및 README 작성

### 230907

프로젝트 발표 및 리뷰


## 230908

### python 기초 강의

장점
1. Python-Django 는 Java-Spring에 비해 빠르게 MVP까지 올릴 수 있다.
2. 속도
3. 부하분산
4. 스케일업 - 요기요 Django

입출력, 변수, 자료형(정수,실수,문자열)

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

<<<<<<< HEAD
>>>>>>> 7867baf (ipynb 업로드)
=======


## 230911


### python 기초 강의

논리자료형

True, False, None이 있으며 True는 1, False는 0과 같이 취급된다.

None을 확인할때는 == 보다는 is 로 확인하는것이 좋다.
is 는 id값을 기준으로 판단한다.

메소드 체이닝 

STR.Foo().Foo2().Foo3() 식으로 이어나가기

형변환

float에서 str은 되지만, 그것을 바로 int로 할 수는 없다('.' 때문)

연산과 구문

'-'가 여러개 붙어도 연산이 된다? '--' 는 '+' 취급?
python에서 '//' 는 몫이 아니다! '나눈 수의 내림' 이다. (음수연산에서 확인가능)

단락회로평가

A or B 혹은 A and B 일때, A만으로 True, 혹은 False의 판별이 날 경우 A 뒤로는 쳐다도 보지 않는다.

>>>>>>> 7c0c89e (230911 ipynb upload AND README REWRITE)
