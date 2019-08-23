#!/usr/bin/ python

import pyowm
import datetime


now = datetime.datetime.now()

owm = pyowm.OWM('1e25f90d78f5e77120dde7e04d0dd73b',language='ru')

siti='Красный Мак'
# siti=input('Город? :')

# Have a pro subscription? Then use:
# owm = pyowm.OWM(API_key='your-API-key', subscription_type='pro')

# Search for current weather in London (Great Britain)

observation = owm.weather_at_place(siti)
w = observation.get_weather()
ww=w.get_temperature('celsius')

# s=str(w)
# print(siti+'\n'+s.split(',')[-1].split('=')[-1].split('>')[0])
# # print(ww)
# print(ww['temp'],' по цельсию')
def pogoda():
	fc=owm.three_hours_forecast(siti)#на 5 дней
	# fc=owm.daily_forecast(siti,limit=6)#на 14 дней
	f = fc.get_forecast()
	dat=f.get_weathers()

	# print('\n',str(dat[0]).split(' ')[3].split('=')[-1],'\n',str(dat[0]).split(' ')[4].split(':')[0],': 00 Будет ',str(dat[0]).split(' ')[-1].split('=')[-1])
	for i in range(0,len(f.get_weathers())):
		print('\n',str(dat[i]).split(' ')[3].split('=')[-1],'\n',str(dat[i]).split(' ')[4].split(':')[0],': 00 Будет ',str(dat[i]).split(' ')[-1].split('=')[-1])


def test():
	s=str(w)
	a=siti+'\n'+s.split(',')[-1].split('=')[-1].split('>')[0]
	b=ww['temp']
	time=str(now).split(' ')[0]
	fc=owm.three_hours_forecast(siti)#на 5 дней
	f = fc.get_forecast()
	dat=f.get_weathers()
	# for i in range(0,len(f.get_weathers())):
	# 	if str(dat[i]).split(' ')[3].split('=')[-1]==time:
	# 		# print('\n',str(dat[i]).split(' ')[4].split(':')[0],': 00 Будет ',str(dat[i]).split(' ')[-1].split('=')[-1])
	# 		return '\n',str(dat[i]).split(' ')[4].split(':')[0],': 00 Будет ',str(dat[i]).split(' ')[-1].split('=')[-1]
	return a+'\t'+str(b)
time=str(now).split(' ')[0]
def main():
	# pogoda()
	# print (time)
	print(test())
def tab():
    for i in range(0,20):
        print(i)



if __name__ == '__main__':
	main()
