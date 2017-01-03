import random, sys, msvcrt, os, time
characters={
"a":'r',
"b":'o',
"c":'s',
"d":'t',
"e":'e',
"f":'a',
"g":'b',
"h":'c',
"i":'d',
"j":'f',
"k":'g',
"l":'h',
"m":'i',
"n":'j',
"o":'k',
"p":'l',
"q":'m',
"r":'n',
"s":'p',
"t":'q',
"u":'u',
"v":'v',
"w":'w',
"x":'x',
"y":'y',
"z":'z',
"A":'R',
"B":'O',
"C":'S',
"D":'T',
"E":'E',
"F":'A',
"G":'B',
"H":'C',
"I":'D',
"J":'F',
"K":'G',
"L":'H',
"M":'I',
"N":'J',
"O":'K',
"P":'L',
"Q":'M',
"R":'N',
"S":'P',
"T":'Q',
"U":'U',
"V":'V',
"W":'W',
"X":'X',
"Y":'Y',
"Z":'Z',
' ':'*'
}
presets = {
"UPLEFT" :[
[['#', '#', '#', '#', '#', '#', '#', '#', '#', '#'], ['#', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ','#'], ['#', ' ', ' ', '#', ' ', '#', ' ', ' ', ' ', '#'], ['#', ' ', '#', '#', ' ', '#', ' ', ' ', '#', '#'], ['#', ' ', ' ', ' ', ' ', '#', ' ', '#', '#', '#'], ['#', ' ', '#', '#', '#', '#', ' ', '#', ' ', ' '], ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'], ['#', ' ', ' ', '#', '#', '#', '#', '#', ' ', '#'], ['#', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', '#'], ['#', '#', '#', '#',' ', '#', '#', '#', '#', '#']],
[['#', '#', '#', '#', '#', '#', '#', '#', '#', '#'], ['#', '#', ' ', ' ', ' ', ' ', ' ', ' ', '#', '#'], ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'], ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'], ['#', ' ', ' ', ' ', '#', '#', ' ', ' ', ' ', '#'], ['#', ' ', ' ', ' ', '#', '#', ' ', ' ', ' ', ' '], ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'], ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'], ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'], ['#', '#', '#', '#', ' ', '#', '#', '#', '#', '#']],
[['#', '#', '#', '#', '#', '#', '#', '#', '#', '#'], ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#'], ['#', ' ', ' ', ' ', ' ', ' ', ' ', '#', '#', '#'], ['#', ' ', ' ', ' ', ' ', ' ', ' ', '#', '#', '#'], ['#', ' ', ' ', ' ', ' ', ' ', ' ', '#', '#', '#'], ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], ['#', '#', '#', '#', ' ', '#', '#', '#', '#', '#'], ['#', '#', '#', '#', ' ', '#', '#', '#', '#', '#'], ['#', '#', '#', '#', ' ', '#', '#', '#', '#', '#'], ['#', '#', '#', '#', ' ', '#', '#', '#', '#', '#']]
],
"UPRIGHT" : [
[['#', '#', '#', '#', '#', '#', '#', '#', '#', '#'], ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'], ['#', '#', '#', '#', ' ', '#', '#', '#', ' ', '#'], ['#', ' ', ' ', ' ', ' ', '#', ' ', '#', ' ', '#'], ['#', ' ', '#', ' ', '#', '#', ' ', ' ', ' ', '#'], [' ', ' ', '#', ' ', ' ', '#', ' ', '#', ' ', '#'], ['#', ' ', '#', ' ', ' ', '#', ' ', '#', '#', '#'], ['#', ' ', '#', '#', '#', '#', ' ', '#', ' ', '#'], ['#', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', '#'], ['#', '#', '#', '#', '#', ' ', '#', '#', '#', '#']],
[['#', '#', '#', '#', '#', '#', '#', '#', '#', '#'], ['#', '#', ' ', ' ', ' ', ' ', ' ', ' ', '#', '#'], ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'], ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'], ['#', ' ', ' ', ' ', '#', '#', ' ', ' ', ' ', '#'], [' ', ' ', ' ', ' ', '#', '#', ' ', ' ', ' ', '#'], ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'], ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'], ['#', '#', ' ', ' ', ' ', ' ', ' ', ' ', '#', '#'], ['#', '#', '#', '#', '#', ' ', '#', '#', '#', '#']],
[['#', '#', '#', '#', '#', '#', '#', '#', '#', '#'], ['#', '#', '#', '#', ' ', ' ', '#', '#', '#', '#'], ['#', '#', '#', ' ', ' ', ' ', ' ', '#', '#', '#'], ['#', '#', ' ', ' ', ' ', ' ', ' ', ' ', '#', '#'], ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'], ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'], ['#', '#', ' ', ' ', ' ', ' ', ' ', ' ', '#', '#'], ['#', '#', '#', ' ', ' ', ' ', ' ', '#', '#', '#'], ['#', '#', '#', '#', '#', ' ', '#', '#', '#', '#']]
],
"DOWNRIGHT":[
[['#', '#', '#', '#', '#', ' ', '#', '#', '#', '#'], ['#', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', '#'], ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', '#'], ['#', '#', ' ', '#', ' ', '#', '#', '#', '#', '#'], ['#', '#', '#', '#', ' ', '#', '#', '#', '#', '#'], [' ', ' ', ' ', ' ', ' ', '#', '#', '#', '#', '#'], ['#', '#', '#', ' ', ' ', ' ', ' ', ' ', ' ', '#'], ['#', '#', '#', '#', '#', ' ', '#', ' ', '#', '#'], ['#', '#', '#', '#', '#', ' ', ' ', ' ', '#', '#'], ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#']],
[['#', '#', '#', '#', '#', ' ', '#', '#', '#', '#'], ['#', '#', ' ', ' ', ' ', ' ', ' ', ' ', '#', '#'], ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'], ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'], ['#', ' ', ' ', ' ', '#', '#', ' ', ' ', ' ', '#'], [' ', ' ', ' ', ' ', '#', '#', ' ', ' ', ' ', '#'], ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'], ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'], ['#', '#', ' ', ' ', ' ', ' ', ' ', ' ', '#', '#'], ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#']],
[['#', '#', '#', '#', '#', ' ', '#', '#', '#', '#'], ['#', '#', '#', '#', '#', ' ', '#', '#', '#', '#'], ['#', '#', '#', '#', ' ', ' ', ' ', '#', '#', '#'], ['#', '#', '#', ' ', ' ', ' ', ' ', ' ', '#', '#'], ['#', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'], ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#'], ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#'], ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#'], ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#']]
],
"DOWNLEFT":[
[['#', '#', '#', '#', ' ', '#', '#', '#', '#', '#'], ['#', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', '#'], ['#', ' ', '#', ' ', '#', ' ', '#', ' ', '#', '#'], ['#', '#', '#', ' ', '#', ' ', ' ', ' ', '#', '#'], ['#', ' ', ' ', ' ', ' ', ' ', '#', '#', '#', '#'], ['#', '#', '#', '#', '#', ' ', ' ', ' ', ' ', ' '], ['#', '#', '#', '#', ' ', ' ', ' ', ' ', ' ', '#'], ['#', '#', '#', ' ', ' ', ' ', ' ', ' ', '#', '#'], ['#', '#', ' ', ' ', ' ', ' ', ' ', '#', '#', '#'], ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#']],
[['#', '#', '#', '#', ' ', '#', '#', '#', '#', '#'], ['#', '#', ' ', ' ', ' ', ' ', ' ', ' ', '#', '#'], ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'], ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'], ['#', ' ', ' ', ' ', '#', '#', ' ', ' ', ' ', '#'], ['#', ' ', ' ', ' ', '#', '#', ' ', ' ', ' ', ' '], ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'], ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'], ['#', '#', ' ', ' ', ' ', ' ', ' ', ' ', '#', '#'], ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#']],
[['#', '#', '#', '#', ' ', '#', '#', '#', '#', '#'], ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'], ['#', ' ', '#', '#', '#', ' ', '#', '#', ' ', '#'], ['#', ' ', '#', '#', '#', ' ', '#', '#', ' ', '#'], ['#', ' ', '#', '#', '#', ' ', ' ', ' ', ' ', '#'], ['#', ' ', ' ', ' ', ' ', ' ', '#', '#', ' ', ' '], ['#', ' ', ' ', ' ', ' ', ' ', '#', '#', ' ', '#'], ['#', ' ', '#', '#', '#', ' ', ' ', ' ', ' ', '#'], ['#', ' ', '#', '#', '#', ' ', ' ', '#', ' ', '#'], ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#']]
]
}
image={
"Cockatrice":[[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', '~', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', '<', '0', '|', ' ', ' ',' ', ' ', ' '], [' ', ' ', ' ', '\\', '\\', '/', '~', ' ', ' ', ' '], [' ', ' ', ' ', ' ', 'M', ' ', '~', ' ', ' ', ' ']],
"Player":[[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', '~', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', '|', '0', '|', ' ', ' ', ' '], [' ', ' ', ' ', '[', '-', 'H', '-', '+', '-', ' '], [' ', ' ', ' ', ' ', ' ', 'M', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']],
"Mimic":[[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', '/', '/', ' ', '|', ' ', ' ', ' '], [' ', ' ', ' ', '|', '|', '0', '|', ' ', ' ', ' '], [' ', ' ', ' ', '\\', '\\', ' ', '|', ' ', ' ', ' '], [' ', ' ', ' ', ' ', 'm', 'm', 'm', ' ', ' ', ' ']],
"Armour":[[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', '_', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', '|', '~', '|', ' ', ' ', ' '], [' ', ' ', ' ', ' ', '/', 'H', '\\', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', 'H', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']],
"Juggernaut":[[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', '_', '_', ' ', ' ', ' ', ' '], [' ', ' ', ' ', '|', '=', '=', '|', ' ', ' ', ' '], [' ', ' ', ' ', ' ', '\\', '/', ' ', ' ', ' ', ' '], [' ', ' ', ' ', '/', ' ', ' ', '\\', ' ', ' ', ' '], [' ', ' ', ' ', '|', '/', '\\', '|', ' ', ' ', ' '], [' ', ' ', ' ', '0', ' ', ' ', '0', ' ', ' ', ' ']],
"Basilisk":[[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', '_', ' ', '_', ' ', '_', ' ', '_', ' ', '_'], ['/', '0', 'V', ' ', 'V', ' ', 'V', ' ', 'V', ' '], ['\\', '/', '\\', '/', '\\', '/', '\\', '/', '\\', '/'], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']],
"Bumbler":[[' ', ' ', '_', '_', ' ', ' ', '_', '_', ' ', ' '], [' ', '/', ' ', ' ', '\\', '/', ' ', ' ', ']', ' '], [' ', '\\', ' ', ' ', '_', '_', ' ', ' ', '/', ' '], [' ', ' ', '\\', '/', ' ', ' ', '\\', '/' , ' ', ' '], [' ', ' ', '|', '#', '#', '#', '#', '|', ' ', ' '], [' ', ' ', '|', ' ', ' ', ' ', ' ', '|', ' ', ' '], [' ', ' ', '|', '#', '#', '#', '#', '|', ' ', ' '], [' ', ' ', '|', ' ', '0', '0', ' ', '|', ' ', ' '], [' ', ' ', '|', ' ', ' ', ' ', ' ', '|', ' ', ' '], [' ', ' ', '\\', '_', '_', '_', '/', ' ', ' ', ' ']],
}
def printbattle(one,two):
	line=''
	linee=''
	for goes in range(10):
		line=''
		linee=''
		for object in image[one][goes]:
			line+=(object + ' ')
		for object in image[two][goes]:
			linee+=(object + ' ')
		sys.stdout.write(linee)
		print("			" + line)
#PUT THINGS THAT CAN'T BE WALKED THROUGH IN THE LIST UNDER HERE
gamedata = {"collisions":['#']}
gamedata['floor'] = 0
def flush():
	while msvcrt.kbhit():
		msvcrt.getwch()
def clear():
	os.system('cls' if os.name == 'nt' else 'clear')
class Character:
	def __init__(self, NAME, CHARACTERCLASS, STATS, EQUIP, MOVE, MONEY, SKIN):
		self.name = NAME
		self.cclass = CHARACTERCLASS
		self.stats = STATS
		self.equip = EQUIP
		self.moves = MOVE
		self.money = MONEY
		self.skin = SKIN
gamedata['player'] = Character('Aaron','Brawn',{'health':64,'attack':16,'defence':16,"maxhealth":64},{"weapon":['Annoying Wand',2,'Magic'],"shield":["Wheel",2,'Metal']},[['Dying Torch',2,'Fire']], 12, "Player")
gamedata['player'].name=input("YOUR NAME: ")
"""

BESTIARY

"Low Mimic":
	Character("'Chest'",'Mimic',{'health':floor+32,'attack':floor+16,'defence':floor+16,"maxhealth":floor+32},{"weapon":['Fangs',floor+2,'Beast'],"shield":["No Shield",0,'None']},[['Snap Shut',2,'Mimic']], ((floor*floor)+2), "Mimic")
"Low Haunted Armour":
	Character("'Armour'",'Mimic',{'health':floor+12,'attack':floor+10,'defence':floor+10,"maxhealth":floor+2},{"weapon":['Shady Sword',floor+4,'Shade'],"shield":["Living Tissue",floor+16,'Brawn']},[['Shadow Slice',2,'Mimic'],['Electric Jab',4,'Light'],['Goodknight',4,'Shade']], ((floor*floor)+2), "Armour")
"Low Cockatrice":
	Character("Cockatrice",'Dragon',{'health':floor+50,'attack':floor+25,'defence':floor+25,"maxhealth":floor+52},{"weapon":['Talons',floor+4,'Dragon'],"shield":["Parrying Talon",floor+2,'Metal']},[['Demonic Breath',2,'Shade'],['Dragon Talon', 10,'Dragon'],['Talon Slash',2,'Beast'],['Dragon Stare',16,'Dragon']], ((floor*floor*2)+6),"Cockatrice")
"Low Juggernaut":
	Character("Juggernaut",'Metal',{'health':floor+80,'attack':floor+15,'defence':floor+15,"maxhealth":floor+80},{"weapon":['Knuckledusters',floor+4,'Dragon'],"shield":["Buckler",floor+2,'Metal']},[['Comet Punch',2,'Metal'],['Dragon Punch', 10,'Dragon'],['Animal Summon',4,'Beast'],['Metallic Kick',4,'Dragon']], ((floor*floor*2)+6), "Juggernaut")
"Medium Mimic"
	Character("'Strongbox'",'Mimic',{'health':floor+50,'attack':floor+25,'defence':floor+25,"maxhealth":floor+52},{"weapon":['No Weapon',0,'None'],"shield":["Metal Lid",floor+12,'Metal']},[['Lockdown',2,'Shade'],['Tumbler I', 2,'Metal'],['Tumbler II', 4,'Metal'],['Tumbler III',6,'Metal']], ((floor*floor*2)+6),"Mimic")
"Juggernaut"
	Character("Basilisk",'Dragon',{'health':floor+70,'attack':floor+45,'defence':floor+45,"maxhealth":floor+62},{"weapon":['No Weapon',0,'None'],"shield":["Scales of Doom",floor+8,'Metal']},[['Glance',2,'Shade'],['Dragon Talon', 15,'Metal'],['Dragon Tail', random.randint(1,30),'Metal'],['Stare',8,'Shade']], ((floor*floor*2)+6),"Basilisk")
"""

def genbonus(move,play):
	if play =='enemy':
		notplay = 'player'
	else:
		notplay = 'enemy'
	bonus=1
	advan=gamedata['advantages'][move[2]]
	badvanone=gamedata['advantages'][gamedata[notplay].equip['shield'][2]]
	badvantwo=gamedata['advantages'][gamedata[notplay].cclass]
	if gamedata[notplay].cclass in advan:
		bonus+=0.21
	if gamedata[notplay].equip['shield'][2] in advan:
		bonus+=0.21
	if gamedata[play].cclass in [move[2],'Mimic']:
		bonus+=0.20
	if gamedata[play].cclass == gamedata['classlevel'][0]:
		bonus+=0.20
	if gamedata[play].equip['weapon'][2] in [move[2],'Mimic']:
		bonus+=0.20
	if move[2] in badvanone:
		bonus-=0.49
	if move[2] in badvantwo:
		bonus-=0.49
	if bonus > 1.5:
		print("It's Super Effective!")
	elif bonus < 0.5:
		print("It's not very effective!")
	if move[2] in ['Light','Shade','Water','Bloom']:
		bonus=bonus*1.5
	return bonus
def wave(move,play):
	print(str(gamedata[play].name)+" used "+str(move[0]))
	if play =='enemy':
		notplay = 'player'
	else:
		notplay = 'enemy'
	bonus=genbonus(move,play)
	dam=round( ( ( ( gamedata[play].stats['attack'] + gamedata[play].equip['weapon'][1] ) * move[1] ) / ( gamedata[notplay].stats['defence'] + gamedata[notplay].equip['shield'][1]) ) * bonus )
	gamedata[notplay].stats['health'] -= dam
	sys.stdout.write(str(gamedata[play].name))
	print(" dealt " + str(dam) + " damage")
	time.sleep(0.4)
def unchanging(move,play):
	print(str(gamedata[play].name)+" used "+str(move[0]))
	if play =='enemy':
		notplay = 'player'
	else:
		notplay = 'enemy'
	gamedata[notplay].stats['health'] -= move[1]
	sys.stdout.write(gamedata[play].name)
	print(" dealt " + str(move[1]) + " damage")
	time.sleep(0.4)
def spell(move,play):
	print(str(gamedata[play].name)+" used "+str(move[0]))
	if play =='enemy':
		notplay = 'player'
	else:
		notplay = 'enemy'
	bonus=genbonus(move,play)
	dam=round( ( ( ( gamedata[play].stats['attack'] + gamedata[play].equip['weapon'][1] ) * move[1] ) / ( gamedata[notplay].stats['defence'] + gamedata[notplay].equip['shield'][1]) ) * bonus )
	gamedata[notplay].stats['health'] -= dam
	gamedata[play].stats['health'] -= round(dam/4)
	sys.stdout.write(gamedata[play].name)
	print(" dealt " + str(dam) + " damage")
	time.sleep(0.2)
	print("Took " + str(round(dam/4)) + " damage in karma")
	time.sleep(0.2)
def impact(move,play):
	print(str(gamedata[play].name)+" used "+str(move[0]))
	if play =='enemy':
		notplay = 'player'
	else:
		notplay = 'enemy'
	bonus=genbonus(move,play)
	dam=round( ( ( ( gamedata[play].stats['attack'] + gamedata[play].equip['weapon'][1] ) * move[1] ) / ( gamedata[notplay].stats['defence'] + gamedata[notplay].equip['shield'][1]) ) * bonus )
	gamedata[notplay].stats['health'] -= dam
	sys.stdout.write(gamedata[play].name)
	print(" dealt " + str(dam) + " damage")
	time.sleep(0.4)
def blast(move,play):
	print(str(gamedata[play].name)+" used "+str(move[0]))
	if play =='enemy':
		notplay = 'player'
	else:
		notplay = 'enemy'
	bonus=genbonus(move,play)
	dam=round( ( ( ( gamedata[play].stats['attack'] + gamedata[play].equip['weapon'][1] ) * move[1] ) / ( gamedata[notplay].stats['defence'] + gamedata[notplay].equip['shield'][1]) ) * bonus )
	dam=random.randint(0,dam*2)
	gamedata[notplay].stats['health'] -= dam
	sys.stdout.write(gamedata[play].name)
	print(" dealt " + str(dam) + " damage")
	time.sleep(0.4)
gamedata['universe'] = 1
gamedata['maxuniverse'] = 10
gamedata['advantages'] = {
"Light":["Metal","Water","Shade"],
"Shade":["Knowledge","Magic","Range"],
"Magic":["Fire","Water","Bloom","Dragon"],
"Metal":["Brawn","Beast","Bloom"],
"Knowledge":["Mimic","Beast","Brawn"],
"Water":["Fire","Earth","Metal"],
"Fire":["Bloom","Beast","Shade"],
"Bloom":["Water","Earth","Light"],
"Earth":["Fire","Light","Metal"],
"Beast":["Magic","Delicate","Bloom"],
"Brawn":["Delicate","Beast","Earth"],
"Range":["Brawn","Metal","Delicate"],
"Delicate":["Light","Shade","Knowledge"],
"Mimic":["N/A"],
"Dragon":["Bloom","Fire","Wake"],
"None":["N/A"]
}
gamedata['typecasts'] = {
"Light":wave,
"Shade":wave,
"Magic":spell,
"Metal":impact,
"Knowledge":spell,
"Water":wave,
"Fire":blast,
"Bloom":wave,
"Earth":wave,
"Beast":impact,
"Brawn":impact,
"Range":blast,
"Delicate":spell,
"Mimic":impact,
"Dragon":unchanging,
"None":unchanging
}
gamedata['sufkeys'] = {
"Light":'wave',
"Shade":'wave',
"Magic":'spell',
"Metal":'impact',
"Knowledge":'spell',
"Water":'wave',
"Fire":'blast',
"Bloom":'wave',
"Earth":'wave',
"Beast":'impact',
"Brawn":'impact',
"Range":'blast',
"Delicate":'spell',
"Mimic":'impact',
"Dragon":'unchanging',
"None":'impact'
}
gamedata['loottable'] = dict()
gamedata['loottable']['shield'] = {
0:[
['Wheel',3,'Metal'],
["'Circle'",2,'Mimic'],
['Circle of the Beast',3,'Beast'],
['Boxing Ring',3,'Brawn'],
['Circle of Crystal',3,'Delicate'],
['Arena',3,'Range'],
['Circle of Obsidian',3,'Shade'],
['Circle of Curses',3,'Magic'],
['Spotlight',3,'Light'],
['Coiled Snake',5,'Dragon'],
['Circle of the Hell',3,'Fire'],
['Droplet',3,'Water'],
['Crop Circle',3,'Bloom'],
['Shockwave',3,'Earth'],
['Social Circle',3,'Knowledge']
],
8:[
['Buckler',9,'Metal'],
["'Buckler'",7,'Mimic'],
['Buckler of the Beast',9,'Beast'],
['Buckler of Strength',10,'Brawn'],
['Crystal Buckler',9,'Delicate'],
['Buckler of the Hunt',8,'Range'],
['Obsidian Buckler',9,'Shade'],
['Charming Buckler',10,'Magic'],
['Conductive Buckler',9,'Light'],
['Dragonhide Buckler',12,'Dragon'],
['Infernal Buckler',9,'Fire'],
['Basin',9,'Water'],
['Ironwood Buckler',9,'Bloom'],
['Clay Buckler',9,'Earth'],
['Buckler of Influence',9,'Knowledge']
],
16:[
['Shield',15,'Metal'],
["'Shield'",13,'Mimic'],
["Shield of the Beast",16,'Beast'],
["Shield of Strength",16,'Brawn'],
["Glass Shield",14,'Delicate'],
["Shield of the Hunt",14,'Range'],
["Shield of Obsidian",15,'Shade'],
["Hex-Shield",16,'Magic'],
['Refractor',15,'Light'],
['Cockatrice Wing',19,'Dragon'],
['Infernal Wall',15,'Fire'],
['Deluge Front',15,'Water'],
['Husk',15,'Bloom'],
['Tectonic Plate',15,'Earth'],
['Flurry of Pages',15,'Knowledge']
],
26:[
['Barrier',19,'Metal'],
["'Basilisk Claw Barrier'",17,'Mimic'],
['Barrier of the Beast',20,'Beast'],
['Barrier of Brawn',20,'Brawn'],
['Glass Barrier',18,'Delicate'],
['Barrier of the Hunt',18,'Range'],
['Vantablock',19,'Shade'],
['Hex-agon',20,'Magic'],
['Mirror',19,'Light'],
['Basilisk Claw Barrier',23,'Dragon'],
['Flame Barrier',19,'Fire'],
['Solvent Front',19,'Water'],
['Bale Barricade',19,'Bloom'],
['Plateau',19,'Earth'],
['Bookcase Barrier',19,'Knowledge']
],
32:[
['Panel of Ore',23,'Metal'],
['Panel of Duplication',21,'Mimic'],
['Panel of the Beast',24,'Beast'],
['Panel of Strength',24,'Brawn'],
['Panel of Crystal',22,'Delicate'],
['Panel of the Hunt',22,'Range'],
['Panel of Obsidian',23,'Shade'],
['Panel of Curses',24,'Magic'],
['Panel of Lustre',23,'Light'],
['Panel of the Dragon',27,'Dragon'],
['Panel of the Underworld',23,'Fire'],
['Panel of the Ocean',23,'Water'],
['Panel of the Harvest',23,'Bloom'],
['Panel of the Quake',23,'Earth'],
['Panel of Influence',23,'Knowledge']
],
40:[
['Cage of Ore',27,'Metal'],
['Cage of Duplication',25,'Mimic'],
['Cage of the Beast',28,'Beast'],
['Cage of Strength',28,'Brawn'],
['Cage of Crystal',26,'Delicate'],
['Cage of the Hunt',28,'Range'],
['Cage of Obsidian',27,'Shade'],
['Cage of Curses',28,'Magic'],
['Cage of Lustre',27,'Light'],
['Cage of the Dragon',31,'Dragon'],
['Cage of the Underworld',27,'Fire'],
['Cage of the Ocean',27,'Water'],
['Cage of the Harvest',27,'Bloom'],
['Cage of the Quake',27,'Earth'],
['Cage of Influence',27,'Knowledge']
],
48:[
['Deflector of Ore',31,'Metal'],
['Deflector of Duplication',29,'Mimic'],
['Deflector of the Beast',32,'Beast'],
['Deflector of Strength',32,'Brawn'],
['Deflector of Crystal',30,'Delicate'],
['Deflector of the Hunt',30,'Range'],
['Deflector of Obsidian',31,'Shade'],
['Deflector of Curses',32,'Magic'],
['Deflector of Lustre',31,'Light'],
['Deflector of the Dragon',35,'Dragon'],
['Deflector of the Underworld',31,'Fire'],
['Deflector of the Ocean',31,'Water'],
['Deflector of the Harvest',31,'Bloom'],
['Deflector of the Quake',31,'Earth'],
['Deflector of Influence',31,'Knowledge'],
]
}
gamedata['loottable']['weapon'] = {
0:[
['Hunk Of Junk',3,'Metal'],
["'Fire Knife''",2,'Mimic'],
['Collar',3,'Beast'],
['Boxing Glove',3,'Brawn'],
['Mirror Shard',3,'Delicate'],
['Stick & String',3,'Range'],
['Dark Glove',3,'Shade'],
['Abraccadabra',3,'Magic'],
['Unibeam Glove',3,'Light'],
['Fangs of the Snake',5,'Dragon'],
['Fire Knife',3,'Fire'],
['Aqua Sapphire',3,'Water'],
['Manure',3,'Bloom'],
['Earthen Club',3,'Earth'],
['Basic Book',3,'Knowledge']
],
2:[
['Broken Sword',5,'Metal'],
["'Stirrup'",4,'Mimic'],
['Stirrup',5,'Beast'],
['Knuckleduster',5,'Brawn'],
['Glass Knife',5,'Delicate'],
['Tiny Bow',5,'Range'],
['Coal Dust',5,'Shade'],
['Hocus Pocus',5,'Magic'],
['Duobeam Glove',5,'Light'],
['Claws of the Gecko',7,'Dragon'],
['Fire Dagger',5,'Fire'],
['Storm Drainer',5,'Water'],
['Fertiliser',5,'Bloom'],
['Stomping Stones',5,'Earth'],
['Intermediate Book',5,'Knowledge']
],
4:[
['Shortsword',7,'Metal'],
["'Cestus'",5,'Mimic'],
['Saddle',7,'Beast'],
['Cestus',7,'Brawn'],
['Glass Dagger',7,'Delicate'],
['Shortbow',7,'Range'],
['Pmal',7,'Shade'],
['3x2(9yz)4a',7,'Magic'],
['Tribeam Glove',7,'Light'],
['Poison of the Monitor Lizard',9,'Dragon'],
['Fire Sword',7,'Fire'],
['Tempest Wave',7,'Water'],
['Staff of Growth',7,'Bloom'],
["Gaia's Wrath",7,'Earth'],
['Advanced Book',7,'Knowledge']
],
8:[
['Longsword',9,'Metal'],
["'Typhoon Staff'",7,'Mimic'],
['Harness',9,'Beast'],
['Katar',10,'Brawn'],
['Glass Shortsword',9,'Delicate'],
['Longbow',8,'Range'],
['Blub',9,'Shade'],
['Voilatile Scepter',10,'Magic'],
['Tetrabeam Glove',9,'Light'],
['Fangs of the Komodo',12,'Dragon'],
['Burning Blade',9,'Fire'],
['Typhoon Staff',9,'Water'],
['Harvest Scythe',9,'Bloom'],
['Terrablade',9,'Earth'],
['Basic Scroll',9,'Knowledge']
],
12:[
['Claymore',11,'Metal'],
["'Lucky Charm'",9,'Mimic'],
['Bola',12,'Beast'],
['Mubuchae',12,'Brawn'],
['Glass Longsword',10,'Delicate'],
['Compound Bow',10,'Range'],
['Tnecsednacni',11,'Shade'],
['Lucky Charm',12,'Magic'],
['Quinbeam Glove',11,'Light'],
['Dragonfire Flask',15,'Dragon'],
['Firestorm Vortex',11,'Fire'],
['Flood Bucket',11,'Water'],
['Hay Presto',11,'Bloom'],
['Power Globe',11,'Earth'],
['Intermediate Scroll',11,'Knowledge']
],
18:[
['Cutlass',15,'Metal'],
["'Glass Gladius'",13,'Mimic'],
['Boomerang',16,'Beast'],
['Deerhorn Knives',16,'Brawn'],
['Glass Gladius',14,'Delicate'],
['Crossbow',14,'Range'],
['Tnecseroulf',15,'Shade'],
['Amburlet',16,'Magic'],
['Unibeam Gauntlet',15,'Light'],
['Cockatrice Claw',19,'Dragon'],
['Hellfire Chain',15,'Fire'],
['Deluge Chalice',15,'Water'],
['Cereal Killer',15,'Bloom'],
['Tectonic Plating',15,'Earth'],
['Advanced Scroll',15,'Knowledge']
],
26:[
['Katana',19,'Metal'],
["'Obsidian Blade'",17,'Mimic'],
['Boar Spear',20,'Beast'],
['Sword Gauntlet',20,'Brawn'],
['Glass Cleaver',18,'Delicate'],
['Javelin',18,'Range'],
['Obsidian Blade',19,'Shade'],
['Hex-agon',20,'Magic'],
['Duobeam Gauntlet',19,'Light'],
['Basilisk Venom Dagger',23,'Dragon'],
['Soulburner',19,'Fire'],
['Inundator',19,'Water'],
['Daybale',19,'Bloom'],
['Miniature Moon',19,'Earth'],
['Basic Tome',19,'Knowledge']
],
32:[
['Gem of Ore',23,'Metal'],
["'Gem of the Dragon'",21,'Mimic'],
['Gem of the Beast',24,'Beast'],
['Gem of Strength',24,'Brawn'],
['Gem of Crystal',22,'Delicate'],
['Gem of the Hunt',22,'Range'],
['Gem of Obsidian',23,'Shade'],
['Gem of Curses',24,'Magic'],
['Gem of Lustre',23,'Light'],
['Gem of the Dragon',27,'Dragon'],
['Gem of the Underworld',23,'Fire'],
['Gem of the Ocean',23,'Water'],
['Gem of the Harvest',23,'Bloom'],
['Gem of the Quake',23,'Earth'],
['Gem of Influence',23,'Knowledge']
],
40:[
['Sphere of Ore',27,'Metal'],
["'Sphere of the Quake'",25,'Mimic'],
['Sphere of the Beast',28,'Beast'],
['Sphere of Strength',28,'Brawn'],
['Sphere of Crystal',26,'Delicate'],
['Sphere of the Hunt',28,'Range'],
['Sphere of Obsidian',27,'Shade'],
['Sphere of Curses',28,'Magic'],
['Sphere of Lustre',27,'Light'],
['Sphere of the Dragon',31,'Dragon'],
['Sphere of the Underworld',27,'Fire'],
['Sphere of the Ocean',27,'Water'],
['Sphere of the Harvest',27,'Bloom'],
['Sphere of the Quake',27,'Earth'],
['Sphere of Influence',27,'Knowledge']
],
48:[
['Orb of Ore',31,'Metal'],
["'Orb of the Underworld'",29,'Mimic'],
['Orb of the Beast',32,'Beast'],
['Orb of Strength',32,'Brawn'],
['Orb of Crystal',30,'Delicate'],
['Orb of the Hunt',30,'Range'],
['Orb of Obsidian',31,'Shade'],
['Orb of Curses',32,'Magic'],
['Orb of Lustre',31,'Light'],
['Orb of the Dragon',35,'Dragon'],
['Orb of the Underworld',31,'Fire'],
['Orb of the Ocean',31,'Water'],
['Orb of the Harvest',31,'Bloom'],
['Orb of the Quake',31,'Earth'],
['Orb of Influence',31,'Knowledge'],
]
}
gamedata['moveprefix'] = {
"Light":["Glowing","Luminous","Shining"],
"Shade":["Dim","Darkened","Void"],
"Magic":["Arcane","Esoteric","Eldritch"],
"Metal":["Copper","Iron","Steel"],
"Knowledge":["Basic","Intermediate","Advanced"],
"Water":["Flowing","Rushing","Crashing"],
"Fire":["Dying","Burning","Roaring"],
"Bloom":["Growing","Sprouting","Photosynthesising"],
"Earth":["Vibrating","Shaking","Quaking"],
"Beast":["Well Done","Medium Rare","Rare"],
"Brawn":["Weak","Strong","Forceful"],
"Range":["Nearby","Far","Long"],
"Delicate":["Light","Dainty","Elegant"],
"Mimic":["Weak","Strong","Forceful"],
"Dragon":["Reptilian","Draconic","Demonic"],
"None":['Basic','Complex','Ultimate']
}
gamedata['classlevel'] = ["Knowledge","Light","Shade","Magic","Metal","Knowledge","Water","Fire","Bloom","Earth","Beast","Brawn","Range","Delicate","Mimic","Dragon"]
gamedata['movesuffix'] = {
"wave":["Stream","Wake","Flood"],
"spell":["Whispers","Chant","Spell"],
"blast":["Shot","Double-Shot","Volley"],
"impact":["Hit","Slam","Strike"],
"unchanging":["Claw","Breath","Blast"],
}
def gen_weapon (classs):
	one = gamedata['loottable']['weapon']
	two = list(one.keys())
	three=list()
	for object in two:
		if object <= gamedata['floor']:
			three.append(object)
	four= list()
	for object in three:
		for object in one[object]:
			if object[2] == classs:
				four.append(object)
	random.shuffle(four)
	return(four[0])
def gen_shield (classs):
	one = gamedata['loottable']['shield']
	two = list(one.keys())
	three=list()
	for object in two:
		if object <= gamedata['floor']:
			three.append(object)
	four= list()
	for object in three:
		for object in one[object]:
			if object[2] == classs:
				four.append(object)
	random.shuffle(four)
	return(four[0])
def genmove(classs,floorr):
	if classs == 'Dragon':
		one = random.randint(0,2)
		two = random.randint(0,2)
		four = str(gamedata['moveprefix']['Dragon'][one] + " " + gamedata['movesuffix']['unchanging'][two])
		one+=1
		two+=1
		three = random.randint(1,round((one+two)*floorr))
		return [four, three, classs]
	else:
		one = random.randint(0,2)
		two = random.randint(0,2)
		three = one + two +floorr +2
		three = three * floorr
		three = random.randint(1,three)
		four = str(gamedata['moveprefix'][classs][one] + " " + gamedata['movesuffix'][gamedata['sufkeys'][classs]][two])
		return [four, three, classs]
def get_weapon (weapon):
	one = gamedata['player'].equip['weapon']
	print("YOU FOUND:\n***\n" + str(weapon[0].upper()) + "\n---\n	Power: " + str(weapon[1]) + "\n	Class: " + str(weapon[2]) + "\n***")
	print("YOU ARE CURRENTLY HOLDING:\n***\n" + str(one[0]).upper() + "\n---\n	Power: " + str(one[1]) + "\n	Class: " + str(one[2]) + "\n***\n\nReplace your current weapon?\nAnswer Y, YES, N or NO")
	while True:
		flush()
		two = input("ANSWER: ").lower()
		if two in ['y','yes','n','no']:
			break
	if two in ['y','yes']:
		gamedata['player'].equip['weapon'] = weapon
	else:
		print("You ignored the weapon.")
def get_shield (weapon):
	one = gamedata['player'].equip['shield']
	print("YOU FOUND:\n***\n" + str(weapon[0].upper()) + "\n---\n	Power: " + str(weapon[1]) + "\n	Class: " + str(weapon[2]) + "\n***")
	print("YOU ARE CURRENTLY HOLDING:\n***\n" + str(one[0]).upper() + "\n---\n	Power: " + str(one[1]) + "\n	Class: " + str(one[2]) + "\n***\n\nReplace your current shield?\nAnswer Y, YES, N or NO")
	while True:
		flush()
		two = input("ANSWER: ").lower()
		if two in ['y','yes','n','no']:
			break
	if two in ['y','yes']:
		gamedata['player'].equip['shield'] = weapon
	else:
		print("You ignored the dhield.")
def learn_move(movee):
	if not movee in gamedata['player'].moves:
		print("***\n" + str(movee[0]).upper() + "\n---\n	Power: " + str(movee[1]) + "\n	Class: " +str(movee[2]).upper()+"\n***")
		if len(gamedata['player'].moves) >3:
			count = 0
			for object in gamedata['player'].moves:
				count+=1
				print(str(count) + " " + str(object[0]) +"\n	Power: " + str(object[1]) + "	Class: " + object[2])
			while True:
				try:
					flush()
					gamedata['input'] = input("NUMBER: ").lower()
					if not gamedata['input'] == 'cancel':
						gamedata['input'] = round(int(gamedata['input']) - 1)
				except Exception:
					continue
				choices=list(range(len(gamedata['player'].moves)))
				choices.append('cancel')
				if gamedata['input'] in choices:
					break
			if not gamedata['input'] == 'cancel':
				print("Replaced " + str(gamedata['player'].moves[gamedata['input']][0]) +" with " + str(movee[0]))
				gamedata['player'].moves[gamedata['input']] = movee
			else:
				print("You decided not to learn the move.")
		else:
			gamedata['player'].moves.append(movee)
			print("Learned " + str(movee[0]))
	else:
		print("Sorry, you already know that move.")
def battle(bestiary) :
	gamedata['enemy'] = bestiary
	while True:
		flush()
		clear()
		printbattle(gamedata['enemy'].skin,gamedata['player'].skin)
		print("BATTLE:\n    YOU: " + gamedata['player'].name + " Health: " + str(gamedata['player'].stats['health']) + "\n  ENEMY: " + gamedata['enemy'].name + " Health: " + str(gamedata['enemy'].stats['health']) + "\n***")
		time.sleep(0.1)
		if gamedata['enemy'].stats['health']<1:
			print("Found $" + str(gamedata['enemy'].money))
			gamedata['player'].money += gamedata['enemy'].money
			gamedata['win'] = True
			break
		elif gamedata['player'].stats['health']<1:
			clear()
			print("You lose!")
			print("Lost $" + str(gamedata['enemy'].money))
			gamedata['player'].stats['health'] = 10
			gamedata['player'].money -= gamedata['enemy'].money
			time.sleep(2)
			gamedata['win'] = False
			break
		print("YOUR MOVES: ")
		count=0
		for object in gamedata['player'].moves:
			count+=1
			print(str(count)+": "+str(object[0]))
		while True:
			try:
				gamedata['input'] = int(input("MOVE NUMBER: "))
			except Exception:
				continue
			if gamedata['input']<=count:
				break
		gamedata['typecasts'][gamedata['player'].moves[gamedata['input']-1][2]](gamedata['player'].moves[gamedata['input']-1],'player')
		if gamedata['enemy'].stats['health']<1:
			print("Found $" + str(gamedata['enemy'].money))
			gamedata['player'].money += gamedata['enemy'].money
			gamedata['win'] = True
			break
		elif gamedata['player'].stats['health']<1:
			clear()
			print("You lose!")
			print("Lost $" + str(gamedata['enemy'].money))
			gamedata['player'].stats['health'] = 10
			gamedata['player'].money -= gamedata['enemy'].money
			time.sleep(2)
			gamedata['win'] = False
			break
		random.shuffle(gamedata['enemy'].moves)
		gamedata['typecasts'][gamedata['enemy'].moves[0][2]](gamedata['enemy'].moves[0],'enemy')
		if gamedata['enemy'].stats['health']<1:
			print("Found $" + str(gamedata['enemy'].money))
			gamedata['player'].money += gamedata['enemy'].money
			gamedata['win'] = True
			break
		elif gamedata['player'].stats['health']<1:
			clear()
			print("You lose!")
			print("Lost $" + str(gamedata['enemy'].money))
			gamedata['player'].stats['health'] = 10
			gamedata['player'].money -= gamedata['enemy'].money
			time.sleep(2)
			gamedata['win'] = False
			break
		input("\n***\nPress enter to continue\n")
	if gamedata['win'] == True:
		if random.randint(1,5) == 1:
			print("You absorbed some of the enemy's vitality")
			gamedata['player'].stats['maxhealth']+=4
		if random.randint(1,5) == 1:
			print("You absorbed some of the enemy's strength")
			gamedata['player'].stats['attack']+=1
		if random.randint(1,5) == 1:
			print("You absorbed some of the enemy's durability")
			gamedata['player'].stats['defence']+=2
	if gamedata['win'] == False and gamedata['player'].money < 1:
		while True:
			clear()
			print("You lose!")
	time.sleep(2)
	clear()
	print("Move to continue")
	floor_display()
	print("COORDINATES:"+str(gamedata['location']))
def place_thing(thing,scatter):
	for goes in range(scatter):
		one=random.randint(1,19)
		two=random.randint(1,19)
		if gamedata['output'][one][two] == ' ':
			gamedata['output'][one][two] = thing
def floor_generate():
	gamedata['visibility']=[]
	for goes in range(20):
		gamedata['visibility'].append([])
		for goes in range(20):
			gamedata['visibility'][-1].append('#')
	gamedata['floor'] += 1
	random.shuffle(gamedata['classlevel'])
	gamedata['output'] = []
	random.shuffle(presets["UPRIGHT"])
	random.shuffle(presets["UPLEFT"])
	random.shuffle(presets["DOWNRIGHT"])
	random.shuffle(presets["DOWNLEFT"])
	temp=[]
	for goes in range(10):
		temp.append([])
		for object in presets["UPLEFT"][0][goes]:
			temp[-1].append(object)
		for object in presets["UPRIGHT"][0][goes]:
			temp[-1].append(object)
	for goes in range(10):
		temp.append([])
		for object in presets["DOWNLEFT"][0][goes]:
			temp[-1].append(object)
		for object in presets["DOWNRIGHT"][0][goes]:
			temp[-1].append(object)
	gamedata['output'] = temp
	place_thing('X',random.randint(1,gamedata['floor']+16))
	place_thing('H',random.randint(1,gamedata['floor']+16))
	place_thing('F',random.randint(1,(50-gamedata['floor'])))
	place_thing('*',random.randint(1,gamedata['floor']+16))
	place_thing('%',15)
	place_thing('R',1)
	if gamedata['floor'] > 4:
		place_thing('@',1)
	while True:
		rand1=random.randint(0,19)
		rand2=random.randint(0,19)
		gamedata['location'] = [rand1,rand2]
		if gamedata['output'][rand1][rand2] == ' ':
			break
	while True:
		rand1=random.randint(0,19)
		rand2=random.randint(0,19)
		gamedata['stairs'] = [rand1,rand2]
		if gamedata['output'][rand1][rand2] == ' ':
			break
def floor_display():
	clear_view()
	print("Radar * Floor " + str(gamedata['floor']) + " * Universe " + str(gamedata['universe']))
	for goes in range(20):
		go1=goes
		for goes in range(20):
			go2=goes
			if not gamedata['visibility'][go1][go2] == '#':
				if [go1,go2]==gamedata['location']:
					sys.stdout.write('O ')
				elif [go1,go2]==gamedata['stairs']:
					sys.stdout.write('^ ')
				else:
					sys.stdout.write(gamedata['output'][go1][go2] + " ")
			else:
				sys.stdout.write('~ ')
		print("")
	location=gamedata['location']
	stairs=gamedata['stairs']
	print("Floor Class: " + gamedata['classlevel'][0])
	if gamedata['location'][0] > gamedata['stairs'][0]:
		print("You are " + str(location[0] - stairs[0]) + " metres below the stairs")
	elif gamedata['location'][0] < gamedata['stairs'][0]:
		print("You are " + str(stairs[0] - location[0]) + " metres above the stairs")
	else:
		print("You're standing on the same column as the stairs!")
	if gamedata['location'][1] > gamedata['stairs'][1]:
		print("You are " + str(location[1] - stairs[1]) + " metres to the right of the stairs")
	elif gamedata['location'][1] < gamedata['stairs'][1]:
		print("You are " + str(stairs[1] - location[1]) + " metres to the left of the stairs")
	else:
		print("You're standing on the same row as the stairs!")
def testcollision(y,x):
	if not gamedata['output'][gamedata['location'][0] + y][gamedata['location'][1] + x] in gamedata['collisions']:
		return True
	else:
		return False
def clear_view():
	gamedata['visibility'][gamedata['location'][0]][gamedata['location'][1]] = ' '
	gamedata['visibility'][gamedata['location'][0]][gamedata['location'][1]-1] = ' '
	gamedata['visibility'][gamedata['location'][0]][gamedata['location'][1]+1] = ' '
	gamedata['visibility'][gamedata['location'][0]-1][gamedata['location'][1]-1] = ' '
	gamedata['visibility'][gamedata['location'][0]-1][gamedata['location'][1]] = ' '
	gamedata['visibility'][gamedata['location'][0]-1][gamedata['location'][1]+1] = ' '
	gamedata['visibility'][gamedata['location'][0]+1][gamedata['location'][1]-1] = ' '
	gamedata['visibility'][gamedata['location'][0]+1][gamedata['location'][1]] = ' '
	gamedata['visibility'][gamedata['location'][0]+1][gamedata['location'][1]+1] = ' '
while True:
	if gamedata['floor'] > 50:
		break
	floor=gamedata['floor']
	clear()
	floor_generate()
	floor_display()
	while True:
		while True:
			gamedata['input'] = (str(msvcrt.getch())[2])
			if gamedata['input'] in ['w','a','s','d','e','q']:
				if gamedata['input'] == 'w' and testcollision(-1,0):
					gamedata['location'][0] -= 1
				if gamedata['input'] == 's' and testcollision(1,0):
					gamedata['location'][0] += 1
				if gamedata['input'] == 'a' and testcollision(0,-1):
					gamedata['location'][1] -= 1
				if gamedata['input'] == 'd' and testcollision(0,1):
					gamedata['location'][1] += 1
				if gamedata['input'] == 'e':
					input("***\nYOUR STATS\n---\nNAME: " + str(gamedata['player'].name) + "\nClass:" + str(gamedata['player'].cclass) + "\nCombat Stats\n	HEALTH: " + str(gamedata['player'].stats['health']) + "\n	ATTACK: " + str(gamedata['player'].stats['attack']) + "\n	DEFENCE: " + str(gamedata['player'].stats['defence']) + "\nEquipment:\n	Weapon: \n		Name: " + str(gamedata['player'].equip['weapon'][0]) + "\n		Power: " + str(gamedata['player'].equip['weapon'][1]) + "\n		Class: " + str(gamedata['player'].equip['weapon'][2]) + "\n	Shield:\n		Name: " + str(gamedata['player'].equip['shield'][0]) + "\n		Power: " + str(gamedata['player'].equip['shield'][1]) + "\n		Class: " + str(gamedata['player'].equip['shield'][2]) + "\nMoney: " + str(gamedata['player'].money) + "\n***\nPress enter to continue\n")
				if gamedata['input'] == 'q':
					print("***\nYOUR MOVES\n---")
					for object in gamedata['player'].moves:
						print(str(object[0].upper()) + "\n	Power: " + str(object[1]) + "\n	Class: " + str(object[2]))
					input('***')
			break
		clear()
		floor_display()
		if gamedata['output'][gamedata['location'][0]][gamedata['location'][1]] == 'X':
			if floor < 6 and random.randint(1,3) > 1:
				if random.randint(1,10) == 1:
					battle(Character("Cockatrice",'Dragon',{'health':floor+50,'attack':floor+25,'defence':floor+25},{"weapon":['Talons',floor+4,'Dragon'],"shield":["Parrying Talon",floor+2,'Metal']},[['Demonic Breath',2,'Shade'],['Dragon Talon', 10,'Dragon'],['Talon Slash',2,'Beast'],['Dragon Stare',16,'Dragon']], (floor*floor*2)+6 , "Cockatrice"))
				else:
					battle(Character("'Chest'",'Mimic',{'health':floor+32,'attack':floor+16,'defence':floor+16},{"weapon":['Fangs',floor+2,'Beast'],"shield":["No Shield",0,'None']},[['Snap Shut',2,'Mimic']], (floor*floor)+2 ,"Mimic"))
			elif floor <13 and floor >5 and random.randint(1,3) > 1:
				if random.randint(1,10) ==1:
					battle(Character("Basilisk",'Dragon',{'health':floor+70,'attack':floor+45,'defence':floor+45,"maxhealth":floor+62},{"weapon":['No Weapon',0,'None'],"shield":["Scales of Doom",floor+8,'Metal']},[['Glance',2,'Shade'],['Dragon Talon', 15,'Metal'],['Dragon Tail', random.randint(1,30),'Metal'],['Stare',8,'Shade']], ((floor*floor*2)+6),"Basilisk"))
				else:
					battle(Character("'Strongbox'",'Mimic',{'health':floor+50,'attack':floor+25,'defence':floor+25,"maxhealth":floor+52},{"weapon":['No Weapon',0,'None'],"shield":["Metal Lid",floor+12,'Metal']},[['Lockdown',2,'Shade'],['Tumbler I', 2,'Metal'],['Tumbler II', 4,'Metal'],['Tumbler III',6,'Metal']], ((floor*floor*2)+6),"Mimic"))
			else:
				get_weapon(gen_weapon(gamedata['classlevel'][0]))
			gamedata['output'][gamedata['location'][0]][gamedata['location'][1]]=' '
		if gamedata['output'][gamedata['location'][0]][gamedata['location'][1]] == 'H':
			if floor < 6 and random.randint(1,3) > 1:
				if random.randint(1,10) == 1:
					battle(Character("Juggernaut",'Metal',{'health':floor+80,'attack':floor+15,'defence':floor+15,"maxhealth":floor+80},{"weapon":['Knuckledusters',floor+4,'Metal'],"shield":["Buckler",floor+2,'Metal']},[['Comet Punch',2,'Metal'],['Dragon Punch', 10,'Dragon'],['Animal Summon',6,'Beast'],['Metallic Kick',4,'Metal']], (floor*floor*2)+6,"Juggernaut"))
				else:
					battle(Character("'Armour'",'Mimic',{'health':floor+12,'attack':floor+10,'defence':floor+10,"maxhealth":floor+12},{"weapon":['Shady Sword',floor+4,'Shade'],"shield":["Living Tissue",floor+16,'Brawn']},[['Shadow Slice',2,'Mimic'],['Electric Jab',4,'Light'],['Goodknight',4,'Shade']], (floor*floor)+2,"Armour"))
			else:
				get_shield(gen_shield(gamedata['classlevel'][0]))
			gamedata['output'][gamedata['location'][0]][gamedata['location'][1]]=' '
		if gamedata['output'][gamedata['location'][0]][gamedata['location'][1]] == 'F':
			gamedata['player'].stats['health'] = gamedata['player'].stats['maxhealth']
			print("Rejuvenated you!")
		if gamedata['output'][gamedata['location'][0]][gamedata['location'][1]] == '*':
			if random.randint(1,10) >4:
				learn_move(genmove(gamedata['classlevel'][0],1))
			elif not gamedata['player'].cclass == gamedata['classlevel'][0]:
				print("Do you want to switch your class from " + str(gamedata['player'].cclass).upper() + " to " + str(gamedata['classlevel'][0]).upper() + "?\nAnswer y, yes, n or no.")
				gamedata['input'] = 'lol'
				while not gamedata['input'] in ['y','n','yes','no']:
					flush()
					gamedata['input'] = input("ANSWER: ")
				if gamedata['input'] in ['y','yes']:
					print("Switched your class from " + str(gamedata['player'].cclass).upper() + " to " + str(gamedata['classlevel'][0]).upper() + ".")
					gamedata['player'].cclass = gamedata['classlevel'][0]
			gamedata['output'][gamedata['location'][0]][gamedata['location'][1]]=' '
		if gamedata['output'][gamedata['location'][0]][gamedata['location'][1]] == '%':
			random.shuffle(gamedata['player'].moves)
			gamedata['temporary'] = 1
			while True:
				gamedata['temporary'] += 1
				rand1=random.randint(0,19)
				rand2=random.randint(0,19)
				gamedata['location'] = [rand1,rand2]
				if gamedata['output'][rand1][rand2] == ' ':
					if gamedata['temporary']>40 or gamedata['visibility'][rand1][rand2] == '#':
						break
		if gamedata['output'][gamedata['location'][0]][gamedata['location'][1]] == 'R':
			if gamedata['universe'] < gamedata['maxuniverse']:
				gamedata['floor'] -= 1
				gamedata['universe']+=1
				break
			else:
				gamedata['floor'] -= 1
				gamedata['universe']-=1
				break
		if gamedata['output'][gamedata['location'][0]][gamedata['location'][1]] == '@':
			if True:
				if gamedata['universe'] < gamedata['maxuniverse']:
					gamedata['floor'] -= 1
					gamedata['universe']+=1
					break
				else:
					gamedata['floor'] -= 1
					gamedata['universe']-=1
					break
				gamedata['rand'] = random.randint(1,5)
				if rand == 5:
					place_thing('X',random.randint(1,gamedata['floor']+10))
				if rand == 4:
					place_thing('H',random.randint(1,gamedata['floor']+10))
				if rand == 3:
					place_thing('F',random.randint(1,(100-gamedata['floor'])))
				if rand == 2:
					place_thing('*',random.randint(1,gamedata['floor']+10))
				if rand == 1:
					place_thing('%',gamedata['floor'] + 10)
		if gamedata['location'] == gamedata['stairs']:
			break
clear()
print("TEMPLE OF THE PYTHON: Endgame\nCredits:\n    Head Programmer: Martin L-P\n   Creator of Cipher: Patsy Ng\n")
