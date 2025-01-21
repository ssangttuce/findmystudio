import requests

cookies = {
    'NNB': '3AJGDW7D4MOGM',
    'page_uid': 'i3UkBdqo1awsslVyhcCssssssSC-101215',
    'landHomeFlashUseYn': 'Y',
    'ba.uuid': '0',
    'NDV_SHARE': 'SEqwKe5IlPymiuRJ69ZA4KGub3Ao1ejNzIcMODTWFTxL5YwP6MEeJR9U6JZZ4460vs9aBoYOL8MAJjH2llNaSc7Nmv/DTLaYP6l+mQwZiucK',
    'nid_inf': '85052801',
    'NID_JKL': 'VPNNXxpLtIKcebM07xPaQJHtYzdx4mayO74CiANKWOw=',
    'nhn.realestate.article.rlet_type_cd': 'Z03',
    'nhn.realestate.article.trade_type_cd': 'B2',
    'BUC': 'CU0s-8w3zSKzwDgc2uw73cha1vxxgPRPBFIA9nv0KuI=',
    'REALESTATE': 'Tue%20Jan%2021%202025%2016%3A05%3A47%20GMT%2B0900%20(Korean%20Standard%20Time)',
}

headers = {
    'accept': '*/*',
    'accept-language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
    'authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IlJFQUxFU1RBVEUiLCJpYXQiOjE3Mzc0NDMxNDcsImV4cCI6MTczNzQ1Mzk0N30.VNrNahB0DTN9XfdcxSlpPpG1uX0vzKYsTmchanD2drM',
    # 'cookie': 'NNB=3AJGDW7D4MOGM; page_uid=i3UkBdqo1awsslVyhcCssssssSC-101215; landHomeFlashUseYn=Y; ba.uuid=0; NDV_SHARE=SEqwKe5IlPymiuRJ69ZA4KGub3Ao1ejNzIcMODTWFTxL5YwP6MEeJR9U6JZZ4460vs9aBoYOL8MAJjH2llNaSc7Nmv/DTLaYP6l+mQwZiucK; nid_inf=85052801; NID_JKL=VPNNXxpLtIKcebM07xPaQJHtYzdx4mayO74CiANKWOw=; nhn.realestate.article.rlet_type_cd=Z03; nhn.realestate.article.trade_type_cd=B2; BUC=CU0s-8w3zSKzwDgc2uw73cha1vxxgPRPBFIA9nv0KuI=; REALESTATE=Tue%20Jan%2021%202025%2016%3A05%3A47%20GMT%2B0900%20(Korean%20Standard%20Time)',
    'dnt': '1',
    'priority': 'u=1, i',
    'referer': 'https://new.land.naver.com/rooms?ms=37.30117,127.048381,16&a=APT:OPST:ABYG:OBYG:GM:OR:VL:DDDGG:JWJT:SGJT:HOJT&b=B1:B2&d=70&e=RETAIL&g=3500&aa=SMALLSPCRENT&ae=ONEROOM',
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36',
}

response = requests.get(
    'https://new.land.naver.com/api/articles?cortarNo=4111710300&order=rank&realEstateType=APT%3AOPST%3AABYG%3AOBYG%3AGM%3AOR%3AVL%3ADDDGG%3AJWJT%3ASGJT%3AHOJT&tradeType=B1%3AB2&tag=%3A%3A%3A%3A%3A%3A%3ASMALLSPCRENT%3AONEROOM&rentPriceMin=0&rentPriceMax=70&priceMin=0&priceMax=3500&areaMin=0&areaMax=900000000&oldBuildYears&recentlyBuildYears&minHouseHoldCount&maxHouseHoldCount&showArticle=false&sameAddressGroup=false&minMaintenanceCost&maxMaintenanceCost&priceType=RETAIL&directions=&page=5&articleState',
    cookies=cookies,
    headers=headers,
)