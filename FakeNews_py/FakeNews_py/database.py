# 데이터베이스 연결
import pymysql
import pandas as pd

# MariaDB 연결 설정
def create_table():
    conn = pymysql.connect(
        host = 'localhost', # 데이터베이스 주소
        user = 'root', # 사용자 이름
        password = '1234', # 비밀번호
        database = 'sys',
        charset = 'utf8mb4'
    )

    cursor = conn.cursor()

    create_table_query = """
        CREATE TABLE IF NOT EXISTS news (
            id INT AUTO_INCREMENT PRIMARY KEY,
            title VARCHAR(255) NOT NULL,
            content TEXT NOT NULL,
            date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """

    cursor.execute(create_table_query)
    conn.commit()
    conn.close()

create_table()