# 한 페이지 크롤링
import requests
from bs4 import BeautifulSoup

def get_news_data(url):
    """
    주어진 뉴스 URL에서 제목과 본문을 크롤링하는 함수
    :param url: 뉴스 기사 URL
    :return: {'title': 제목, 'content': 본문}
    """
    headers = {"User-Agent": "Mozilla/5.0"}
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # HTTP 오류 발생 시 예외 처리
        
        soup = BeautifulSoup(response.text, "html.parser")

        # 뉴스 제목 추출 (사이트별로 태그가 다를 수 있음)
        title = soup.find("h1").get_text(strip=True) if soup.find("h1") else "제목 없음"

        # 뉴스 본문 추출 (사이트별로 태그가 다를 수 있음)
        paragraphs = soup.find_all("p")
        content = "\n".join([p.get_text(strip=True) for p in paragraphs if p.get_text(strip=True)])

        return {"title": title, "content": content}

    except requests.exceptions.RequestException as e:
        print(f"오류 발생: {e}")
        return None

# 테스트할 뉴스 URL (실제 사용할 뉴스 사이트 URL로 변경 필요)
news_url = "https://n.news.naver.com/mnews/article/001/0012958103/"
news_data = get_news_data(news_url)

if news_data:
    print("뉴스 제목:", news_data["title"])
    print("뉴스 내용:", news_data["content"])
else:
    print("크롤링 실패!")