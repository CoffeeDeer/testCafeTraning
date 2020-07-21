체크해야될 중요 포인트는 어떤점들 인가요? 
(예를들면 UI의 배치?

기본 가이드

테스트 구성하기
(생략


페이지 엘리먼트 선택하기
* 셀렉터 변수를 함수형으로 선언 가능
* 하나의 셀렉터에 여러개의 엘리먼트가 선택 될 수 있다.


셀렉터 사용하기
* 엘리먼트 갯수를 확인 할 수 있다.
    * eql, ok 사용 할 수 있다.
* const 변수를 선언할때 기다렸다가 선언되게 할 수 있다. (초기값 X)
* 테스트 밖에서 선언한 변수를 테스트 내부에서 사용 할 수 있다.
* 선언된 셀렉터 변수의 요소를 검증 하는 테스트 를 할 수 있다.
* 커스텀 셀  렉터를 선언하여 사용 할 수 있다.
* 옵션을 오버라이드 할 수 있다. 
* 프레임 워크에 종속적인 셀렉터들도 있다.
    * 리액트 
    * 앵귤러
    * 뷰
* 노드 js 콜백에서 셀렉터를 부르는 방법
* 섀도우돔에 엑세스 할 수 있다.
* 엘리먼트가 사용 가능한 상황인지 알 수 있다.

페이지와 상호 작용 하기
* 클릭(클릭, 더블클릭, 우클릭 가능)
* 키보드 버튼도 누를수 있다(space, delete)
* 특정 URL로 네비게이트
* input element 에 텍스트 입력
* 특정 element 위로 hover
* 엘리먼트 드래그
* 파일 업로드 
* 화면의 스크린샷을 찍을수 있다. 
* iframe 사용
* 윈도우 리사이즈
* wait으로 프로세스 정

assert = 검증한다
* expect method
    * deep equal, not deep equal
    * ok, not ok ( t.expect(Selector('#element').exists).ok();
    * contains, not contains
    * type of, not type of
    * greater than, not case
    * less than, not case
    * within, not
    * match, not



















