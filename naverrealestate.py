import csv
import requests
from datetime import datetime
import os

# Cookies and headers 설정
cookies = {
    'NNB': '3AJGDW7D4MOGM',
    'page_uid': 'i3UkBdqo1awsslVyhcCssssssSC-101215',
    'landHomeFlashUseYn': 'Y',
    'ba.uuid': '0',
    'NDV_SHARE': 'SEqwKe5IlPymiuRJ69ZA4KGub3Ao1ejNzIcMODTWFTxL5YwP6MEeJR9U6JZZ4460vs9aBoYOL8MAJjH2llNaSc7Nmv/DTLaYP6l+mQwZiucK',
    'nid_inf': '85052801',
    'NID_JKL': 'VPNNXxpLtIKcebM07xPaQJHtYzdx4mayO74CiANKWOw=',
    'BUC': 'CL9GbSx5fk1DrWTIyyIYi1CX3YFtplnOgnliSWNNPwA=',
    'nhn.realestate.article.rlet_type_cd': 'Z03',
    'nhn.realestate.article.trade_type_cd': 'B2',
    'REALESTATE': 'Tue%20Jan%2021%202025%2014%3A30%3A35%20GMT%2B0900%20(Korean%20Standard%20Time)',
}

headers = {
    'accept': '*/*',
    'accept-language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
    'authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IlJFQUxFU1RBVEUiLCJpYXQiOjE3Mzc0Mzc0MzUsImV4cCI6MTczNzQ0ODIzNX0.Q-MT6Nscb2OmUEEMWx5nyfX6Dlsb2j1m_q6THmEOhwk',
    'dnt': '1',
    'priority': 'u=1, i',
    'referer': 'https://new.land.naver.com/rooms?ms=37.2905873,127.0468745,17&a=APT:OPST:ABYG:OBYG:GM:OR:VL:DDDGG:JWJT:SGJT:HOJT&b=B1:B2&d=70&e=RETAIL&g=3500&aa=SMALLSPCRENT&ae=ONEROOM',
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36',
}

# 현재 날짜와 시간 설정
now = datetime.now()
formatted_date = now.strftime("%Y%m%d_%H%M%S")

# 저장 경로 설정
output_dir = "./studiolist"
os.makedirs(output_dir, exist_ok=True)

csv_file = os.path.join(output_dir, f"{formatted_date}.csv")

fieldnames = [
    "articleNo", "articleName", "realEstateTypeName", "tradeTypeName", "floorInfo",
    "rentPrc", "dealOrWarrantPrc", "area1", "area2", "direction", "articleFeatureDesc",
    "latitude", "longitude", "realtorName"
]

with open(csv_file, mode="w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()

    for page in range(1, 11):
        url = f'https://new.land.naver.com/api/articles?markerId=2120310212103&markerType=LGEOHASH_MIX_ARTICLE&order=rank&realEstateType=APT%3AOPST%3AABYG%3AOBYG%3AGM%3AOR%3AVL%3ADDDGG%3AJWJT%3ASGJT%3AHOJT&tradeType=B1%3AB2&tag=%3A%3A%3A%3A%3A%3A%3ASMALLSPCRENT%3AONEROOM&rentPriceMin=0&rentPriceMax=70&priceMin=0&priceMax=3500&areaMin=0&areaMax=900000000&oldBuildYears&recentlyBuildYears&minHouseHoldCount&maxHouseHoldCount&showArticle=false&sameAddressGroup=false&minMaintenanceCost&maxMaintenanceCost&priceType=RETAIL&directions=&page={page}&articleState'

        # API 요청
        response = requests.get(url, cookies=cookies, headers=headers)
        data = response.json()
        article_list = data.get("articleList", [])

        for article in article_list:
            writer.writerow({
                "articleNo": article.get("articleNo"),
                "articleName": article.get("articleName"),
                "realEstateTypeName": article.get("realEstateTypeName"),
                "tradeTypeName": article.get("tradeTypeName"),
                "floorInfo": article.get("floorInfo"),
                "rentPrc": article.get("rentPrc"),
                "dealOrWarrantPrc": article.get("dealOrWarrantPrc"),
                "area1": article.get("area1"),
                "area2": article.get("area2"),
                "direction": article.get("direction"),
                "articleFeatureDesc": article.get("articleFeatureDesc"),
                "latitude": article.get("latitude"),
                "longitude": article.get("longitude"),
                "realtorName": article.get("realtorName"),
            })

print(f"CSV 파일이 '{csv_file}' 이름으로 저장되었습니다.")
