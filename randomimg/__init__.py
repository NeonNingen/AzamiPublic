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
	if num == 1:
		gif_list = [
		"http://i.imgur.com/hPL5TGD.gif",
		"https://data.whicdn.com/images/207272964/original.gif"
		]
		return choice(gif_list)
	elif num == 2:
		gif_list = [
		"https://media.giphy.com/media/5xaOcLAo1Gg0oRgBz0Y/giphy.gif",
		"https://i.kym-cdn.com/photos/images/original/000/801/745/825.gif"
		] # Finish these
		return choice(gif_list)
	elif num == 3:
		gif_list = [
		"https://s-media-cache-ak0.pinimg.com/originals/2d/fa/a9/2dfaa995a09d81a07cad24d3ce18e011.gif",
		"https://i.imgur.com/W3MY1.gif",
		"https://media.giphy.com/media/VuKsgBXgjOUtW/giphy.gif"
		]
		return choice(gif_list)

		

	