import requests
import telegram
from bs4 import BeautifulSoup
from apscheduler.schedulers.blocking import BlockingScheduler

bot = telegram.Bot(token='1234556788:AAAAAAAA_BBB2BBB-aABCAbCdE-ASDASS33') # 보안때문에 임의로 바꿔놓음
url = 'http://www.cgv.co.kr/common/showtimes/iframeTheater.aspx?areacode=01&theatercode=0013&date=20210624'

def job_function():
    html = requests.get(url)
    soup = BeautifulSoup(html.text, 'html.parser')
    gold = soup.select_one('span.gold')
    if (gold):
        gold = gold.find_parent('div', class_='col-times')
        title = gold.select_one('div.info-movie > a > strong').text.strip()
        bot.sendMessage(chat_id=745027769, text=title + 'Gold Class 예매가 열렸습니다.')
        sched.pause()
        # print(title + 'Gold Class 예매가 열렸습니다.')
        # print('Gold Class 예매가 열렸습니다.')

sched = BlockingScheduler()
sched.add_job(job_function, 'interval', seconds=30)
sched.start()