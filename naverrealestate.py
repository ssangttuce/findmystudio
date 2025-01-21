import csv
import requests
from datetime import datetime
import os

# Cookies와 Headers 설정
cookies = {
    'NNB': '3AJGDW7D4MOGM',
    'page_uid': 'i3UkBdqo1awsslVyhcCssssssSC-101215',
    'landHomeFlashUseYn': 'Y',
    'ba.uuid': '0',
    'NDV_SHARE': 'SEqwKe5IlPymiuRJ69ZA4KGub3Ao1ejNzIcMODTWFTxL5YwP6MEeJR9U6JZZ4460vs9aBoYOL8MAJjH2llNaSc7Nmv/DTLaYP6l+mQwZiucK',
    'nid_inf': '85052801',
    'NID_JKL': 'VPNNXxpLtIKcebM07xPaQJHtYzdx4mayO74CiANKWOw=',
    'BUC': 'CL9GbSx5fk1DrWTIyyIYi1CX3YFtplnOgnliSWNNPwA=',
    'REALESTATE': 'Tue%20Jan%2021%202025%2014%3A30%3A35%20GMT%2B0900%20(Korean%20Standard%20Time)',
}

headers = {
    'accept': '*/*',
    'accept-language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
    'authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IlJFQUxFU1RBVEUiLCJpYXQiOjE3Mzc0Mzc0MzUsImV4cCI6MTczNzQ0ODIzNX0.Q-MT6Nscb2OmUEEMWx5nyfX6Dlsb2j1m_q6THmEOhwk',
    'dnt': '1',
    'priority': 'u=1, i',
    'referer': 'https://new.land.naver.com/rooms',
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36',
}

# 동 정보 가져오기
def fetch_region_list():
    params = {'cortarNo': '4111700000'}
    response = requests.get(
        'https://new.land.naver.com/api/regions/list',
        params=params,
        cookies=cookies,
        headers=headers
    )
    data = response.json()
    return data.get("regionList", [])

# 부동산 검색 및 CSV 저장
def fetch_real_estate(cortarNo, dong_name, rent_min, rent_max, price_min, price_max):
    now = datetime.now()
    formatted_date = now.strftime("%Y%m%d_%H%M%S")
    output_dir = "./studiolist"
    os.makedirs(output_dir, exist_ok=True)
    csv_file = os.path.join(output_dir, f"{formatted_date}_{dong_name}.csv")

    fieldnames = [
        "articleNo", "articleName", "realEstateTypeName", "tradeTypeName", "floorInfo",
        "rentPrc", "dealOrWarrantPrc", "area1", "area2", "direction", "articleFeatureDesc",
        "latitude", "longitude", "realtorName"
    ]

    with open(csv_file, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()

        for page in range(1, 11):
            url = (
                f'https://new.land.naver.com/api/articles?cortarNo={cortarNo}'
                f'&order=rank&realEstateType=APT%3AOPST%3AABYG%3AOBYG%3AGM%3AOR%3AVL%3ADDDGG%3AJWJT%3ASGJT%3AHOJT'
                f'&tradeType=B1%3AB2&tag=%3A%3A%3A%3A%3A%3A%3ASMALLSPCRENT%3AONEROOM'
                f'&rentPriceMin={rent_min}&rentPriceMax={rent_max}&priceMin={price_min}&priceMax={price_max}'
                f'&areaMin=0&areaMax=900000000&oldBuildYears&recentlyBuildYears'
                f'&minHouseHoldCount&maxHouseHoldCount&showArticle=false'
                f'&sameAddressGroup=false&minMaintenanceCost&maxMaintenanceCost'
                f'&priceType=RETAIL&directions=&page={page}&articleState'
            )

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

# 실행 로직
region_list = fetch_region_list()
if region_list:
    print("4111700000에 속한 동 목록:")
    for idx, region in enumerate(region_list, start=1):
        print(f"{idx}. {region['cortarName']}")

    try:
        choice = int(input("조회할 동의 번호를 입력하세요: "))
        if 1 <= choice <= len(region_list):
            selected_region = region_list[choice - 1]
            print(f"선택한 동: {selected_region['cortarName']}")

            # 사용자 입력: 월세와 보증금 범위
            rent_min = input("최소 월세를 입력하세요 (기본값: 0): ") or "0"
            rent_max = input("최대 월세를 입력하세요 (기본값: 무제한): ") or "900000000"
            price_min = input("최소 보증금을 입력하세요 (기본값: 0): ") or "0"
            price_max = input("최대 보증금을 입력하세요 (기본값: 무제한): ") or "900000000"

            fetch_real_estate(
                selected_region['cortarNo'],
                selected_region['cortarName'],
                rent_min,
                rent_max,
                price_min,
                price_max
            )
        else:
            print("잘못된 번호를 입력하셨습니다.")
    except ValueError:
        print("유효한 숫자를 입력하세요.")
else:
    print("동 목록을 가져오지 못했습니다.")
