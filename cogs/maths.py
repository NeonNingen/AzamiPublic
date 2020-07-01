import discord
from discord.ext import commands

class Maths(commands.Cog):

	def __init__(self, azami):
		self.azami = azami

	@commands.command(aliases = ['addition', 'plus', '+'], 
					  description='9 + 10 = ?',
					  usage='Adding two numbers together')
	async def add(self, ctx, a: float, b: float):
		await ctx.send(f"{a} + {b} = {a + b}")

	@commands.command(aliases = ['takeaway', 'minus', '-'], 
					  description='9 - 11 = ?',
					  usage='Subtracting two numbers from each other')
	async def subtract(self, ctx, a: float, b: float):
		await ctx.send(f"{a} - {b} = {a - b}")

	@commands.command(aliases = ['times', '*'], 
					  description='9 x 11 = ?',
					  usage='Multiply two numbers together')
	async def multiply(self, ctx, a: float, b: float):
		await ctx.send(a * b)

	@commands.command(aliases = ['division', '/'], 
					  description='9 / 11 = ?',
					  usage='Divide two numbers from each other')
	async def divide(self, ctx, a: float, b: float):
		await ctx.send(a / b)
	

def setup(azami):
	azami.add_cog(Maths(azami))
