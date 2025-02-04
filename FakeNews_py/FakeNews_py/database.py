# 데이터베이스 연결
import pymysql
import pandas as pd
import pymysql.cursors

# MariaDB 연결 설정
DB_CONFIG = {
    "host": "localhost",      # 데이터베이스 주소
    "user": "root",           # 사용자 이름
    "password": "1234",       # 비밀번호
    "database": "sys",        # 사용할 데이터베이스 이름
    "charset": "utf8mb4"
}

# 데이터베이스 테이블 생성
def create_table():
    """
    news 테이블 생성 함수
    """
    conn = pymysql.connect(**DB_CONFIG)
    cursor = conn.cursor()
    
    create_table_query = """
    CREATE TABLE IF NOT EXISTS news (
        id INT AUTO_INCREMENT PRIMARY KEY,
        title VARCHAR(255) NOT NULL,
        content TEXT NOT NULL,
        data TIMESTAMP DEFAULT CURREENT_TIMESTAMP
    )
    """
    cursor.execute(create_table_query)
    conn.commit()
    conn.close()

# 데이터 저장
def save_news_to_db(title, content):
    """
    뉴스 데이터를 MariaDB에 저장하는 함수
    """
    conn = pymysql.connect(**DB_CONFIG)
    cursor = conn.cursor()
    
    insert_query = "INSERT INTO news (title, content) VALUES (%s, %s)"
    cursor.execute(insert_query, (title, content))
    
    conn.commit()
    conn.close()
    
# 데이터 불러오기
def fetch_all_news():
    """
    데이터베이스에서 모든 뉴스 데이터를 가져오는 함수
    :return: [{"id}: 1, "title": "제목1", "content": "내용1", "date": "2023-01-01"}, ...]
    """
    conn = pymysql.connect(**DB_CONFIG)
    cursor = conn.cursor(pymysql.cursors.DictCursor) # 결과를 딕셔너리 형태로 반환
    
    select_query = "SELECT * FROM news"
    cursor.execute(select_query)
    results = cursor.fetchall()
    
    conn.close()
    return results

# 테이블 생성(한 번만 수행됨)
create_table()