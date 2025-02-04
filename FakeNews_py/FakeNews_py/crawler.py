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
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, "html.parser")

        # 뉴스 제목 추출 (사이트 구조에 따라 변경 필요)
        title = soup.find("h1").get_text(strip=True) if soup.find("h1") else "제목 없음"

        # 뉴스 본문 추출
        paragraphs = soup.find_all("p")
        content = "\n".join([p.get_text(strip=True) for p in paragraphs if p.get_text(strip=True)])

        return {"title": title, "content": content}

    except requests.exceptions.RequestException as e:
        print(f"오류 발생: {e}")
        return None