# -*- coding: utf-8 -*-
from pytils import numeral
import vk, time, datetime, json, requests, urllib3, dateutil.parser
from captcha_solver import CaptchaSolver

access_token = "ce9e8f522ec975419a465248552e10731e299d87de9d57bd5aeca961cffbdecc40265cbcd5064133346d3"
antigate_token = "TOKEN"

session = vk.Session(access_token=access_token)
api = vk.API(session)
APIVersion = 5.92
chat_users_all={}
message_longpoll = [0]


base={
    'Yes':'No',
}

server = None
key    = None
ts     = None

def requests_image(file_url):
	img_data = requests.get(file_url,verify=False).content
	with open('captcha.jpg', 'wb') as handler:
		handler.write(img_data)

def get_key(d, value):
    for k, v in d.items():
        if v == value:
            return k

def check_dict(word):
    try:
        bike = base[word]
        return bike
    except:
        return 0

def print_(s):
	from pytils.third import six
	if six.PY3:
		out = s
	else:
		out = s.encode('UTF-8')
	return(out)


while True:

	if server == None:
		cfg = api.messages.getLongPollServer(v=APIVersion)
		server = cfg['server']
		key = cfg['key']
		ts = cfg['ts']

	response = requests.post(
		"https://{server}?act=a_check&key={key}&ts={ts}&wait=25&mode={mode}&version=2".format(**{
			"server": server,
            "key": key,
            "ts": ts,
            "mode": 2
        }),
    timeout=30
   	).json()

	now_date = datetime.date.today()
	now_time = datetime.datetime.now()
	day = now_date.isoweekday()
	cur_hour = now_time.hour
	cur_minute = now_time.minute
	cur_second = now_time.second
	cur_month = now_date.month
	cur_day = now_date.day
	for_logs = str(now_time.hour)+':'+str(now_time.minute)+':'+str(now_time.second)
	bb = datetime.date.today()


	for i in range(len(response['updates'])):
		if checker != True:
			try:

				message_longpoll = response['updates'][i][5]
				chat_longpoll = response['updates'][i][3]-2000000000
				checker = True

			except:
				pass
	if checker == False:
		message_longpoll = [0]
		chat_longpoll = [0]

	ts = response['ts']

	if message_longpoll != [0]:

		if check_dict(message_longpoll) != 0:
			api.messages.send(chat_id=chat_longpoll,message=base[message_longpoll],v=APIVersion)
