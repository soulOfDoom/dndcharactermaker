#write race/class lists
raceList = ['Human', 'Dwarf', 'Elf', 'Gnome', 'Half-Elf', 'Half-Orc', 'Halfling']
classList = ['Barbarian', 'Bard', 'Cleric', 'Druid', 'Fighter', 'Monk', 'Paladin', 'Ranger', 'Rogue', 'Sorcerer', 'Wizard']

#define funtions
def pickRace():
	for races in raceList:
		print races
	race = ''
	race = raw_input('What is your race? ').title()

def pickClass():
	for classes in classList:
		print classes
	clas = ''
	clas = raw_input('What is your class? ').title()

def interpretRace():
	if race == 'Human':
		stren = baseStren
		dex = baseDex
		con = baseCon
		intell = baseIntell
		wis = baseWis
		cha = baseCha

	elif race == 'Dwarf':
		stren = baseStren
		dex = baseDex
		con = baseCon + 2
		intell = baseIntell
		wis = baseWis
		cha = baseCha - 2

	elif race == 'Elf':
		stren = baseStren
		dex = (baseDex + 2)
		con = (baseCon - 2)
		intell = baseIntell
		wis = baseWis
		cha = baseCha

	elif race == 'Gnome':
		stren = baseStren - 2
		dex = baseDex
		con = baseCon + 2
		intell = baseIntell
		wis = baseWis
		cha = baseCha

	elif race == 'Half-Elf':
		stren = baseStren
		dex = baseDex
		con = baseCon
		intell = baseIntell
		wis = baseWis
		cha = baseCha

	elif race == 'Half-Orc':
		stren = baseStren + 2
		dex = baseDex
		con = baseCon
		intell = baseIntell - 2
		wis = baseWis
		cha = baseCha - 2

	elif race == 'Halfling':
		stren = baseStren - 2
		dex = baseDex + 2
		con = baseCon
		intell = baseIntell
		wis = baseWis
		cha = baseCha

	else:
		print 'Race does not exsits'
		pickRace()

def interpretClass():
	if clas == 'Barbarian':
		BAB = 1
		baseFort = 2
		baseRef = 0
		baseWill = 0
		spells = False

	elif clas == 'Bard':
		BAB = 0
		baseFort = 0
		baseRef = 2
		baseWill = 2
		spells = True
		spellsDay = {0:2, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0}
		spellsKnown = {0:4, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0}
		bonusSpellsMod = chaMod

	elif clas == 'Cleric':
		BAB = 0
		baseFort = 2
		baseRef = 0
		baseWill = 2
		spells = True
		spellsDay = {0:3, 1:1, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0}
		spellsDomain = {0:0, 1:1, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0}
		spellsKnown = 'all'
		bonusSpellsMod = wisMod

	elif clas == 'Druid':
		BAB = 0
		baseFort = 2
		baseRef = 0
		baseWill = 2
		spells = True
		spellsDay = {0:3, 1:1, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0}
		spellsKnown = 'all'
		bonusSpellsMod = wisMod

	elif clas == 'Fighter':
		BAB = 1
		baseFort = 2
		baseRef = 0
		baseWill = 0
		spells = False

	elif clas == 'Monk':
		BAB = 0
		baseFort = 2
		baseRef = 2
		baseWill = 2
		spells = False

	elif clas == 'Paladin':
		BAB = 1
		baseFort = 2
		baseRef = 0
		baseWill = 0
		spells = True
		spellsDay = {0:0, 1:0, 2:0, 3:0, 4:0}
		spellsKnown = 'all'
		bonusSpellsMod = wisMod

	elif clas == 'Ranger':
		BAB = 1
		baseFort = 2
		baseRef = 2
		baseWill = 0
		spells = True
		spellsDay = {0:0, 1:0, 2:0, 3:0, 4:0}
		spellsKnown = 'all'
		bonusSpellsMod = wisMod

	elif clas == 'Rogue':
		BAB = 0
		baseFort = 0
		baseRef = 2
		baseWill = 0
		spells = False

	elif clas == 'Sorcerer':
		BAB = 0
		baseFort = 0
		baseRef = 0
		baseWill = 2
		spells = True
		spellsDay = {0:5, 1:3, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0}
		spellsKnown = {0:4, 1:2, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0}
		bonusSpellsMod = chaMod

	elif clas == 'Wizard':
		BAB = 0
		baseFort = 0
		baseRef = 0
		baseWill = 2
		spells = True
		spellsDay = {0:3, 1:1, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0}
		spellsKnown = {0:'all', 1:3, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0}
		bonusSpellsMod = intellMod

	else:
		print 'class does not exist.'
		pickClass()

#pick name
name = raw_input('What is your name? ').title()

#first pick race
race = pickRace()

#first pick class
clas = pickClass()

#picking ability scores
baseStren = input('\nRoll 4d6 and drop the lowest for your STR score: ')
baseDex = input('Roll 4d6 and drop the lowest for your DEX score: ')
baseCon = input('Roll 4d6 and drop the lowest for your CON score: ')
baseIntell = input('Roll 4d6 and drop the lowest for your INT score: ')
baseWis = input('Roll 4d6 and drop the lowest for your WIS score: ')
baseCha = input('Roll 4d6 and drop the lowest for your CHA score: ')

#interpret race
interpretRace()

#interpret class
interpretClass()

#calculate mods
strenMod = (stren-10)/2
dexMod = (dex-10)/2
conMod = (con-10)/2
intellMod = (intell-10)/2
wisMod = (wis-10)/2
chaMod = (cha-10)/2

abilityFormat = '%3d%+4d'

saveFormat = '%+3d'

fortSave = baseFort + conMod
refSave = baseRef + dexMod
willSave = baseWill + wisMod

print '\n', name, 'the', race, clas, '\n', \
'=' * 20, '\n', \
' Ability Scores\n', \
'-' * 20, '\n', \
'STR:', abilityFormat % (stren, strenMod), '\n', \
'DEX:', abilityFormat % (dex, dexMod), '\n', \
'CON:', abilityFormat % (con, conMod), '\n', \
'INT:', abilityFormat % (intell, intellMod), '\n', \
'WIS:', abilityFormat % (wis, wisMod), '\n', \
'CHA:', abilityFormat % (cha, chaMod), '\n', \
'=' * 20, '\n', \
'Base Attack Bonus:', BAB , '\n', \
'=' * 20, '\n', \
' Saves\n', \
'-' * 20, '\n', \
'%-10s' % ('Fortitude:'), saveFormat % (fortSave), '\n', \
'%-10s' % ('Refex:'), saveFormat % (refSave), '\n', \
'%-10s' % ('Will:'), saveFormat % (willSave), '\n', \
'-' * 20, '\n'
if spells == True:
	print '=' * 37, '\n', \
	'Spells Known\n', \
	'-' * 37, '\n', \
	'level-0 | spells per day:', spellsDay[0], '|'
