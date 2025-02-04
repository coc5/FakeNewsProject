import requests
from bs4 import BeautifulSoup
import pymysql

# ---------------------- 개별 뉴스 기사 크롤링 ----------------------
def get_news_data(url):
    headers = {"User-Agent": "Mozilla/5.0"}
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, "html.parser")

        # 뉴스 제목 가져오기 (사이트마다 다를 수 있음)
        title = soup.find("h1").get_text(strip=True) if soup.find("h1") else "제목 없음"

        # 뉴스 본문 가져오기
        paragraphs = soup.find_all("p")
        content = "\n".join([p.get_text(strip=True) for p in paragraphs if p.get_text(strip=True)])

        return {"title": title, "content": content}

    except requests.exceptions.RequestException as e:
        print(f"오류 발생: {e}")
        return None

# ---------------------- 뉴스 목록에서 기사 링크 가져오기 ----------------------
def get_news_links(news_list_url):
    headers = {"User-Agent": "Mozilla/5.0"}
    
    try:
        response = requests.get(news_list_url, headers=headers)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, "html.parser")

        # 뉴스 기사 링크 추출 (사이트별로 class 값 수정 필요)
        links = [a["href"] for a in soup.find_all("a", class_="news-title")]

        return links

    except requests.exceptions.RequestException as e:
        print(f"오류 발생: {e}")
        return []
