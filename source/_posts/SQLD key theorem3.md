---
title: SQLD key theorem3
tag: SQLD key theorem3
date: 2022-03-07
categories:	SQLD
---
# SQLD 핵심정리3

**<순수 관계연산자와 SQL 문장 비교>**

- SELECT 연산은 WHERE 절로 구현
- PROJECT 연산은 SELECT 절로 구현
- (NATURAL) JOIN 연산은 다양한 JOIN 기능으로 구현
- DIVIDE 연산은 현재 사용되지 않음.

**<ANSI/ISO-SQL에서 표시하는 FROM 절의 JOIN형태>**

- INNER JOIN
- NATURAL JOIN
- USING 조건절
- ON 조건절
- CROSS JOIN
- OUTER JOIN(LEFT,RIGHT, FULL)

▶ **INNER JOIN** 

INNER JOIN은 OUTER(외부) JOIN과 대비하여 내부 JOIN이라고 하며 JOIN 조건에서 동일한 값이 있는 행만 반환한다.

▶ **CROSS JOIN** 

테이블 간 JOIN 조건이 없는 경우 생길 수 있는 모든 데이터의 조합을 말한다. 결과는 양쪽 집합의 M*N 건의 데이터 조합이 발생한다.

▶ **LEFT OUTER JOIN** 

조인 수행시 먼저 표기된 좌측 테이블에 해당하는 데이터를 먼저 읽은 후, 나중 표기된 우측 테이블에서 JOIN 대상 데이터를 읽어 온다. 즉, Table A와 B가 있을 때(Table ‘A’가 기준이 됨), A와 B를 비교해서 B의 JOIN 칼럼에서 같은 값이 있을 때 그 해당 데이터를 가져오고, B의 JOIN 칼럼에서 같은 값이 없는 경우에는 B 테이블에서 가져오는 칼럼들은 NULL 값으로 채운다.

▶ **FULL OUTER JOIN**

조인 수행시 좌측, 우측 테이블의 모든 데이터를 읽어 JOIN하여 결과를 생성한다. 즉, TABLE A와 B가 있을 때(TABLE ‘A’, ‘B’ 모두 기준이 됨.), RIGHT OUTER JOIN과 LEFT OUTER JOIN과 LEFT OUTER JOIN의 결과를 합집합으로 처리한 결과와 동일하다.

**<OUTER JOIN 문장 예시>**

- **LEFT OUTER JOIN**

  SELECT X.KEY1, Y.KEY2

  FROM TAB1 X LEFT OUTER JOIN TAB2 Y

  ON (X.KEY1=Y.KEY2)

 

- **RIGHT OUTER JOIN**

  SELECT X.KEY1, Y.KEY2

  FROM TAB1 X RIGHT OUTER JOIN TAB2 Y

  ON(X.KEY1=Y.KEY2)

 

- **FULL OUTER JOIN**

  SELECT X.KEY1, Y.KEY2

  FROM TAB1 X FULL OUTER JOIN TAB2 Y

  ON (X.KEY1=Y.KEY2)0

  

**<집합 연산자의 종류>**

|    집합 연산자  |                                                                       연산자의 의미  |
| --- | --- |
|        UNION | 여러 개의 SQL문의 결과에 대한 합집합으로 결과에서 모든 중복된 행은 하나의 행으로 만든다. |
|     UNION ALL | 여러 개의 SQL문의 결과에 대한 합집합으로 중복된 행도 그래도 결과로 표시된다. 즉, 단순한 결과만 합쳐놓은 것이다. 개별 SQL문의 결과가 서로 중복되지 않는 경우, UNION과 결과가 동일하다. |
|     INTERSECT | 어러 개의 SQL문의 결과에 대한 교집합이다. 중복된 행은 하나의 행으로 만든다. |
|       EXCEPT | 앞의 SQL문의 결과에서 뒤의 SQL문의 결과에 대한 차집합이다. 중복된 행은 하나의 행으로 만든다. |

**<집합 연산자 쿼리문과 일반 쿼리문 차이>**

**일반 쿼리문**

SELECT 칼럼명1, 

             칼럼명2, ....

FROM 테이블명1

[WHERE 조건식]

[[GROUP BY

    칼럼이나 표현식

[HAVING 그룹조건식]]

**집합연산자 쿼리문** 

SELECT 칼럼명1,

            칼럼명2,...

FROM 테이블명1

[WHERE 조건식]

[[GROPUP BY 

    칼럼이나 표현식

[HAVING 그룹조건식]]

**[ORDER BY 1,2**

    **ASC 또는 DESC];**

→ ORDER BY는 집합 연산을 적용한 최종 결과에 대한 정렬 처리이므로 

    마지막에 한번만 기술한다.

**<일반 집합 연산자를 SQL과 비교>**

- UNION 연산은 UNION 기능이 됨.
- INTERSECTION 연산은 INTERSECT 기능이 됨.
- DIFFERENCE 연산은 EXCEPT(Oracle은 MINUS) 기능이 됨.
- PRODUCT 연산은 CROSS JOIN 기능이 됨.

▶ **PRIOR** 

 CONNECT BY 절에서 사용되며, 현재 읽는 칼럼을 지정한다.  PRIOR 자식 = 부모 형태를 사용하면 계층구조에서 부모 데이터에서 자식 데이터(부모 → 자식) 방향으로 전개하는 순방향 전개를 한다. 그리고 PRIOR 부모 = 자식 형태를 사용하면 반대로 자식 데이터에서 부모 데이터(자식 →부모) 방향으로 전개하는 역방향 전개를 한다.

▶ **START WITH 절**은 계층구조 전개의 시작 위치를 지정하는 구문이다. 즉, 루트 데이터를 지정한다.(엑세스)

▶ **ORDER SIBLINGS BY** : 형제 노드(동일 LEVEL) 사이에서 정렬을 수행한다.

▶ **계층형 질의** : 테이블에 계층형 데이터가 조재하는 경우 데이터를 조회하기 위해서 사용.

▶ **계층형 데이터** 

동일 테이블에 계층적으로 상위와 하위 데이터가 포함된 데이터를 말한다.

예를 들어, 사원 테이블에서는 사원들 사이에 상위 사원(관리자)과 하위 사원 관계가 존재하고 조직 

테이블에서는 조직들 사이에 상위 조직과 하위 조직 관계가 존재하는 것이 이와 같은 개념이다.

▶ **셀프 조인(Self Join)**

동일 테이블 사이의 조인을 말한다. 따라서 FROM절에 동일 테이블이 2번 이상 나타난다. 동일 테이블 사이의 조인을 수행하면 테이블과 칼럼 이름이 모두 동일하기 때문에 식별을 위해 반드시 테이블 별칭(Alias)를 사용해야 한다.

**<셀프 조인(Self Join) 문장>**

SELECT

    ALIAS명1.칼럼명,

    ALIAS명2.칼럼명, ...

FROM

    테이블 ALIAS명1,

    테이블 ALIAS명2

WHERE

    ALIAS명1.칼럼명2 =

    ALIAS명2.칼럼명1;

![Untitled](SQLD%20%E1%84%92%E1%85%A2%E1%86%A8%E1%84%89%E1%85%B5%202dcf5/Untitled.png)

**<반환되는 데이터의 형태에 따라 서브쿼리 분류>**

|                             서브쿼리 종류 |                                                      설명 |
| --- | --- |
|           Sing Row 서브쿼리(단일행 서브쿼리) | 서브쿼리의 실행 결과가 항상 1건 이하인 서브쿼리를 의미한다.     단일 행 서브쿼리는 단일 행 비교 연산자와 함께 사용된다.                                                단일 행 비교연산자에는 =,<,< =,>,> =, <>이 있다. |
|          Multi Row 서브쿼리(다중 행 서브쿼리) | 서브쿼리의 실행 결과가 여러 건인 서브쿼리를 의미한다. 다중 행 서브쿼리는 다중 행 비교 연산자와 함께 사용된다.                         다중 행 비교연산자에는 IN, ALL, ANY, SOME, EXISTS가 있다. |
|     Multi Column 서브쿼리(다중 칼럼 서브쿼리) | 서브쿼리의 실행 결과로 여러 칼럼을 반환한다. 메인쿼리의 조건절에 여러 칼럼을 동시에 비교할 수 있다.                                           서브쿼리와 메인쿼리에서 비교하고자 하는 칼럼 개수와 칼럼의 위치가 동일해야 한다. |

▶ **인라인 뷰(InIine View)**

FROM 절에서 사용하는 서브쿼리를 말한다. 서브쿼리의 결과가 마치 실행 시에 동적으로 생성된 테이블인 것처럼 사용할 수 있다. 인라인 뷰는 SQL문이 실행 될 때만 임시적으로 생성되는 동적인 뷰이기 때문에 데이터베이스에 해당 정보가 저장되지 않는다. 

서브쿼리의 결과가 마치 실행 시에 동적으로 생성된 테이블인 것처럼 사용할 수 있다. 인라인 뷰는 SQL문이 실행될 때만 임시적으로 생성되는 동적인 뷰이기 때문에 데이터베이스에 해당 정보가 저장되지 않는다. 

**<뷰 사용의 장점>**

- 독립성 : 테이블 구조가 변경되어도 뷰를 사용하는 응용 프로그램은 변경하지 않아도 된다.
- 편리성 : 복잡한 질의를 뷰로 생성함으로써 관련 질의를 단순하게 작성할 수 있다. 또한 해당 형태의 SQL문을 자주 사용할 때 뷰를 이용하면 편리하게 사용할 수 있다.
- 보안성 : 직원의 급여정보와 같이 숨기고 싶은 정보가 존재한다면, 뷰를 생성할 때 해당 칼럼을 빼고 생성함으로써 사용자에게 정보를 감출 수 있다.

▶ **Grouping Columns** 

가질 수 있는 모든 경우에 대하여 Subtotal을 생성해야 하는 경우에는 CUBE를 사용하는 것이 바람직하나, ROLLUP에 비해 시스템에 많은 부담을 주므로 사용해 주의 할 것

▶ **CUBE**

결합가능한 모든 값에 대하여 다차원 집계를 생성한다. CUBE도 결과 에 대한 정렬이 필요한 경우는 ORDER BY 절에 명시적으로 정렬 칼럼이 표시 되어야 한다.

▶ **GROUPING SETS**

다양한 소계 집합을 만들 수 있는데, GROUPING SETS에 표시된 인수들에 대한 개별 집계를 구할 수 있으며, 이때 표시된 인수들 간에는 계층 구조인 ROLLUP과는 달리 평등한 관계이므로 인수의 순서가 바뀌어도 결과는 같다. 

그리고 GROUPING SETS 함수도 결과에 대한 정렬이 필요한 경우는 ORDER BY 절에 명시적으로 정렬 칼럼이 표시 되어야 한다.

▶ **RANK 함수**

ORDER BY를 포함한 QUERY 문에서 특정 칼럼에 대해 순위를 구하는 함수이며 동인한 값에 대해서는  동일한 순위를 부여하게 된다.

▶**DENSE RANK 함수**

RANK 함수와 흡사하나, 동일한 순위를 하나의 건수로 취급하는 것이 다른 점이다.

▶ **ROW_NUMBER 함수**

RANK나 DENSE_RANK 함수가 동일한 값에 대해서는 동일한 순위를 부여하는데 반해, 동일한 값이라도 고유한 순위를 보유한다.

**<PL/SQL의 특징>**

- PL/SQL은 Block 구조로 되어있어 각 기능별로 모듈화가 가능하다.
- 변수, 상수 등을 선언하여 SQL 문장 간 값을 교환한다.
- IF, LOOP 등의 절차형 언어를 사용하여 절차적인 프로그램이 가능하도록 한다.
- DBMS 정의 에러나 사용자 정의 에러를 정의하여 사용할 수 있다.
- PL/SQL은 Oracle에 내장되어 있으므로 Oracle과 PL/SQL을 지원하는 어떤 서버로도 프로그램을 옯길 수 있다.
- PL/SQL은 응용 프로그램의 성능을 향상시킨다.
- PL/SQL은 여러 SQL문장을 Block으로 묶고 한 번에 Block 전부를 서버로 보내기 때문에 통신량을 줄일 수 있다.

▶ **저장 모듈(Stored Module)**

SQL 문장을 데이터베이스 서버에 저장하여 사용자와 애플리케이션 사이에서 공유할 수 있도록 만든 일종의 SQL 컴포넌트 프로그램이며, 독립적으로 실행되거나 다른 프로그램으로부터 실행될 수 있는 완전한 실행 프로그램이다.

Oracle의 저장 모듈에는 Procedure, User Defined Function, Trigger가 있다.

**<프로시저와 트리거의 차이점>**

|                   프로시저 |                    트리거 |
| --- | --- |
| CREATE Procedure 문법사용 | CREATE Trigger 문법사용 |
| EXECUTE 명령어로 실행 | 생성 후 자동으로 실행 |
| COMMIT, ROLLBACK 실행가능 | COMMIT, ROLLBACK 실행안됨 |

▶ **Sort Merge Join**

조인 칼럼을 기준으로 데이터를 정렬하여 조인을 수행한다. NL Join은 주로 랜덤 엑세스 방식으로 데이터를 읽는 반면 Sort Merge Join은 주로 스캔 방식으로 데이터를 읽는다. Sort Merge Join은 랜덤 엑세스로 NL Join에서 부담이 되던 넓은 범위의 데이터를 처리할 때 이용되던 조인기법이다. 그러나 Sort Merge Join은 정렬할 데이터가 많아 메모리에서 모든 정렬 작업을 수행하기 어려운 경우에는 임시 영역(디스크)을 사용하기 때문에 성능이 떨어질 수 있다.

▶**Hash Join**

조인 칼럼의 인덱스를 사용하지 않기 때문에 조인 칼럼의 인덱스가 존재하지 않을 경우에도 사용할 수 있는 조인 기법이다. Hash Join은 해쉬 함수를 이용하여 조인을 수행하기 때문에 ‘=’로 수행하는 조인 즉, 동등 조인에서만 사용 가능하다.

▶ **클라이언트가 서버 프로세스와 연결하는 Oracle의 예**

1) 전용 서버(Dedicated Server) 방식

2) 공유 서버(Shared Server) 방식

▶ **SQL Server에서**는 **세그먼트**는 테이블, 인덱스, Undo처럼 저장공간을 필요로 하는 데이터베이스 오브젝트다. 저장공간을 필요로 한다는 것은 한 개 이상의 익스텐트를 사용함을 뜻한다.

▶ **SQL Server에서**는 **세그먼트**라는 용어를 사용하지 않지만, 힙 구조 또는 인덱스 구조의 오브젝트가 여기에 속한다.

▶ DB 버퍼 캐시에 가해자는 모든 변경사항을 기록하는 Oracle은 ‘**Redo 로그**’라고 부르며, 

     SQL Server는 ‘**트랙잭션 로그**’라고 부른다.

▶ **Response Time Analysis 방법론**

Response Time을 정의하고, CPU Time과 Wait Time을 각각 break down 하면서 서버의 일량과 대기 시간을 분석해 나간다. CPU Time은 파싱 작업에 소비한 시간인지 아니면 쿼리 본연의 오퍼레이션 수행을 위해 소비한 시간인지를 분석한다. Wait Time은 각각 발생한 대기 이벤트들을 분석해 가장 시간을 많이 소비한 이벤트 중심으로 해결방안을 모색한다.

▶ **소프트 파싱과 하드 파싱**

- 소프트 파싱(Soft Parsing) : SQL과 실행계획을 캐시에서 찾아 곧바로 실행단계로 넘어가는 경우를 말함.
- 하드 파싱(Hard Parsing) : SQL과 실행계획을 캐시에서 찾지 못해 최적화 과정을 거치고 나서 실행단계로 넘어가는 경우를 말함.

▶ **바인드 변수 (Bind Variable)** : 파라미터 Driven 방식으로 SQL을 작성하는 방법이 제공되는데 SQL과 실행계획을 여러 개 캐싱하지 않고 하나를 반복 재사용하므로 파싱 소요시간과 메모리 사용량을 줄여준다.

▶ **SQL 커서에 대한 작업요청에 따른 데이터베이스 Call의 구분**

1. Parse Call : SQL 파싱을 요청하는 Call
2. Execute Call : SQL 실행을 요청하는 Call
3. Fetch Call : SELECT문의 결과 데이터 전송을 요청하는 Call

▶ **사용자 정의 함수/프로시저**

내장 함수처럼 Native 코드로 완전 컴파일된 형태가 아니어서 가상머신(Virtual Machine) 같은 별도의 실행 엔진을 통해 실행된다.

실행 될 때마다 컨텍스트 스위칭(Context Switching)이 일어나며, 이 때문에 내장 함수(Built-In)를 호출할 때와 비교해 성능을 상당히 떨어뜨린다.

▶ **Single Block I/O 와 Multi Block I/O**

- Sigle Block I/O : 한번의 I/O Call에 하나의 데이터 블록만 읽어 메모리에 적재하는 방식
- Multi Block I/O : I/O Call이 필요한 시점에, 인접한 블록들을 같이 읽어 메모리에 적재하는 방식

▶ **버퍼 캐시 히트율(Buffer Cache Hit Ratio)** 

버퍼 캐시 효율을 측정하는 지표로서, 전체 읽은 블록 중에서 메모리 버퍼 캐시에서 찾은 비율을 나타낸다.

물리적인 디스크 읽기를 수반하지 않고 곧바로 메모리에서 블록을 찾은 비율을 말한다.

▶ **I/O튜닝의 핵심 원리**

■ Sequential 엑세스에 의한 선택 비중을 높인다.

■ Random 엑세스 발생량을 줄인다.