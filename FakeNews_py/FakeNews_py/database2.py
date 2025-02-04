import pymysql

DB_CONFIG = {
    "host": "localhost",
    "user": "root",  # MariaDB 사용자 이름
    "password": "1234",  # MariaDB 비밀번호
    "database": "sys",  # 'sys' 데이터베이스에 연결
    "charset": "utf8mb4"
}

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
        date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """
    cursor.execute(create_table_query)
    conn.commit()
    conn.close()

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
