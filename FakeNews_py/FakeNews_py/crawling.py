from database import save_news_to_db
from crawling import get_news_data

# 테스트 URL
news_url = "https://n.news.naver.com/mnews/article/003/0013046707?sid=101"
news_data = get_news_data(news_url)

if news_data:
    print("뉴스 제목: ", news_data["title"])
    print("뉴스 내용: ", news_data["content"])
    save_news_to_db(news_data["title"], news_data["content"]) # 데이터 저장
    print("데이터 저장 완료!")
else:
    print("크롤링 실패!")