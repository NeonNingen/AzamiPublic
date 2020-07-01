import discord
from discord.ext import commands

class CommandErrorHandler(commands.Cog):

	def __init__(self, bot):
		self.bot = bot

	@commands.Cog.listener()
	async def on_command_error(self, ctx, error):
		'''Error Handler'''

		if hasattr(ctx.command, 'on_error'):
			return
		cog = ctx.cog
		if cog:
			if cog._get_overridden_method(cog.cog_command_error) is not None:
				return

		ignored = (commands.CommandNotFound, )
		error = getattr(error, 'original', error)

		if isinstance(error, ignored):
			return

		if isinstance(error, commands.DisabledCommand):
			await ctx.send(f'{ctx.command} has been disabled.')

		elif isinstance(error, commands.NoPrivateMessage):
			try:
				await ctx.author.send(f'{ctx.command} can not be used in Private Messages.')
			except discord.HTTPException:
				pass

		elif isinstance(error, commands.BadArgument) or isinstance(error, commands.CommandInvokeError):
            await ctx.send('Invalid input')

        elif isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Requires an argument.")

        elif isinstance(error, commands.NotOwner):
			await ctx.send("You must be the owner of this bot to use this command")
        




        #Include this block of code if you want to send errors to console
		# print('Ignoring exception in command {}:'.format(ctx.command), file=sys.stderr)
		# traceback.print_exception(type(error), error, error.__traceback__, file=sys.stderr)

        #Include this block of code if you want to send errors to a channel, change id in  channel = bot.get_channel(id) to the id of the channel you want to send it to
		# channel = bot.get_channel(id)
		# embed=discord.Embed(color=0xFF0000)
		# embed.add_field(name="Error", value="```python\n"+str(error)+"```\n", inline=True)
		# embed.add_field(name="Invoking command", value=str(ctx.message.content), inline=False)
		# embed.add_field(name="Author", value=ctx.author, inline=False)
		# embed.add_field(name="File", value="discordbots/logger/logbot.py", inline=True)
		# await channel.send(embed=embed)
		#await ctx.send(embed=ctx.bot.something_error)

        return

def setup(bot):
	bot.add_cog(CommandErrorHandler(bot))