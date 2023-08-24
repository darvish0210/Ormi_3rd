
function 함수1(a,b,c){
    return a+b+c;
}
// console.log(함수1(1,2,3));




// 즉시실행 함수
(function(x,y){return x+y})(3,4);




// 화살표 함수(람다식)
let 함수2 = (x,y)=> x + y;


// console.log(((x,y)=>x+y)(5,6));


const arr = [1,2,3];
function callbackfn(item){
    return item*2
}
console.log(arr.map(callbackfn))
console.log(arr)






//과제1: 홀수만 더하는 reduce 함수
const arrr = [1,2,3,4,5,6,7,8,9,11,13,14,18]
function reducer(x,y){
    if (y%2 === 1)
        return x+y
    else
        return x
}
const resultt = arrr.reduce(reducer,0);
console.log(resultt)

// 과제2 :초깃값이 없으면 애러가 날 수 있는 경우 찾기

// 초깃값이 없으면 자동으로 0번째 인덱스가 초깃값이 되는데, 빈 배열이면 에러가 반드시 발생한다.

const arrrr = []
function reducer(x,y){
    return (x+y)/arrrr.length
}
const resulttt = arrrr.reduce(reducer);
console.log(resulttt)

// 초깃값을 주면 에러가 발생하지 않는다.
const arrrr = []
function reducer(x,y){
    return (x+y)/arrrr.length
}
const resulttt = arrrr.reduce(reducer,0);
console.log(resulttt)
