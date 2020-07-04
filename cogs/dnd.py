import discord, sys, time, aiohttp, json
from discord.ext import commands
from discord.ext.commands import MissingRequiredArgument
from random import randint
from asyncio import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
sys.path.insert(1, '../')
from diceimg import diceroll
from searchjson import startEquipment, levelling, spellfind, simpleclassfind, classfind
from driver import get_driver

# This cog is a real mess but it works xD

color_list = [discord.Color.red(), discord.Color.green(), discord.Color.blue(),
			  discord.Color.orange(), discord.Color.purple(), discord.Color.gold(),
			  discord.Color.blurple(), discord.Color.greyple(), discord.Color.teal(),
			  discord.Color.dark_red(), discord.Color.dark_green(),
			  discord.Color.light_grey(), discord.Color.dark_gold()]

def return_results(limit, rolls, mod, i=0): # Future update: Embed all commands
	if rolls == 1:
		result = ', '.join(str(randint(1, limit)) for r in range(rolls))
		result = int(result)

		if mod > 0:
			result += mod

		result_em = discord.Embed(title=f"Here's your result!",
							  	  description=f"You got: {result}!",
							  	  color=discord.Color.gold())

		if result > 20:
			return result_em
		else:
			dicepic = diceroll(result)
			result_em.set_image(url=dicepic)
			return result_em

	else:
		multi_em = discord.Embed(title=f"Rolled so far {i+1}",
								 color=discord.Color.gold())
		limit = randint(1, limit)

		if mod > 0:
			limit += mod

		if limit > 20:
			return multi_em.add_field(name=f"Roll {i + 1}", value=f"This your value: {limit}")
		else:
			dicepic = diceroll(limit)
			multi_em.add_field(name=f"Roll {i + 1}", value=f"This your value: {limit}")
			multi_em.set_image(url=dicepic)
			return multi_em

def hiddenrolls(mod=0):
	dice = '1d20'
	rolls, limit = map(int, dice.split('d'))
	result = ', '.join(str(randint(1, limit)) for r in range(rolls))
	result = int(result)
	result += mod
	return result

async def hastebin(content, session=None): # Move to cogs/utils/check in future
	session = aiohttp.ClientSession()
	async with session.post("https://hastebin.com/documents", data=content.encode('utf-8')) as resp:
		if resp.status == 200:
			result = await resp.json()
			await session.close()
			return "https://hastebin.com/" + result["key"]
		else:
			return f"Error with creating Hastebin, Status: {resp.status}"

class Dnd(commands.Cog): # Work on Embed Rolls also modifier addon

	def __init__(self, azami):
		self.azami = azami
		try:
			self.driver = get_driver()
		except:
			self.driver = webdriver.Chrome('./chromedriver')
		self.driver.minimize_window()

	@commands.command(description=f'The format must be NdN',
					  usage='To roll any dice, any amount of times')
	async def roll(self, ctx, dice: str, mod=0):
		try:
			rolls, limit = map(int, dice.split('d'))
		except Exception:
			await ctx.send('The format has to be in NdN!')
			return

		roll_em = discord.Embed(title=f"Rolling {rolls} dice(s)",
								description=f"Hope you get a natural {limit}!",
								color=discord.Color.teal())
		roll_em.set_thumbnail(url=ctx.message.author.avatar_url)

		if limit == 4:
			roll_em.set_image(url="https://media.giphy.com/media/fiqcUhBNj6jWgJnRlu/giphy.gif")
			roll_em.add_field(name=f"Currently rolling {rolls}d{limit}", value="\u200b")
			msg = await ctx.send(embed=roll_em)
			await sleep(2)
			result_em = return_results(limit, rolls, mod)
			result_em.set_thumbnail(url=ctx.message.author.avatar_url)
			if rolls > 1:
				await msg.delete()
				for i in range(0, rolls):
					result_em = return_results(limit, rolls, mod, i)
					result_em.set_thumbnail(url=ctx.message.author.avatar_url)
					await ctx.send(embed=result_em)
			else:
				await msg.edit(embed=result_em)

		elif limit == 6:
			roll_em.set_image(url="https://bestanimations.com/Games/Dice/rolling-dice-gif-1.gif")
			roll_em.add_field(name=f"Currently rolling {rolls}d{limit}", value="\u200b")
			msg = await ctx.send(embed=roll_em)
			await sleep(2)
			result_em = return_results(limit, rolls, mod)
			result_em.set_thumbnail(url=ctx.message.author.avatar_url)
			if rolls > 1:
				await msg.delete()
				for i in range(0, rolls):
					result_em = return_results(limit, rolls, mod, i)
					result_em.set_thumbnail(url=ctx.message.author.avatar_url)
					await ctx.send(embed=result_em)
			else:
				await msg.edit(embed=result_em)

		elif limit == 8:
			roll_em.set_image(url="https://66.media.tumblr.com/457d10f08e468d1392ab7165ab330ba7/dc90dde4ae909e0f-2b/s400x600/a62e416692fcddf76e7623d560b89a8ad102a5c6.gifv")
			roll_em.add_field(name=f"Currently rolling {rolls}d{limit}", value="\u200b")
			msg = await ctx.send(embed=roll_em)			
			await sleep(2)
			result_em = return_results(limit, rolls, mod)
			result_em.set_thumbnail(url=ctx.message.author.avatar_url)
			if rolls > 1:
				await msg.delete()
				for i in range(0, rolls):
					result_em = return_results(limit, rolls, mod, i)
					result_em.set_thumbnail(url=ctx.message.author.avatar_url)
					await ctx.send(embed=result_em)
			else:
				await msg.edit(embed=result_em)

		elif limit == 10:
			roll_em.set_image(url="https://66.media.tumblr.com/3096dd055c2c00055e68e46695d18b09/23077a30d50cc0d0-93/s400x600/0936ec389211b11f159f79265b15a44370e8688a.gifv")
			roll_em.add_field(name=f"Currently rolling {rolls}d{limit}", value="\u200b")
			msg = await ctx.send(embed=roll_em)
			await sleep(2)
			result_em = return_results(limit, rolls, mod)
			result_em.set_thumbnail(url=ctx.message.author.avatar_url)
			if rolls > 1:
				await msg.delete()
				for i in range(0, rolls):
					result_em = return_results(limit, rolls, mod, i)
					result_em.set_thumbnail(url=ctx.message.author.avatar_url)
					await ctx.send(embed=result_em)
			else:
				await msg.edit(embed=result_em)

		elif limit == 100:
			roll_em.set_image(url="https://i.pinimg.com/originals/2f/d5/73/2fd573b2f3c6499ec3963b77475b43b2.png")
			roll_em.add_field(name=f"Currently rolling {rolls}d{limit}", value="\u200b")
			msg = await ctx.send(embed=roll_em)
			await sleep(2)
			result_em = return_results(limit, rolls, mod)
			result_em.set_thumbnail(url=ctx.message.author.avatar_url)
			if rolls > 1:
				await msg.delete()
				for i in range(0, rolls):
					result_em = return_results(limit, rolls, mod, i)
					result_em.set_thumbnail(url=ctx.message.author.avatar_url)
					await ctx.send(embed=result_em)
			else:
				await msg.edit(embed=result_em)

		elif limit == 12:
			roll_em.set_image(url="https://webstockreview.net/images/dice-clipart-d12-5.png")
			roll_em.add_field(name=f"Currently rolling {rolls}d{limit}", value="\u200b")
			msg = await ctx.send(embed=roll_em)
			await sleep(2)
			result_em = return_results(limit, rolls, mod)
			result_em.set_thumbnail(url=ctx.message.author.avatar_url)
			if rolls > 1:
				await msg.delete()
				for i in range(0, rolls):
					result_em = return_results(limit, rolls, mod, i)
					result_em.set_thumbnail(url=ctx.message.author.avatar_url)
					await ctx.send(embed=result_em)
			else:
				await msg.edit(embed=result_em)

		elif limit == 20:
			roll_em.set_image(url="https://66.media.tumblr.com/1458225a6051e572f34b931011630d71/tumblr_ol1es3Lg4a1tevcm3o1_400.gifv")
			roll_em.add_field(name=f"Currently rolling {rolls}d{limit}", value="\u200b")
			msg = await ctx.send(embed=roll_em)
			await sleep(2)
			result_em = return_results(limit, rolls, mod)
			result_em.set_thumbnail(url=ctx.message.author.avatar_url)
			if rolls > 1:
				await msg.delete()
				for i in range(0, rolls):
					result_em = return_results(limit, rolls, mod, i)
					result_em.set_thumbnail(url=ctx.message.author.avatar_url)
					await ctx.send(embed=result_em)
			else:
				await msg.edit(embed=result_em)

		else:
			roll_em.set_image(url="https://cdn.shopify.com/s/files/1/1483/3510/products/Haunted_Dice_Ice_grande.gif")
			roll_em.add_field(name=f"Currently rolling {rolls}d{limit}", value="\u200b")
			msg = await ctx.send(embed=roll_em)
			await sleep(2)
			result_em = return_results(limit, rolls, mod)
			result_em.set_thumbnail(url=ctx.message.author.avatar_url)
			if rolls > 1:
				await msg.delete()
				for i in range(0, rolls):
					result_em = return_results(limit, rolls, mod, i)
					result_em.set_thumbnail(url=ctx.message.author.avatar_url)
					await ctx.send(embed=result_em)
			else:
				await msg.edit(embed=result_em)

	@commands.command(description='Rolling initiative',
					  usage='This will decide who gets to attack first')
	async def initiative(self, ctx):
		await ctx.send("How many players are playing?")
		while True:
			try:
				player = await self.azami.wait_for('message')
				playercont = int(player.content)
				await player.delete()
				break
			except Exception:
				await ctx.send("Please enter a integer")
		order = []
		for i in range(0, playercont):
			msg = await ctx.send(f'Player {i + 1}')
			msg2 = await ctx.send("Enter your name!")
			player_name = await self.azami.wait_for('message')
			player_namecont = player_name.content
			msg3 = await ctx.send("Enter your dex modifier")
			while True:
				while True:
					try:
						mod = await self.azami.wait_for('message')
						modcont = int(mod.content)
						break
					except Exception:
						await ctx.send("Please enter an integer")
				result = hiddenrolls(modcont)
				line = f"{player_namecont},"+str(result)
				name, score = line.split(',')
				score = int(score)
				order.append((name, score))
				await mod.delete()
				await msg.delete()
				await msg2.delete()
				await msg3.delete()
				order.sort(key=lambda x: x[1], reverse=True)
				break
					
		hastebin_list = []
		for name, score in order:
			line = f"{name}, {score}"
			await ctx.send(line)
			hastebin_list.append(line)
		_all = '\n'.join(hastebin_list)
		url = await hastebin(str(_all), None)
		hastebin_of_players = f'[List of all players in order]({url})'
		em = discord.Embed(name="Link for the player order!", # When working on 2.0 make a general embed function
						   description= hastebin_of_players,
						   color= discord.Color.blurple())
		await ctx.send(embed=em)

	@commands.command(name="spell search",
					  description="Search from spells across all of dnd 5e",
					  usage="spellsearch is written together when using the command",
					  aliases=['ss', 'spellsearch'])
	async def spellsearch(self, ctx, *, content):
		content = content.lower().replace(' ', '-')
		wait = WebDriverWait(self.driver, 5)
		self.driver.get(f"https://www.dnd5eapi.co/api/spells/{content}")
		body = self.driver.find_element_by_xpath('/html/body/pre').text
		x = body
		y = json.loads(x)

		valueDesc = y['desc']
		valueDesc = '\n\n'.join(p for p in valueDesc)
		valueHighLvl = y['higher_level']
		valueHighLvl = '\n\n'.join(p for p in valueHighLvl)
		valueComp = y['components']
		valueComp = ', '.join(p for p in valueComp)
		valueClasses = [y['classes'][x]['name'] for x in range(len(y['classes']))]
		valueClasses = ', '.join(p for p in valueClasses)

		spell_em = discord.Embed(title="So here's the spell your looking for traveller!",
								description=f"Information on: {y['name']}",
								color=discord.Color.blue())
		spell_em.set_thumbnail(url=ctx.message.author.avatar_url)
		spell_em.add_field(name="Name", value=y['name'])
		spell_em.add_field(name="Description", value=valueDesc)
		spell_em.add_field(name="At a higher level", value=valueHighLvl)
		spell_em.add_field(name="Range", value=y['range'])
		spell_em.add_field(name="Components", value=valueComp)
		spell_em.add_field(name="Ritual", value=y['ritual'])
		spell_em.add_field(name="Duration", value=y['duration'])
		spell_em.add_field(name="Concentration", value=y['concentration'])
		spell_em.add_field(name="Casting time", value=y['casting_time'])
		spell_em.add_field(name="Level", value=y['level'])
		spell_em.add_field(name="Classes", value=valueClasses)
		await ctx.send(embed=spell_em)

	@commands.command(name="simple classes search",
					  description="Search from classes across all of dnd 5e. Just Simpler. Using aiohttp",
					  usage="simpleclassessearch is written together when using the command",
					  aliases=['scs', 'simpleclassessearch'])
	async def simpleclassessearch(self, ctx, *, content):
		content = content.lower().replace(' ', '-')
		wait = WebDriverWait(self.driver, 5)
		self.driver.get(f"https://www.dnd5eapi.co/api/classes/{content}")
		body = self.driver.find_element_by_xpath('/html/body/pre').text
		y = json.loads(body)

		# valueDesc = y['desc']
		# valueDesc = '\n\n'.join(p for p in valueDesc)
		# valueHighLvl = y['higher_level']
		# valueHighLvl = '\n\n'.join(p for p in valueHighLvl)
		# valueComp = y['components']
		# valueComp = ', '.join(p for p in valueComp)
		valueProfSpells = [y['proficiency_choices'][0]['from'][x]['name'] for x in range(len(y['proficiency_choices'][0]['from']))]
		valueProfSpells = '\n'.join(p for p in valueProfSpells)
		try:
			valueProfItems = [y['proficiency_choices'][1]['from'][x]['name'] for x in range(len(y['proficiency_choices'][1]['from']))]
			valueProfItems = '\n'.join(p for p in valueProfItems)
		except:
			valueProfItems = 'N/A'
		valueProfGeneral = [y['proficiencies'][x]['name'] for x in range(len(y['proficiencies']))]
		valueProfGeneral = '\n'.join(p for p in valueProfGeneral)
		savingThrow = [y['saving_throws'][x]['name'] for x in range(len(y['saving_throws']))]
		savingThrow = ', '.join(p for p in savingThrow)
		valueStartEquipmentDef, valueStartEquipmentChoose, valueStartEquipmentChoiceA, valueStartEquipmentChoiceB, valueStartEquipmentChoiceC = startEquipment(self.driver, body)
		valueLevel1, valueLevel2, valueLevel3 = levelling(self.driver, body)

		url1 = await hastebin(str(valueProfSpells), None)
		url2 = await hastebin(str(valueProfGeneral), None)
		url3 = await hastebin(str(valueProfSpells), None)
		url4 = await hastebin(str(valueStartEquipmentDef), None)
		url5 = await hastebin(str(valueStartEquipmentChoiceA), None)
		url6 = await hastebin(str(valueStartEquipmentChoiceB), None)
		url7 = await hastebin(str(valueStartEquipmentChoiceC), None)
		url8 = await hastebin(str(valueLevel1), None)
		url9 = await hastebin(str(valueLevel2), None)
		url10 = await hastebin(str(valueLevel3), None)
		url1 = f'[Proficiencies in Skills]({url1})'
		url2 = f'[Proficiencies in Items]({url2})'
		url3 = f'[Proficient in Armour and Weapons]({url3})'
		url4 = f'[Default Starting Equipment]({url4})'
		url5 = f'[Starting Equipment Choice 1]({url5})'
		url6 = f'[Starting Equipment Choice 2]({url6})'
		url7 = f'[Starting Equipment Choice 3]({url7})'
		url8 = f'[Class Levels]({url8})'
		url9 = f'[Ability Score per Level]({url9})'
		url10 = f'[Proficiencies per Level]({url10})'

		class_em = discord.Embed(title="So here's the class Information, traveller!",
								description=f"Information on: {y['name']}",
								color=discord.Color.blue())
		class_em.set_thumbnail(url=ctx.message.author.avatar_url)
		class_em.add_field(name="Name", value=y['name'])
		
		class_em.add_field(name="Hit Die", value=y['hit_die'])
		try:
			class_em.add_field(name="(Proficient in skills) Choose up to", value=y['proficiency_choices'][1]['choose'])
		except:
			class_em.add_field(name="(Proficient in skills) Choose up to", value=y['proficiency_choices'][0]['choose'])
		class_em.add_field(name="Proficiencies in Skills", value=url1)
		class_em.add_field(name="(Proficient in Items) Choose up to", value=y['proficiency_choices'][0]['choose'])
		class_em.add_field(name="Proficiencies in Items", value=url2)
		class_em.add_field(name="Proficient in Armour and Weapons", value=url3)
		class_em.add_field(name="Saving Throws", value=savingThrow)
		if content != 'fighter':
			class_em.add_field(name="Default Starting Equipment", value=url4)
		class_em.add_field(name="(Starting Equipment) Choose up to: ", value=valueStartEquipmentChoose)
		class_em.add_field(name="Starting Equipment Choice 1", value=url5)
		class_em.add_field(name="Starting Equipment Choice 2", value=url6)
		class_em.add_field(name="Starting Equipment Choice 3", value=url7)	
		class_em.add_field(name="Class Levels", value=url8)
		class_em.add_field(name="Ability Score per Level", value=url9)
		class_em.add_field(name="Proficiencies per Level", value=url10)
		await ctx.send(embed=class_em)

	@commands.command(name="classes search",
					  description="Search from classes across all of dnd 5e.",
					  usage="classessearch is written together when using the command",
					  aliases=['cs', 'classessearch'])
	async def classessearch(self, ctx, *, content):
		content = content.lower().replace(' ', '-')
		wait = WebDriverWait(self.driver, 5)
		self.driver.get(f"https://www.dnd5eapi.co/api/classes/{content}")
		body = self.driver.find_element_by_xpath('/html/body/pre').text
		y = json.loads(body)

		valueProfSpells = [y['proficiency_choices'][0]['from'][x]['name'] for x in range(len(y['proficiency_choices'][0]['from']))]
		valueProfSpells = '\n'.join(p for p in valueProfSpells)
		try:
			valueProfItems = [y['proficiency_choices'][1]['from'][x]['name'] for x in range(len(y['proficiency_choices'][1]['from']))]
			valueProfItems = '\n'.join(p for p in valueProfItems)
		except:
			valueProfItems = 'N/A'
		valueProfGeneral = [y['proficiencies'][x]['name'] for x in range(len(y['proficiencies']))]
		valueProfGeneral = '\n'.join(p for p in valueProfGeneral)
		savingThrow = [y['saving_throws'][x]['name'] for x in range(len(y['saving_throws']))]
		savingThrow = ', '.join(p for p in savingThrow)
		valueStartEquipmentDef, valueStartEquipmentChoose, valueStartEquipmentChoiceA, valueStartEquipmentChoiceB, valueStartEquipmentChoiceC = startEquipment(self.driver, body)
		valueLevel1, valueLevel2, valueLevel3 = levelling(self.driver, body)

		class_em = discord.Embed(title="So here's the class Information, traveller!",
								description=f"Information on: {y['name']}",
								color=discord.Color.blue())
		class_em.set_thumbnail(url=ctx.message.author.avatar_url)
		class_em.add_field(name="Name", value=y['name'])
		
		class_em.add_field(name="Hit Die", value=y['hit_die'])
		try:
			class_em.add_field(name="(Proficient in skills) Choose up to", value=y['proficiency_choices'][1]['choose'])
		except:
			class_em.add_field(name="(Proficient in skills) Choose up to", value=y['proficiency_choices'][0]['choose'])
		class_em.add_field(name="Proficiencies in Skills", value=valueProfSpells)
		class_em.add_field(name="(Proficient in Items) Choose up to", value=y['proficiency_choices'][0]['choose'])
		class_em.add_field(name="Proficiencies in Items", value=valueProfItems)
		class_em.add_field(name="Proficient in Armour and Weapons", value=valueProfGeneral)
		class_em.add_field(name="Saving Throws", value=savingThrow)
		if content != 'fighter':
			class_em.add_field(name="Default Starting Equipment", value=valueStartEquipmentDef)
		class_em.add_field(name="(Starting Equipment) Choose up to: ", value=valueStartEquipmentChoose)
		class_em.add_field(name="Starting Equipment Choice 1", value=valueStartEquipmentChoiceA)
		class_em.add_field(name="Starting Equipment Choice 2", value=valueStartEquipmentChoiceB)
		class_em.add_field(name="Starting Equipment Choice 3", value=valueStartEquipmentChoiceC)
		if content != 'warlock':
			class_em.add_field(name="Class Levels", value=valueLevel1)
		class_em.add_field(name="Ability Score per Level", value=valueLevel2)
		class_em.add_field(name="Proficiencies per Level", value=valueLevel3)
		await ctx.send(embed=class_em)

	@commands.command(name='dnd menu', description=f'A DND Menu',
					  aliases=['dndm', 'mdnd'],
					  usage='dndmenu is written together when using the command')
	async def dndmenu(self, ctx):
		menu_em = discord.Embed(title="Welcome to the DND Menu, traveller!",
								description="So what would you like adventurer?",
								color=discord.Color.red())
		menu_em.set_thumbnail(url=ctx.message.author.avatar_url)
		menu_em.set_footer(text=f"Requested by {ctx.message.author.name} - Today at: " + (
							  time.strftime("%I:%M %p")),
							  icon_url=self.azami.user.avatar_url)

		menumessage = "So choose from the following: \n" \
		"1) a!roll - Simple Roll Command\n" \
		"2) a!modroll - Simple Roll with modifier\n" \
		"3) a!initiative - Rolling for initiative\n" \
		"4) a!spellsearch - Search for any spell in DND 5e\n" \
		"5) a!classessearch - Search for any class in DND 5e\n" \
		"6) a!simpleclassessearch - A cleaner way to search for classes in 5e\n" \
		"7) Quit - Exit Menu"

		menu_em.add_field(name="Menu Commands", value=menumessage)

		msg = await ctx.send(embed=menu_em)


		while True:
			await ctx.send(f"Waiting for you command, {ctx.message.author.name}", delete_after=3)
			msg2 = await ctx.send("Please enter a number 1 - 7")
			player = await self.azami.wait_for('message', timeout=120.00)
			if player.content == "7":
				await msg.delete()
				await msg2.delete()
				await ctx.send("See you next time!")
				return
			elif player.content == "1":
				await msg.delete()
				await msg2.delete()
				await ctx.send("Please enter NdN format, eg. 1d20")
				dice = await self.azami.wait_for('message')
				await self.roll(ctx, dice.content)
				break
			elif player.content == "2":
				await msg.delete()
				await msg2.delete()
				await ctx.send("Please enter NdNdN format, eg. 1d20d2")
				dice = await self.azami.wait_for('message')
				dice = dice.content
				try:
					rolls, limit, mod = map(int, dice.split('d'))
				except Exception:
					await ctx.send('The format has to be in NdNdN!')
					return
				dice = str(rolls) + "d" + str(limit)
				await self.roll(ctx, dice, mod)
				break
			elif player.content == "3":
				await msg.delete()
				await msg2.delete()
				await self.initiative(ctx)
				break
			elif player.content == "4":
				await msg.delete()
				await msg2.delete()
				await ctx.send("Enter the spell you want to search for: ")
				player = await self.azami.wait_for('message')
				playercont = player.content
				await player.delete()
				spell_em = spellfind(self.driver, playercont, ctx, self.azami)
				await ctx.send(embed=spell_em)
				break
			elif player.content == "5":
				await msg.delete()
				await msg2.delete()
				await ctx.send("Enter the class you want to search for: ")
				player = await self.azami.wait_for('message')
				playercont = player.content
				await player.delete()
				class_em = classfind(self.driver, playercont, ctx, self.azami)
				await ctx.send(embed=class_em)
				break
			elif player.content == "6":
				await msg.delete()
				await msg2.delete()
				await ctx.send("Enter the class you want to search for: ")
				player = await self.azami.wait_for('message')
				playercont = player.content
				await player.delete()
				spell_em = await simpleclassfind(self.driver, playercont, ctx, self.azami)
				await ctx.send(embed=spell_em)
				break

	
	@spellsearch.error
	async def spellsearch_error(self, ctx, error):
		if isinstance(error, commands.CommandInvokeError):
			await ctx.send(f"Incorrect Spell given")
		elif isinstance(error, MissingRequiredArgument):
			await ctx.send("Requires an argument")

	@classessearch.error
	async def classessearch_error(self, ctx, error):
		if isinstance(error, commands.CommandInvokeError):
			await ctx.send(f"Incorrect Class given")
			print(error)
		elif isinstance(error, MissingRequiredArgument):
			await ctx.send("Requires an argument")

	@simpleclassessearch.error
	async def simpleclassessearch_error(self, ctx, error):
		if isinstance(error, commands.CommandInvokeError):
			await ctx.send(f"Incorrect Class given")
			print(error)
		elif isinstance(error, MissingRequiredArgument):
			await ctx.send("Requires an argument")


def setup(azami):
	azami.add_cog(Dnd(azami))