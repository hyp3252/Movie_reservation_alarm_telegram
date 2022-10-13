import telegram
bot = telegram.Bot(token='1234556788:AAAAAAAA_BBB2BBB-aABCAbCdE-ASDASS33') # 보안때문에 임의로 가려놓음

# for i in bot.getUpdates():
#     print(i)

bot.sendMessage(chat_id=745027769, text='이것은 테스트')