import discord
from discord.ext import commands

class Maths(commands.Cog):

	def __init__(self, azami):
		self.azami = azami

	@commands.command(aliases = ['addition', 'plus', '+'], 
					  description='9 + 10 = ?',
					  usage='Adding two numbers together')
	async def add(self, ctx, a, b, *):
		sum = float(a) + float(b)
		if str(sum)[-2:] == '.0':
			sum = str(sum)[:-2]
		await ctx.send(a, "+", b, "=", sum)

	@commands.command(aliases = ['takeaway', 'minus', '-'], 
					  description='9 - 11 = ?',
					  usage='Subtracting two numbers from each other')
	async def subtract(self, ctx, a, b, *):
		sum = float(a) - float(b)
		if str(sum)[-2:] == '.0':
			sum = str(sum)[:-2]
		await ctx.send(a, "-", b, "=", sum)

	@commands.command(aliases = ['times', '*'], 
					  description='9 x 11 = ?',
					  usage='Multiply two numbers together')
	async def multiply(self, ctx, a, b, *):
		sum = float(a) * float(b)
		if str(sum)[-2:] == '.0':
			sum = str(sum)[:-2]
		await ctx.send(a, "*", b, "=", sum)

	@commands.command(aliases = ['division', '/'], 
					  description='9 / 11 = ?',
					  usage='Divide two numbers from each other')
	async def divide(self, ctx, a, b, *):
		sum = float(a) / float(b)
		if str(sum)[-2:] == '.0':
			sum = str(sum)[:-2]
		await ctx.send(a, "/", b, "=", sum)
	

def setup(azami):
	azami.add_cog(Maths(azami))
