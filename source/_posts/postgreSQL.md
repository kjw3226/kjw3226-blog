----
title: Postgre SQL (포스트그리 SQL)
tag: Postgre SQL (포스트그리 SQL)
date: 2022-01-07
categories:	SQL
----
'postgreSQL'을 설치하고 
'파이참'을 활용해 '쿼리문'을 '.py(파이썬)' 파일로 만들고
터미널에서 파일을 실행시켜 테이블과 '데이터 베이스'를 생성하는
실습을 했다. 참고로 설치는 [여기]['https://dschloe.github.io/settings/postgresql_install_windows/']
  
에 들어가서 [URL]['https://www.enterprisedb.com/downloads/postgres-postgresql-downloads']
  
이 링크를 클릭해 진행하였다.

그리고 설치가 끝나면 나머지는 [여기]['https://dschloe.github.io/settings/postgresql_install_windows/']

에 다시 들어가서 '마우스 스크롤'을 내리면 '어떻게' 해야 하는지 나와있다. 따라하면
되겠다.

'파이참'에서 코드를 치기 전에 패키지를 하나 설치한다.
'터미널'을 열어서 진행.
```python
pip install psycopg2
```
이렇게 치면 패키지가 설치된다.   

본격적인 코딩 시작!!
```python
import psycopg2

def main():
    # step 01 연결
    connecting()

def connecting():
    # DB Connect
    conn = psycopg2.connect(
        host = "localhost", # SQL 서버 주소
        dbname = "postgres",
        user = "postgres",
        password = "531014",
        port = "5432"
    )

    print(conn)

if __name__ == "__main__":
    main()
```
두번 째 코드 ('db' 생성 코드)

```python
from psycopg2 import connect, extensions

def main():
    # step 01 연결
    conn = connecting()
    print(conn)

    createDB(conn)

def connecting():
    # DB Connect
    conn = connect(
        host = "localhost", # SQL 서버 주소
        dbname = "postgres",
        user = "postgres",
        password = "531014",
        port = "5432"
    )

    # print(conn)
    return conn

def createDB(conn):
    print("createDB function.. in... ")
    DB_NAME = "temp"

    # AutoCommit
    autocommit = extensions.ISOLATION_LEVEL_AUTOCOMMIT
    print("ISOLATION_LEVEL_AUTOCOMMIT:", extensions.ISOLATION_LEVEL_AUTOCOMMIT)
    conn.set_isolation_level(autocommit)

    # 쿼리 작성
    '''
    SQL_QUERY = """
        SELECT 'CREATE DATABASE GREEN' 
        WHERE NOT EXISTS (SELECT FROM pg_database WHERE datname = 'GREEN')
    """
    '''
    QUERY = '''CREATE DATABASE {DBNAME}'''.format(DBNAME = DB_NAME)

    cursor = conn.cursor()
    cursor.execute(QUERY)
    print("Database created...")

    cursor.close()

    conn.close()

if __name__ == "__main__":
    main()
```

세 번째 코드 ('table' 생성 코드)

```python
from psycopg2 import connect, extensions

def main():
    # Step 01
    conn = connecting()
    print(conn)
    # createDB(conn)
    createTable(conn)

def connecting():

    # DB connect
    conn = connect(
        host = "localhost",
        dbname = "postgres",
        user = "postgres",
        password = "531014",
        port = "5432"
    )

    # print(conn)
    return conn

def createDB(conn):
    DB_NAME = "testDB"

    # AutoCommit
    autocommit = extensions.ISOLATION_LEVEL_AUTOCOMMIT
    print("ISOLATION_LEVEL_AUTOCOMMIT:", extensions.ISOLATION_LEVEL_AUTOCOMMIT)
    conn.set_isolation_level(autocommit)

    # 새로운 데이터베이스 생성
    SQL_QUERY = """
        SELECT 'CREATE DATABASE {DB_NAME}'
        WHERE NOT EXISTS (SELECT FROM pg_database WHERE datname = 'testDB')
    """.format(DB_NAME = DB_NAME)

    cursor = conn.cursor()
    cursor.execute(SQL_QUERY)
    print("Database created successfully...!")

    # close the cursor to avoid memory leaks
    cursor.close()

    # Connection Closed to avoid memory leaks
    conn.close()

def createTable(conn):

    TABLE_NAME = "TEMP"

    # AutoCommit
    autocommit = extensions.ISOLATION_LEVEL_AUTOCOMMIT
    print("ISOLATION_LEVEL_AUTOCOMMIT:", extensions.ISOLATION_LEVEL_AUTOCOMMIT)
    conn.set_isolation_level(autocommit)

    cursor = conn.cursor()

    # 테이블 삭제
    cursor.execute("DROP TABLE IF EXISTS TEMP")
    print("TABLE Deleted successfully...!")

    # 테이블 생성
    SQL_QUERY = '''
        CREATE TABLE {NAME}(
            STATION CHAR(50) NOT NULL, 
            GETON_PPL CHAR(50), 
            GETOFF_PPL CHAR(50)
        )
    '''.format(NAME = TABLE_NAME)
    cursor.execute(SQL_QUERY)
    print("TABLE created successfully........")

    # close the cursor to avoid memory leaks
    cursor.close()

    # Connection Closed to avoid memory leaks
    conn.close()

if __name__ == "__main__":
    main()
```

네 번째 코드(data insert 코드)

```python
import pandas as pd
from psycopg2 import connect, extensions
import psycopg2.extras as extras
import psycopg2
# from sqlalchemy import create_engine

# https://docs.sqlalchemy.org/en/14/core/engines.html
# pip install sqlalchemy

def main():
    # Step 01
    conn = connecting()
    print(conn)
    # createDB(conn)
    # createTable(conn)
    data = pd.DataFrame({
        "STATION": ["합계", "서울역"],
        "GETON_PPL": ["271,214,262", "4,465,118"],
        "GETOFF_PPL": ["52,767,099", "4,205,563"]
    })

    dataInsertPsycopg2(conn, data)
    # dataInsertAlchemy(data)



def connecting():

    # DB connect
    conn = connect(
        host = "localhost",
        dbname = "postgres",
        user = "postgres",
        password = "531014",
        port = "5432"
    )

    # print(conn)
    return conn

def create(conn):
    DB_NAME = "testDB"

    # AutoCommit
    autocommit = extensions.ISOLATION_LEVEL_AUTOCOMMIT
    print("ISOLATION_LEVEL_AUTOCOMMIT:", extensions.ISOLATION_LEVEL_AUTOCOMMIT)
    conn.set_isolation_level(autocommit)

    # 새로운 데이터베이스 생성
    SQL_QUERY = """
        SELECT 'CREATE DATABASE {DB_NAME}'
        WHERE NOT EXISTS (SELECT FROM pg_database WHERE datname = 'testDB')
    """.format(NAME = DB_NAME)

    cursor = conn.cursor()
    cursor.execute(SQL_QUERY)
    print("Database created successfully...!")

    # close the cursor to avoid memory leaks
    cursor.close()

    # Connection Closed to avoid memory leaks
    conn.close()

def createTable(conn):

    TABLE_NAME = "TEMP"

    # AutoCommit
    autocommit = extensions.ISOLATION_LEVEL_AUTOCOMMIT
    print("ISOLATION_LEVEL_AUTOCOMMIT:", extensions.ISOLATION_LEVEL_AUTOCOMMIT)
    conn.set_isolation_level(autocommit)

    cursor = conn.cursor()

    # 테이블 삭제
    cursor.execute("DROP TABLE IF EXISTS TEMP")
    print("TABLE Deleted successfully...!")

    # 테이블 생성
    SQL_QUERY = '''
        CREATE TABLE {NAME}(
            STATION CHAR(50) NOT NULL, 
            GETON_PPL CHAR(50), 
            GETOFF_PPL CHAR(50)
        )
    '''.format(NAME = TABLE_NAME)
    cursor.execute(SQL_QUERY)
    print("TABLE created successfully........")

    # close the cursor to avoid memory leaks
    cursor.close()

    # Connection Closed to avoid memory leaks
    conn.close()

def dataInsertPsycopg2(conn, data):
    # Single Insert
    TABLE_NAME = "TEMP"

    # AutoCommit
    autocommit = extensions.ISOLATION_LEVEL_AUTOCOMMIT
    print("ISOLATION_LEVEL_AUTOCOMMIT:", extensions.ISOLATION_LEVEL_AUTOCOMMIT)
    conn.set_isolation_level(autocommit)

    tuples = [tuple(x) for x in data.to_numpy()]
    # print(tuples)
    '''
    [('합계', '271,214,262', '52,767,099'), ('서울역', '4,465,118', '4,205,563')]
    '''

    cols = ','.join(list(data.columns))
    print(cols) # STATION,GETON_PPL,GETOFF_PPL


    # SQL query to execute
    query = "INSERT INTO %s(%s) VALUES %%s" % (TABLE_NAME, cols)
    print(query)


    cursor = conn.cursor()
    # https://www.psycopg.org/docs/extras.html
    try:
        extras.execute_values(cursor, query, argslist = tuples)
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print("Error: %s" % error)
        conn.rollback()
        cursor.close()
        return 1
    print("the dataframe is inserted")
    cursor.close()
    conn.close()


if __name__ == "__main__":
    main()
```
다섯 번째 코드 (sqlalchemy 코드)

```python
import pandas as pd
from psycopg2 import connect, extensions
import psycopg2.extras as extras
import psycopg2
from sqlalchemy import create_engine

# https://docs.sqlalchemy.org/en/14/core/engines.html
# pip install sqlalchemy

def main():
    # Step 01
    conn = connecting()
    print(conn)
    # createDB(conn)
    # createTable(conn)
    data = pd.DataFrame({
        "STATION": ["합계", "서울역"],
        "GETON_PPL": ["271,214,262", "4,465,118"],
        "GETOFF_PPL": ["52,767,099", "4,205,563"]
    })

    # dataInsertPsycopg2(conn, data)
    dataInsertAlchemy(data)



def connecting():

    # DB connect
    conn = connect(
        host = "localhost",
        dbname = "postgres",
        user = "postgres",
        password = "temp",
        port = "5432"
    )

    # print(conn)
    return conn

def createDB(conn):
    DB_NAME = "testDB"

    # AutoCommit
    autocommit = extensions.ISOLATION_LEVEL_AUTOCOMMIT
    print("ISOLATION_LEVEL_AUTOCOMMIT:", extensions.ISOLATION_LEVEL_AUTOCOMMIT)
    conn.set_isolation_level(autocommit)

    # 새로운 데이터베이스 생성
    SQL_QUERY = """
        SELECT 'CREATE DATABASE {DB_NAME}'
        WHERE NOT EXISTS (SELECT FROM pg_database WHERE datname = 'testDB')
    """.format(DB_NAME = DB_NAME)

    cursor = conn.cursor()
    cursor.execute(SQL_QUERY)
    print("Database created successfully...!")

    # close the cursor to avoid memory leaks
    cursor.close()

    # Connection Closed to avoid memory leaks
    conn.close()

def createTable(conn):

    TABLE_NAME = "TEMP"

    # AutoCommit
    autocommit = extensions.ISOLATION_LEVEL_AUTOCOMMIT
    print("ISOLATION_LEVEL_AUTOCOMMIT:", extensions.ISOLATION_LEVEL_AUTOCOMMIT)
    conn.set_isolation_level(autocommit)

    cursor = conn.cursor()

    # 테이블 삭제
    cursor.execute("DROP TABLE IF EXISTS TEMP")
    print("TABLE Deleted successfully...!")

    # 테이블 생성
    SQL_QUERY = '''
        CREATE TABLE {NAME}(
            STATION CHAR(50) NOT NULL, 
            GETON_PPL CHAR(50), 
            GETOFF_PPL CHAR(50)
        )
    '''.format(NAME = TABLE_NAME)
    cursor.execute(SQL_QUERY)
    print("TABLE created successfully........")

    # close the cursor to avoid memory leaks
    cursor.close()

    # Connection Closed to avoid memory leaks
    conn.close()

def dataInsertPsycopg2(conn, data):
    # Single Insert
    TABLE_NAME = "TEMP"

    # AutoCommit
    autocommit = extensions.ISOLATION_LEVEL_AUTOCOMMIT
    print("ISOLATION_LEVEL_AUTOCOMMIT:", extensions.ISOLATION_LEVEL_AUTOCOMMIT)
    conn.set_isolation_level(autocommit)

    tuples = [tuple(x) for x in data.to_numpy()]
    # print(tuples)
    '''
    [('합계', '271,214,262', '52,767,099'), ('서울역', '4,465,118', '4,205,563')]
    '''

    cols = ','.join(list(data.columns))
    print(cols) # STATION,GETON_PPL,GETOFF_PPL


    # SQL query to execute
    query = "INSERT INTO %s(%s) VALUES %%s" % (TABLE_NAME, cols)
    print(query)


    cursor = conn.cursor()
    # https://www.psycopg.org/docs/extras.html
    try:
        extras.execute_values(cursor, query, argslist = tuples)
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print("Error: %s" % error)
        conn.rollback()
        cursor.close()
        return 1
    print("the dataframe is inserted")
    cursor.close()
    conn.close()

def dataInsertAlchemy(data):
    conn_string = "postgresql://postgres:temp@localhost:5432/testdb"
    engine = create_engine(conn_string)
    conn = engine.connect()
    data.to_sql("temp123", con = conn, if_exists="replace", index=False)
    print("DataFrame is inserted")
    conn = psycopg2.connect(conn_string)
    conn.autocommit = True

if __name__ == "__main__":
    main()
```
마지막 코드는 '에러'가 발생하는데 이를 해결하는건 '개인'의 역량이니 
실습 시 해결해 보길 바란다.
