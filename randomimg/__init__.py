import discord
from random import choice
'''
Try aiohttp when bot reaches 500mb
Make giphy account to store gifs forever
Use this idea:
https://github.com/KingOfPlagues/ViralBot/blob/master/discordbot/utils/util.py
'''
def slap():
	slap_list = [
	'https://media.giphy.com/media/l3vRb8wtvRtW9mOk0/giphy.gif',
	'https://media.giphy.com/media/l1IYa5UYE8iBLWp6E/giphy.gif',
	'https://media0.giphy.com/media/xUPGcF8xjWmt2CRuo0/giphy.gif',
	]
	return choice(slap_list)

def shoot(num: int):
	images = {1 : [
			"http://i.imgur.com/hPL5TGD.gif",
			"https://data.whicdn.com/images/207272964/original.gif"
		],
		 2 : [
			"https://media.giphy.com/media/5xaOcLAo1Gg0oRgBz0Y/giphy.gif",
			"https://i.kym-cdn.com/photos/images/original/000/801/745/825.gif"
		],
		 3 : [
			"https://media.giphy.com/media/5xaOcLAo1Gg0oRgBz0Y/giphy.gif",
			"https://i.kym-cdn.com/photos/images/original/000/801/745/825.gif"
		]}
	return images[num]

		

	
