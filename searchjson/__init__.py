import discord, json, aiohttp
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

async def hastebin(content, session=None): # Move to cogs/utils/check in future
	session = aiohttp.ClientSession()
	async with session.post("https://hastebin.com/documents", data=content.encode('utf-8')) as resp:
		if resp.status == 200:
			result = await resp.json()
			await session.close()
			return "https://hastebin.com/" + result["key"]
		else:
			return f"Error with creating Hastebin, Status: {resp.status}"

		
def startEquipment(driver, body):
	y = json.loads(body)
	startEquipmentUrl = y['starting_equipment']['url']
	driver.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 't') 
	driver.get(f"https://www.dnd5eapi.co{startEquipmentUrl}")
	body2 = driver.find_element_by_xpath('/html/body/pre').text
	y2 = json.loads(body2)

	valueStartEquipmentDef = [y2['starting_equipment'][x]['item']['name'] + " " + str(y2['starting_equipment'][0]['quantity']) for x in range(len(y2['starting_equipment']))] 
	valueStartEquipmentDef = '\n'.join(valueStartEquipmentDef)
	valueStartEquipmentChoose = y2['choices_to_make']

	try:
		valueStartEquipmentChoiceA1 = ["a) " + y2['choice_1'][0]['from'][x]['item']['name'] + " or " + y2['choice_1'][1]['from'][x]['item']['name'] for x in range(len(y2['choice_1'][0]['from']))]
		valueStartEquipmentChoiceA2 = [y2['choice_1'][2]['from'][x]['item']['name'] for x in range(len(y2['choice_1'][2]['from']))]
	except:
		valueStartEquipmentChoiceA1 = ["a) " + y2['choice_1'][0]['from'][x]['item']['name'] for x in range(len(y2['choice_1'][0]['from']))]
		valueStartEquipmentChoiceA2 = [y2['choice_1'][1]['from'][x]['item']['name'] for x in range(len(y2['choice_1'][1]['from']))]
		
	valueStartEquipmentChoiceA1 = ', '.join(valueStartEquipmentChoiceA1)
	valueStartEquipmentChoiceA2 = ', '.join(valueStartEquipmentChoiceA2)
	valueStartEquipmentChoiceA = valueStartEquipmentChoiceA1+" or "+valueStartEquipmentChoiceA2

	try:
		valueStartEquipmentChoiceB = ["b) " + y2['choice_2'][0]['from'][x]['item']['name'] + " or " + y2['choice_2'][1]['from'][x]['item']['name'] for x in range(len(y2['choice_2'][0]['from']))]
	except:
		valueStartEquipmentChoiceB = ["b) " + y2['choice_2'][0]['from'][x]['item']['name'] for x in range(len(y2['choice_2'][0]['from']))]
		
	valueStartEquipmentChoiceB = ', '.join(valueStartEquipmentChoiceB)

	try:
		valueStartEquipmentChoiceC1 = ["c) " + y2['choice_3'][0]['from'][x]['item']['name'] for x in range(len(y2['choice_3'][0]['from']))]
		valueStartEquipmentChoiceC2 = [y2['choice_3'][1]['from'][x]['item']['name'] for x in range(len(y2['choice_3'][1]['from']))]
		valueStartEquipmentChoiceC1 = ', '.join(valueStartEquipmentChoiceC1)
		valueStartEquipmentChoiceC2 = ', '.join(valueStartEquipmentChoiceC2)#
		valueStartEquipmentChoiceC = valueStartEquipmentChoiceC1+" or "+valueStartEquipmentChoiceC2
	except:
		valueStartEquipmentChoiceC = "N/A"

	driver.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 'w') 
	return valueStartEquipmentDef, valueStartEquipmentChoose ,valueStartEquipmentChoiceA, valueStartEquipmentChoiceB, valueStartEquipmentChoiceC


def levelling(driver, body):
	y = json.loads(body)
	levellingUrl = y['class_levels']['url']
	driver.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 't') 
	driver.get(f"https://www.dnd5eapi.co{levellingUrl}")
	body2 = driver.find_element_by_xpath('/html/body/pre').text
	y2 = json.loads(body2)

	level_list = []
	level_list2 = []
	level_list3 = []
	for i in range(0, 23):
		try:
			valueLevel1 = [y2[i]['features'][x]['name'] for x in range(len(y2[i]['features']))]
		except:
			for i in range(0, 20):
				valueLevel1 = [y2[i]['features'][x]['name'] for x in range(len(y2[i]['features']))]
		valueLevel2 = [y2[i]['feature_choices'][x]['name'] for x in range(len(y2[i]['feature_choices']))]
		valueLevel2 += '\n'
		valueLevel1 = str(f"Level {y2[i]['level']} -> ") + (', ').join(p for p in valueLevel1) + " " + (', ').join(p for p in valueLevel2)
		if 'ability_score_bonuses' in y2[i]:
			valueLevel3 = f"Level {y2[i]['level']} -> {y2[i]['ability_score_bonuses']}"
			level_list2.append(valueLevel3)
		if 'prof_bonus' in y2[i]:
			valueLevel4 = f"Level {y2[i]['level']} -> {y2[i]['prof_bonus']}"
			level_list3.append(valueLevel4)
		level_list.append(valueLevel1)

	level_list = '\n'.join(level_list)
	level_list2 = '\n'.join(level_list2)
	level_list3 = '\n'.join(level_list3)
	return level_list, level_list2, level_list3


def spellfind(driver, content, ctx, azami):
	content = content.lower().replace(' ', '-')
	wait = WebDriverWait(driver, 5)
	driver.get(f"https://www.dnd5eapi.co/api/spells/{content}")
	body = driver.find_element_by_xpath('/html/body/pre').text
	x = body
	y = json.loads(x)

	try:
		valueDesc = y['desc']
	except:
		spell_em = discord.Embed(title="Incorrect Spell Given",
								 description="Error Occurred!",
								 color=discord.Color.red())
		spell_em.set_thumbnail(url=azami.user.avatar_url)
		return spell_em
	valueDesc = '\n\n'.join(valueDesc)
	valueHighLvl = y['higher_level']
	valueHighLvl = '\n\n'.join(valueHighLvl)
	valueComp = y['components']
	valueComp = ', '.join(valueComp)
	valueClasses = [y['classes'][x]['name'] for x in range(len(y['classes']))]
	valueClasses = ', '.join(valueClasses)

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
	return spell_em

				  
async def simpleclassfind(driver, content, ctx, azami):
	content = content.lower().replace(' ', '-')
	wait = WebDriverWait(driver, 5)
	driver.get(f"https://www.dnd5eapi.co/api/classes/{content}")
	body = driver.find_element_by_xpath('/html/body/pre').text
	y = json.loads(body)

	try:
		valueProfSpells = [y['proficiency_choices'][0]['from'][x]['name'] for x in range(len(y['proficiency_choices'][0]['from']))]
		valueProfSpells = '\n'.join(p for p in valueProfSpells)
	except:
		class_em = discord.Embed(title="Incorrect Class Given",
								 description="Error Occurred!",
								 color=discord.Color.red())
		class_em.set_thumbnail(url=azami.user.avatar_url)
		return class_em
	try:
		valueProfItems = [y['proficiency_choices'][1]['from'][x]['name'] for x in range(len(y['proficiency_choices'][1]['from']))]
		valueProfItems = '\n'.join(p for p in valueProfItems)
	except:
		valueProfItems = 'N/A'
	valueProfGeneral = [y['proficiencies'][x]['name'] for x in range(len(y['proficiencies']))]
	valueProfGeneral = '\n'.join(p for p in valueProfGeneral)
	savingThrow = [y['saving_throws'][x]['name'] for x in range(len(y['saving_throws']))]
	savingThrow = ', '.join(p for p in savingThrow)
	valueStartEquipmentDef, valueStartEquipmentChoose, valueStartEquipmentChoiceA, valueStartEquipmentChoiceB, valueStartEquipmentChoiceC = startEquipment(driver, body)
	valueLevel1, valueLevel2, valueLevel3 = levelling(driver, body)

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
	return class_em


def classfind(driver, content, ctx, azami):
	content = content.lower().replace(' ', '-')
	wait = WebDriverWait(driver, 5)
	driver.get(f"https://www.dnd5eapi.co/api/classes/{content}")
	body = driver.find_element_by_xpath('/html/body/pre').text
	y = json.loads(body)

	try:
		valueProfSpells = [y['proficiency_choices'][0]['from'][x]['name'] for x in range(len(y['proficiency_choices'][0]['from']))]
		valueProfSpells = '\n'.join(valueProfSpells)
	except:
		class_em = discord.Embed(title="Incorrect Class Given",
								 description="Error Occurred!",
								 color=discord.Color.red())
		class_em.set_thumbnail(url=azami.user.avatar_url)
		return class_em
	try:
		valueProfItems = [y['proficiency_choices'][1]['from'][x]['name'] for x in range(len(y['proficiency_choices'][1]['from']))]
		valueProfItems = '\n'.join(valueProfItems)
	except:
		valueProfItems = 'N/A'
	valueProfGeneral = [y['proficiencies'][x]['name'] for x in range(len(y['proficiencies']))]
	valueProfGeneral = '\n'.join(valueProfGeneral)
	savingThrow = [y['saving_throws'][x]['name'] for x in range(len(y['saving_throws']))]
	savingThrow = ', '.join(savingThrow)
	valueStartEquipmentDef, valueStartEquipmentChoose, valueStartEquipmentChoiceA, valueStartEquipmentChoiceB, valueStartEquipmentChoiceC = startEquipment(driver, body)
	valueLevel1, valueLevel2, valueLevel3 = levelling(driver, body)

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
	return class_em
