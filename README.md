# Ormi_3rd
오르미 3기 폴더

230816

VSC 설치, extension 환경설정 및 html 기초에 대해 학습

230817

html 기본 강의 
- 블록과 인라인 요소 : 한줄 차지+줄바꿈, 일정 공간만 차지
- 다양한 태그들 : div,span, header, article, section, h1,a,p, br, hr... etc
- 양식(form) : label, button, input, fieldset ... etc

연습문제

act1 : 게시판 글조회 페이지 만들어 보기
- footer, ul, ol 태그 사용

act2 : 로그인 페이지 만들어 보기
- form, label, input 태그 사용

act3 : 회원가입 양식 페이지 만들어 보기
- fieldset, radio, checkbox 태그 사용

230818

html 기본 강의
- 양식(form) : select , option , fieldset, textarea
- 표(table) : tr, th, td

css 기본 강의
- css의 정의 : cascade style sheet
- css 적용방법, 상속
- css 선택자, 선택자 우선순위
- css display 속성 : 블록, 인라인 요소는 그대로 시각적으로만 변화
- css 단위, box model

연습문제

act4 : 게시판 글목록 페이지 만들어보기
- table, tr, th, td 태그 사용

CSS 선택자 관련 문제풀이
- 외부 웹사이트(CSS DINER https://flukeout.github.io/) , CSS SPEEDRUN (https://css-speedrun.netlify.app/)


230819

act5: 주말과제 - 로그인 페이지 (act2) 에 CSS입히기 
- margin과 padding 등의 수치를 바꿔가며 가운데로 위치시키려 했지만, 창 크기를 바꾸면 위치가 바뀌어 의미가 없었다.
- 가운데 정렬은 가장 큰 tag에서 'margin:auto'로 하는 편이 가장 편하고 세부적인 위치 조정은 각각 tag에서 조정 해주는 것이 최고다.


230821

css 기본 강의
- float: block 요소가 아닌 것에 float를 주면 block이 된다. 해제는 clear로.
- flex : 'display:flex' 로 시작한다. 컨테이너에 선언하고 안에 내부의 item들의 배치를 조정하는 방식.

flex 관련 문제풀이
- 외부 웹사이트 (flexbox-froggy https://flexboxfroggy.com/#ko)

act5 주말과제 해설
- 내 코드와 다른점은 ? : 대부분의 태그에 class선언하고, 이를 css로 편집하는 방식. 코드의 재사용과 쉬운 편집을 위함?
- 중복된 선언은 최대한 묶어서 선언.

act6 회원가입 페이지(act3)에 css 입히기 : 시간초과

 왜 시간초과 했는가? 

--1)fieldset에 flex가 먹히지 않아서 헤멨다. -> fieldset 태그를 빼버리고 section으로 전환 후 flex 먹이기 시도

--2) ul에 flex를 먹이니 까만점?이 남아있었다. -> 이를 없애기 위해 ul과 li 태그도 빼버리고 flex 먹이기 시도

---1) 이런 경우엔 flaot를 쓰거나, fieldset 태그를 바꿔야 하는 것이 맞다

---2) list-style: none;을 입히면 까만점이 사라진다. 의외로 간단.

생각보단 사소한 곳에서 시간을 잡아먹어 고민하느라 오래걸렸다.


230822

글목록(act4) css 입히기, 게시판 글 작성 html+css 만들기, layout 만들기, chat 만들기 실습
아쉽지만 간단한 layout을 빼고는 시간내에 잘 만들지 못했다. (강사님의 완성본은 board 폴더)
왜 시간초과 했는가?
-게시판 글 작성은 flex와 float등으로 이리 저리 해보려다 실패 -> 해설에선 table 사용
-chat은 배치와 이미지 경로? 에 신경쓰다가 헤멨다. -> 이미지 경로는 상대경로가 맞다



230823

JavaScript 기초 강의 

JavaScript는 웹페이지에서 '동작하는 프로그램'을 만들 때 사용

HTML과 연결은 body 태그 밑에<script src = ""> 형태로 연결 확장자는 .js



변수는 var, let, const로 선언한다.

var - 가장 유연한? 선언. init 안해도 된다. 키워드 생략시 기본적으로 var로 선언 (엄격모드에선 불가)

let과 const는 블록 레벨 선언. 블록 밖에서 접근 불가 (지역 변수 느낌?), 재정의 불가

const는 init 필수. 값 변경 불가(상수 취급)

원시 타입

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
