import discord

# This, randomimg and searchjson were all their own modules

def diceroll(result):
	if result == 1:
		dicepic = 'https://p.kindpng.com/picc/s/244-2448572_dice-clipart-number-one-1-side-of-dice.png'
		return dicepic
	elif result == 2 or result == 3 or result == 4 or result == 5 or result == 6:
		dicepic = f'https://dobbelsteen.virtuworld.net/img/{result}.gif'
		return dicepic
	elif result == 7:
		dicepic = 'https://i.ya-webdesign.com/images/dice-4-png-5.png'
		return dicepic
	elif result == 8:
		dicepic = 'https://i.ya-webdesign.com/images/peach-clipart-face-19.png'
		return dicepic
	elif result == 9:
		dicepic = 'https://upload.wikimedia.org/wikipedia/commons/thumb/e/e0/Dice-9a.svg/557px-Dice-9a.svg.png'
		return dicepic
	elif result == 10:
		dicepic = 'https://upload.wikimedia.org/wikipedia/commons/thumb/3/31/Dice-10.svg/120px-Dice-10.svg.png'
		return dicepic
	elif result == 11:
		dicepic = 'https://images2.sw-cdn.net/product/picture/710x528_205406_224115_1497789822.jpg'
		return dicepic
	elif result == 12:
		dicepic = 'https://www.seekpng.com/png/detail/300-3007396_the-icon-resembles-a-12-sided-dice-shape.png'
		return dicepic
	elif result == 13:
		dicepic = 'https://www.jackofdice.nl/dobbelstenen-los/impact-13-zijdig-zwart/product1.jpg/view.large.jpg'
		return dicepic
	elif result == 14:
		dicepic = 'https://storage.googleapis.com/3d_model_images/396/3961763/d14-sphere-dice-3d-model-R1AGZJX5U_200.jpg'
		return dicepic
	elif result == 15:
		dicepic = 'https://images4.sw-cdn.net/product/picture/290x218_22174908_12406386_1518011869.jpg'
		return dicepic
	elif result == 16:
		dicepic = 'https://storage.googleapis.com/3d_model_images/421/4216440/alt-d16-sphere-dice-3d-model-zl2Dy3Swt_200.jpg'
		return dicepic
	elif result == 17:
		dicepic = 'https://storage.googleapis.com/3d_model_images/396/3962066/d17-sphere-dice-3d-model-FLnzhTfb6_200.jpg'
		return dicepic
	elif result == 18:
		dicepic = 'https://i.pinimg.com/originals/fb/04/5f/fb045f53d00ec8f95f6a7f77a4ebdc26.jpg'
		return dicepic
	elif result == 19:
		dicepic = 'https://images3.sw-cdn.net/product/picture/710x528_4399453_368146_1459315230.jpg'
		return dicepic
	elif result == 20:
		dicepic = 'https://geekandsundry.com/wp-content/uploads/2015/10/d20.jpg'
		return dicepic
	else:
		dicepic = None
		return dicepic

