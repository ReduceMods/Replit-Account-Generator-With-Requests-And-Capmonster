import requests
import random
from colorama import Fore, Back, Style
from colorama import Fore as fg, Back as bg, Style as st

from capmonster_python import HCaptchaTask




capmonster_key = "Add Your Capmonster Key Here"

url = 'https://replit.com/signup'
site_key = "a20d9b66-6747-404a-9393-c449c4611661"


capmonster = HCaptchaTask(capmonster_key)
task_id = capmonster.create_task(url, site_key)
result = capmonster.join_task_result(task_id)
print(Fore.RESET + f'{Fore.LIGHTYELLOW_EX}[+] Solved Captcha...')




usernameRandom = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz1234567890', k=7))




email1 = open('Emails.txt','r')
email2 = email1.readlines()
email3 = random.choice(email2)
email = email3.strip('\n')


password = "ufyufd_dYJ7FH!h"

def replitGen():
        try:
            
                secemail = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=7)) + "@yahoo.com"
                password1 = 'ufyufd_dYJ7FH!h'
                payload = {
                    "email": f"{email}",
                    "password": f"{password1}",
                    "username": f'{usernameRandom}', 
                    "teacher": False,
                    "source": "explicit",
                    "organization": "",
                    "hCaptchaSiteKey": "a20d9b66-6747-404a-9393-c449c4611661",
                    "hCaptchaResponse": result.get("gRecaptchaResponse")
                }

                headers = {
                    "accept": "application/json",
                    "accept-encoding": "gzip, deflate, br",
                    "accept-language": "en-GB,en;q=0.9",
                    "content-length": "1938",
                    "content-type": "application/json",
                    "cookie": "replit_ng=1655042659.548.79.668986|8035451343a2d8f3e54599c71b2aec19; _anon_id=3a5a8bd0-a971-4e9f-9fa0-d1c70a5a5b10; connect.sid=s%3AjRg_FqLPxajcmEg-BBX69m9fCh9FAJLL.YWxRsA7qtOZxtj%2Fq57PZmNh6DVgdksKgZbMEaLOwdAI; amplitudeSessionId=1655042658; __hstc=205638156.294b2346a0f70aabce98c343ddc09713.1655042658594.1655042658594.1655042658594.1; hubspotutk=294b2346a0f70aabce98c343ddc09713; __hssrc=1; __hssc=205638156.1.1655042658594; ajs_anonymous_id=14dd48a2-f224-41b9-9ff8-3c2fd5dfcea5; _ga=GA1.2.1411639562.1655042659; _gid=GA1.2.1013620272.1655042659; __stripe_mid=2255a7bc-afa8-4783-a855-7df2dd21b4b40afa81; __stripe_sid=36023fa9-8677-49ef-a8bc-e25a762eff92c5686a; _gat=1; _dd_s=logs=1&id=a4172b31-8393-4337-b5be-bcac82ed8ac5&created=1655042658184&expire=1655043670538",
                    "origin": "https://replit.com",
                    "referer": "https://replit.com/signup?goto=%2Frepls",
                    "sec-ch-ua-mobile": "?0",
                    "sec-ch-ua-platform": "Windows",
                    "sec-fetch-dest": "empty",
                    "sec-fetch-mode": "cors",
                    "sec-fetch-site": "same-origin",
                    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36",
                    "x-requested-with": "XMLHttpRequest"
                }
                r = requests.post(url,headers=headers,json=payload)
                logs1 = open('logs.txt','w')
                logs1.write(f'{r.text}\n')
                print(Fore.LIGHTGREEN_EX + f'Generated Account | {usernameRandom} | {password}')

                w = open('accounts.txt','a+')
                w.write({usernameRandom} | {secemail} | {password} + str('\n'))
                w2 = open('user_pass.txt','a+')
                w2.write(f'{usernameRandom} | {password}\n')
        except Exception as e:
            print(e)


replitGen()