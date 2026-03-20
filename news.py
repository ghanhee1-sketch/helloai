import requests
from bs4 import BeautifulSoup

def get_realtime_weather():
    # 1. 사용자 입력 (예: 인천, 강남구, 제주도)
    location = input("어느 지역의 날씨가 궁금하신가요? : ").strip()
    if not location:
        return

    # 2. 네이버 검색 URL 생성
    url = f"https://search.naver.com/search.naver?query={location}+날씨"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"
    }

    try:
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, "html.parser")

        # 3. 데이터 추출 (가장 안정적인 클래스명 사용)
        # 현재 온도
        temp = soup.select_one(".temperature_text strong")
        # 날씨 상태 (맑음, 흐림 등)
        summary = soup.select_one(".before_slash")
        # 미세먼지 상태
        dust = soup.select(".today_chart_list .txt") 

        if temp and summary:
            print(f"\n📍 [{location}] 실시간 날씨 보고서")
            print(f"🌡️ 현재 온도: {temp.get_text(strip=True).replace('현재 온도', '')}")
            print(f"☁️ 날씨 상태: {summary.get_text(strip=True)}")
            
            if dust:
                print(f"😷 미세먼지: {dust[0].get_text(strip=True)}")
            print("-" * 30)
        else:
            print(f"❌ '{location}'의 날씨 정보를 찾을 수 없습니다. 지역명을 다시 확인해 주세요.")

    except Exception as e:
        print(f"⚠️ 연결 오류가 발생했습니다: {e}")

if __name__ == "__main__":
    get_realtime_weather()
    
