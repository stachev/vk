#!/usr/bin/ python
from colorama import Fore, Back, Style
import requests
import tok

import vk_api
import random
from vk_api import VkUpload
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.utils import get_random_id
import time
# from colorama import init
# init()
#https://oauth.vk.com/authorize?client_id=7095516&display=page&redirect_uri=https://oauth.vk.com/blank.html&scope=messages,offline&response_type=token&v=5.101'
#https://oauth.vk.com/authorize?client_id=7095516&display=page&redirect_uri=https://oauth.vk.com/blank.html&scope=friends, notifications, photos, video,  messages, groups, wall, audio, offline&response_type=token&v=5.101
token=tok.token()
version= 5.101
domain='krasnymak'
method='notifications.get'

response=requests.get('https://api.vk.com/method/'+method,params={'access_token':token,'v':version})
data=response.json()

def vk():

	vk_session=vk_api.VkApi(token=token)
	session_api=vk_session.get_api()
	longpoll=VkLongPoll(vk_session)
	# session_api=vk_session.auth()
	# print(session_api)
	mes="И тебе привет"
	while True:
		try:
			messages=vk_session.method("messages.getConversations",{'ofset':0, 'count':20,'filter':'unread'})
			if messages['count']>=1:
				user=messages['items'][0]['last_message']['from_id']
				body=messages['items'][0]['last_message']['text']
				if body.lower()=="привет":
					vk_session.method("messages.send",{"peer_id":user, "message":mes,"random_id":random.randint(1,2121212121)})
				elif body.lower()=="кто ты":
					vk_session.method("messages.send",{"peer_id":user, "message":"Я бот","random_id":random.randint(1,2121212121)})
				elif body.lower()=="как тебя зовут":
					vk_session.method("messages.send",{"peer_id":user, "message":"Отвянь от меня","random_id":random.randint(1,2121212121)})
				elif body.lower()=="как дела":
					vk_session.method("messages.send",{"peer_id":user, "message":"Уже лучше","random_id":random.randint(1,2121212121)})
				else:
					vk_session.method("messages.send",{"peer_id":user, "message":'Я ТЕБЯ НЕ ПОНЯЛ',"random_id":random.randint(1,2121212121)})
		except Exception:
			vk_session.method("messages.send",{"peer_id":user, "message":'Я ТЕБЯ НЕ ПОНЯЛ',"random_id":random.randint(1,2121212121)})
			time.sleep(2)


		# print(messages)Я

	# # mesages=vk_session.method("mesages.Getconversation")
	# # vk.auth_token(
	# vk=vk_session.get_api()""
	# longpoll = vk_api.longpoll.VkLongPoll(vk, wait=25, mode=234, preload_messages=False, group_id=185761879)
	# # vk_session.method('messages.send',)
	# # print(vk)


# print(Style.DIM)
# print(Back.RED)#цвет фона 
# print(Fore.GREEN)#цвет текста

# print(type(len(data['response']['items'])))
def wall():
	for i in range(0,len(data['response']['items'])):
		try:
			if data['response']['items'][i]['text']=='':
				print('')
				
			else: 
				# print(Fore.GREEN)

				print(data['response']['items'][i]['text'])
		except:
				a=''
		try:
			# print(Fore.CYAN)
			print(data['response']['items'][i]['attachments'][0]['photo']['sizes'][-1]['url'])
		except:
				a=''

		# print(data['response']['items'][i]['attachments'][0]['photo']['sizes'][-1]['url'])

# print(len(data['response']['items']))

# print(data['response']['items'][0]['attachments'][0]['photo']['sizes'][-1]['url'])

def meseng():
	print(data)


def main():
	# wall()
	# meseng()
	vk()

   




if __name__ == '__main__':
	main()
	# print(tok.token())