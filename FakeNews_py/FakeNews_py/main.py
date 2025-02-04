from crawler import get_news_data
from database import create_table, save_news_to_db

def main():
    # 테이블 생성
    create_table()

    # 테스트할 뉴스 URL (사이트에 맞게 변경 필요)
    news_url = "https://n.news.naver.com/mnews/article/001/0012958103/"

    # 뉴스 데이터 크롤링
    news_data = get_news_data(news_url)
    
    if news_data:
        # MariaDB에 저장
        save_news_to_db(news_data["title"], news_data["content"])
        print(f"저장 완료: {news_data['title']}")
    else:
        print("크롤링 실패!")

if __name__ == "__main__":
    main()
