import discord
from discord.ext import commands

class Jojo(commands.Cog):

	def __init__(self, azami):
		self.azami = azami

# I actually made this cog for redbot a differnet discord bot project

	@commands.has_permissions(manage_messages = True)
	@commands.guild_only()
	@commands.command(description="Oh? You're Approaching me?",
					  usage="Jotaro! This is ZA WARUDO! TOKIYO TOMARE!")
	async def tomare(self, ctx, time: int = 0):
		if -1 < time < 12:
			await ctx.send("Invalid time value. Time must be between 0 and 12 (inclusive)")
			return
		await ctx.channel.edit(slowmode_delay=time)
		if time > 0:
			await ctx.send(f"**{ctx.channel.mention} has been stopped in time. Time have frozen for {time} seconds**")
		else:
			await ctx.send(f"**Time resume for {ctx.channel.mention}**")

def setup(azami):
	azami.add_cog(Jojo(azami))
