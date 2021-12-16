import requests


url="https://github.com/lovelyAlien"
headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"}
# res=requests.get("https://github.com/lovelyAlien")
res=requests.get(url, headers=headers)



print("응답 코드 : ", res.status_code)


# if res.status_code==requests.codes.ok:
#     print("정상")
# else: 
#     print("문제 발생. [에러코드 ",res.status_code, " ]")


res.raise_for_status() # 웹 스크래핑을 위해 올바른 html 코드를 가져왔는지 확인. 작동 성공하면 다음 코드 실행
print("정상")

print(len(res.text))


with open("mygithub.html", "w", encoding="utf8") as f: 
    f.write(res.text)# 스크래핑 코드 파일 만듦 



