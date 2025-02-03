# 데이터베이스 연결
import pymysql
import pandas as pd

# MariaDB 연결 설정
conn = pymysql.connect(
    host = 'localhost', # 데이터베이스 주소
    user = 'root', # 사용자 이름
    password = '1234', # 비밀번호
    database = 'fake_news',
    charset = 'utf8mb4'
)

# SQL 쿼리 실행
query = "SELECT id, title, content, label FROM articles" # 테이블 이름과 컬럼 수정
data = pd.read_sql(query, conn)

# 데이터 확인
print(data.head())

# 연결 종료
conn.close()