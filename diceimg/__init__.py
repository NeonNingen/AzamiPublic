import discord

# This, randomimg and searchjson were all their own modules

def diceroll(result):
	results = {1 : 'https://p.kindpng.com/picc/s/244-2448572_dice-clipart-number-one-1-side-of-dice.png', 
		   7 : 'https://i.ya-webdesign.com/images/dice-4-png-5.png', 
		   8 : 'https://i.ya-webdesign.com/images/peach-clipart-face-19.png',
		   9 : 'https://upload.wikimedia.org/wikipedia/commons/thumb/e/e0/Dice-9a.svg/557px-Dice-9a.svg.png',
		   10 : 'https://upload.wikimedia.org/wikipedia/commons/thumb/3/31/Dice-10.svg/120px-Dice-10.svg.png',
		   11 : 'https://images2.sw-cdn.net/product/picture/710x528_205406_224115_1497789822.jpg',
		   12 : 'https://www.seekpng.com/png/detail/300-3007396_the-icon-resembles-a-12-sided-dice-shape.png',
		   13 : 'https://www.jackofdice.nl/dobbelstenen-los/impact-13-zijdig-zwart/product1.jpg/view.large.jpg',
		   14 : 'https://storage.googleapis.com/3d_model_images/396/3961763/d14-sphere-dice-3d-model-R1AGZJX5U_200.jpg',
		   15 : 'https://images4.sw-cdn.net/product/picture/290x218_22174908_12406386_1518011869.jpg',
		   16 : 'https://storage.googleapis.com/3d_model_images/421/4216440/alt-d16-sphere-dice-3d-model-zl2Dy3Swt_200.jpg',
		   17 : 'https://storage.googleapis.com/3d_model_images/396/3962066/d17-sphere-dice-3d-model-FLnzhTfb6_200.jpg',
		   18 : 'https://i.pinimg.com/originals/fb/04/5f/fb045f53d00ec8f95f6a7f77a4ebdc26.jpg',
		   19 : 'https://images3.sw-cdn.net/product/picture/710x528_4399453_368146_1459315230.jpg',
		   20 : 'https://geekandsundry.com/wp-content/uploads/2015/10/d20.jpg'}
	
	if 1 < result < 7:
		dicepic = f'https://dobbelsteen.virtuworld.net/img/{result}.gif'
	elif result 0 < result < 21:
		dicepic = results[result]
	else:
		dicepic = None
		
	return dicepic

