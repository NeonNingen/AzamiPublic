import discord, sys, io
from discord.ext import commands
from discord.ext.commands import MissingRequiredArgument
from random import choice, randint
from asyncio import sleep
sys.path.insert(1, '../')
import randomimg

# This cog is also a mess xD

def to_upper(argument):
	return argument.upper()

class Fun(commands.Cog):

	def __init__(self, azami):
		self.azami = azami

	class Slapper(commands.Converter):
		async def convert(self, ctx, argument):
			to_slap = choice(ctx.guild.members)
			return f'{ctx.author} slapped {to_slap} because *{argument}*'

	@commands.command(description="It's your fault!")
	async def blame(self, ctx, *, reason: Slapper):
		await ctx.send(reason)

	@commands.command(description='This is gonna hurt!')
	async def slap(self, ctx, user):
		embed = discord.Embed(
			title = "That hurts!",
			description = f"{ctx.author.mention} slapped {user}",
			colour = discord.Color.dark_red())
		embed.set_image(url = randomimg.slap())
		await ctx.send(embed=embed)

	@commands.command(name='8 or 8ball', aliases=['8ball', '8'], 
					  description='What answers do you seek?',
					  usage='Have your questions answered!')
	async def _8ball(self, ctx, *, question):
		with open('cogs/responses_fun.txt', 'r') as f:
			responses = f.read().splitlines()
			# When rehauling use folders for each cog
		await ctx.send(f"Questions: {question}\nAnswer: {choice(responses)}")

	@commands.command(description='azami -> AZAMI',
					  usage='Basically capitalizes anything you say')
	async def up(self, ctx, *, content: to_upper):
		await ctx.send(content)

	@commands.command(description='Bang and the dirt is gone',
					  usage='You can suicide, shoot others or shoot Azami!')
	async def shoot(self, ctx, *members: discord.Member):
		if not members: # Built in error check
			await ctx.send("You gotta give me someone to shoot!")
			return
		for member in members:
			if member == self.azami.user:
				embed = discord.Embed(
					title = "Dodged it!",
					description = f"You attempted to shoot me {ctx.author.mention}, but I dodged it!",
					colour = discord.Color.green())
				embed.set_image(url = randomimg.shoot(1))
				await ctx.send(embed=embed)
			elif member == ctx.author:
				embed = discord.Embed(
					title = "You died! Better luck next time!",
					description = f"{ctx.author.name} committed suicide!",
					colour = discord.Color.red())
				embed.set_image(url = randomimg.shoot(2))
				await ctx.send(embed=embed)
			else:
				embed = discord.Embed(
					title = "It's a hit!",
					description = f"{member.name} was shot dead by the mighty {ctx.author.name}",
					colour = discord.Color.gold())
				embed.set_image(url = randomimg.shoot(3))
				await ctx.send(embed=embed)

	@commands.command(description='And your next line is!')
	async def say(self, ctx, *, content):
		await ctx.send(content)

	@commands.command(description="Let's play a game of Jan Ken Pon!",
					  aliases=['rockpaperscissors', 'rock'])
	async def rps(self, ctx):
		hello_em = discord.Embed(title=f"Hello {ctx.message.author.name}",
								 description="Let's play Rock, paper, scissors!",
								 color=discord.Color.green())
		hello_em.set_image(url='https://media1.giphy.com/media/xUOwFX9O1080yxFDk4/source.gif')
		hello_em.set_thumbnail(url=ctx.message.author.avatar_url)
		hello_em.set_footer(text="Your opponent is me!",
							   icon_url=self.azami.user.avatar_url)
		msg = await ctx.send(embed=hello_em)


		wins = 0
		losses = 0
		ties = 0

		user_rock_em = discord.Embed(title="You threw out a rock",
									 description="Rock against...",
									 color=discord.Color.greyple())
		user_rock_em.set_image(url="https://media.giphy.com/media/26gsdS1KCyxwTl6IU/giphy.gif")
		user_rock_em.set_thumbnail(url=ctx.message.author.avatar_url)

		user_pap_em = discord.Embed(title="You hit me with paper",
									 description="Paper against...",
									 color=discord.Color.teal())
		user_pap_em.set_image(url="https://media.giphy.com/media/l3q2RoEgmvxXIvA5i/giphy.gif")
		user_pap_em.set_thumbnail(url=ctx.message.author.avatar_url)
		
		user_sci_em = discord.Embed(title="You slashed out some scissors",
									 description="Scissors against...",
									 color=discord.Color.red())
		user_sci_em.set_image(url="https://media1.giphy.com/media/jcBj1VbbrXgJy/source.gif")
		user_sci_em.set_thumbnail(url=ctx.message.author.avatar_url) 

		comp_rock_em = discord.Embed(title="Rock!",
									 color=discord.Color.greyple())
		comp_rock_em.set_image(url="https://technabob.com/blog/wp-content/uploads/2018/07/ksts_st_rock_mood_light_colors.gif")
		comp_rock_em.set_thumbnail(url=self.azami.user.avatar_url)

		comp_pap_em = discord.Embed(title="Paper!",
									 color=discord.Color.teal())
		comp_pap_em.set_image(url="https://share.gifyoutube.com/yEMl0X.gif")
		comp_pap_em.set_thumbnail(url=self.azami.user.avatar_url)

		comp_sci_em = discord.Embed(title="Scissors!",
									 color=discord.Color.red())
		comp_sci_em.set_image(url="https://66.media.tumblr.com/2037d7aa49c718d3229c14eddade2837/tumblr_ov7tlr0UzF1vz54q7o3_500.gifv")
		comp_sci_em.set_thumbnail(url=self.azami.user.avatar_url)

		you_win_em = discord.Embed(title="Congrats you win!",
									 description="I'll get you next time!",
									 color=discord.Color.gold())
		you_win_em.set_image(url="https://media.giphy.com/media/l0HlMWVJqvf86klnq/giphy.gif")
		you_win_em.set_thumbnail(url=ctx.message.author.avatar_url)

		you_lose_em = discord.Embed(title="Better luck next time!",
									 description="Ha! You lost!",
									 color=discord.Color.dark_red())
		you_lose_em.set_image(url="https://media.giphy.com/media/5MtOIdkHhxPFu/giphy.gif")
		you_lose_em.set_thumbnail(url=self.azami.user.avatar_url)

		tie_em = discord.Embed(title="It's a tie...",
									 description="Prepare to lose next time!",
									 color=discord.Color.purple())
		tie_em.set_image(url="https://i.makeagif.com/media/2-03-2016/2VqsWK.gif")
		tie_em.set_thumbnail(url=ctx.message.author.avatar_url)

		while True:
			await ctx.send(f'Wins: {wins}, Losses: {losses}, Ties: {ties}', delete_after=5)
			while True:
				msg2 = await ctx.send("What do you choose (r)ock, (p)aper, (s)cissors or (q)uit")
				player = await self.azami.wait_for('message')
				if player.content == 'q':
					await ctx.send("See you next time")
					return
				if player.content == 'r' or player.content == 'p' or player.content == 's':
					break
				await ctx.send('Write r, p, s or q!', delete_after=5)

			if player.content == 'r':
				await player.delete()
				await msg2.delete()
				await msg.edit(embed=user_rock_em)
			elif player.content == 'p':
				await player.delete()
				await msg2.delete()
				await msg.edit(embed=user_pap_em)
			elif player.content == 's':
				await player.delete()
				await msg2.delete()
				await msg.edit(embed=user_sci_em)

			randomnum = randint(1, 3)
			if randomnum == 1:
				computer = 'r'
				await sleep(3)
				await msg.edit(embed=comp_rock_em)
			elif randomnum == 2:
				computer = 'p'
				await sleep(3)
				await msg.edit(embed=comp_pap_em)
			elif randomnum == 3:
				computer = 's'
				await sleep(3)
				await msg.edit(embed=comp_sci_em)

			if player.content == computer:
				await ctx.send("Please wait...", delete_after=4)
				await sleep(4)
				await msg.edit(embed=tie_em)
				ties += 1
			elif player.content == 'r' and computer == 's':
				await ctx.send("Please wait...", delete_after=4)
				await sleep(4)
				await msg.edit(embed=you_win_em)
				wins += 1
			elif player.content == 'r' and computer == 'p':
				await ctx.send("Please wait...", delete_after=4)
				await sleep(4)
				await msg.edit(embed=you_lose_em)
				losses += 1
			elif player.content == 'p' and computer == 'r':
				await ctx.send("Please wait...", delete_after=4)
				await sleep(4)
				await msg.edit(embed=you_win_em)
				wins += 1
			elif player.content == 'p' and computer == 's':
				await ctx.send("Please wait...", delete_after=4)
				await sleep(4)
				await msg.edit(embed=you_lose_em)
				losses += 1
			elif player.content == 's' and computer == 'p':
				await ctx.send("Please wait...", delete_after=4)
				await sleep(4)
				await msg.edit(embed=you_win_em)
				wins += 1
			elif player.content == 's' and computer == 'r':
				await ctx.send("Please wait...", delete_after=4)
				await sleep(4)
				await msg.edit(embed=you_lose_em)
				losses += 1


	@blame.error
	async def blame_error(self, ctx, error):
		if isinstance(error, MissingRequiredArgument):
			await ctx.send("Requires a user to blame")

	@slap.error 
	async def slap_error(self, ctx, error):
		if isinstance(error, MissingRequiredArgument):
			await ctx.send("Requires a user to hit")

	@_8ball.error
	async def ball8_error(self, ctx, error):
		if isinstance(error, MissingRequiredArgument):
			await ctx.send("Please write a question for me to respond to")

	@up.error
	async def up_error(self, ctx, error):
		if isinstance(error, MissingRequiredArgument):
			await ctx.send("Please give me a word or sentence")

	@say.error
	async def say_error(self, ctx, error):
		if isinstance(error, MissingRequiredArgument):
			await ctx.send("Please give me a word or sentence")
	

def setup(azami):
	azami.add_cog(Fun(azami))