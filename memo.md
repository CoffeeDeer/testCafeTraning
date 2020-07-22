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
* 스마트 assertion query 메커니즘
    * await t (디폴트 3초)
* 옵션들
    * 타임아웃 - 테스트가 실패하기 까지 걸리는 시간초

클라이언트 사이드 정보 가져오기
* ClientFunction 을 사용하여 window location 가져오기
* 비동기 클라이언트 사이드 코드를 실행시킬수 있다.
* 덮어쓰기있고
* saving 없이 클라이언트 함수를 생성하고 바로 실행할수 있다?
* 의존성있는 클라이언트 함수를 임포팅
* 노드 js 콜백에서 클라이언트 함수를 호출
* 한계
    * 클라이언트 함수 내부에서 generators / async / await 사용 불가
    * 클라이언트 함수들은 outer scope 에 접근 불가(그러나 함수 인자로 일방향 전달가능)
*  콘솔 메세지에 액세스
* 페이지 URL 확인 가능
* 브라우저를 확인 가능
* 복잡한 DOM 쿼리 사용 

테스트 구동
* 커맨드 라인으로 실행
* js / ts api 로 실행
* 여러개의 테스트 파일 실행
* glob 패턴 사용
* test 파일내 filtring 하여 특정 테스트만 진행 가능
    * -f fixture
    * -t test
* 특정 metadata를 가진 테스트, fistures 만 실행
* 타겟 브라우저
* 멀티 브라우저 실행
* 테스트를 브라우저:헤드리스 모드로 실행
* 브라우저:특정 모바일 디바이스 - 환경에서 실행
* 클라우드 테스팅 서비스(saucelabs) 실행
* 원격 & 모바일 디바이스에서 테스트 진행
* 리포트 포맷을 설정 확인가능
    * -r xunit
    * -r my-reporter
    * -r json:report.json
    * -r spec, xunit:report.xml
* 스크린샷 비디오 세팅을 커스터마이징 가능
* 테스트를 동시에(Concurrently) 하게 실행 할 수 있다.
    * 엣지를 지원하지 않는다.
    * 테스트가 동시에 실행되는 브라우저 풀을 구 성
* 테스트된 앱을 스테이지 할수 있다 
* 프록시 URL제공 
* 라이브 모드
* 격리모드





















