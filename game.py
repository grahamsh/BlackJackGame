import random
import time
import pygame
import sys

turn = 0
dstay = False
pstay = False
pcard1 = 0
pcard2 = 0
pcard3 = 0
pcolor1 = 0
pcolor2 = 0
pcolor3 = 0
plose = False
pwin = False
pjack = False
pqueen = False
pking = False
pace = False
correct = False
ptotal = 0
dcard1 = 0
dcard2 = 0
dcard3 =0 
dtotal = 0
diamond = False
club = False
spade = False
heart = False
suit1 = ""
suit2 = ""
number = ""
number2 = ""
p_card1 = ""
cont = True
Cash = 1000
bet = 0
existing = True
user = ""


def save_file():

	global existing
	global Cash
	global user
	existing2 = False
	valid = 1

	print("---------------------------------------------------\n")
	time.sleep(0.5)
	print("-                                                 -\n")
	time.sleep(0.5)
	print("-                  WELCOME TO                     -\n")
	time.sleep(0.5)
	print("-                                                 -\n")
	time.sleep(0.5)
	print("-           GRAHAM'S BLACKJACK GAME               -\n")
	time.sleep(0.5)
	print("-                                                 -\n")
	time.sleep(0.5)
	print("-                                                 -\n")
#	time.sleep(0.5)
#	print("-                                                 -\n")
#	time.sleep(0.5)
#	print("-                                                 -\n")
	time.sleep(0.5)
	print("---------------------------------------------------\n")
	#print("turn:",turn)
	time.sleep(0.5)
	print("\n")
	
	i = 0
	save_info = open("blackjack.txt", "r+")
	array = []
	#newline = ""
	#array.append("hello")
	#print i
	for line in save_info:
		#print line
		array.append(line)
		#print array[i]
		i += 1
	while valid == 1:
		usr = raw_input("Do you have a username Yes or No: ")
		#print i
		if usr == "Yes" or usr == "yes":
			inp = raw_input("Please enter your username \n")
			x = len(inp)
			user = inp
			#print x
			y = 0
			while y < i:
				#print("here")
				#print array[y][0:x]
				#print i
				#print y
				if array[y][0:x] == inp:
					z = len(array[y])
					#print z
					w = z-x
				#	print w
					money = array[y][w+1:z]
					Cash = int(money)
					#print money
					#print array[y]
					break
				y+=1
			if y == i:
				print("Name not found in file")
				valid = 1
			else:
				valid = 2
		elif usr == "No" or usr == "no":
			while existing == True:
				existing2 = False
				var1 = 0
				new_usr = raw_input("Please enter a new username: \n")
				#import pdb; pdb.set_trace()
				print new_usr
				a = len(new_usr)
				
				#b+=1
				while var1 < i:
					#print("here")
					#print array[y][0:x]
					if array[var1][0:a] == new_usr:
						print("You typed an existing username")
						existing2 = True
					var1+=1
					#print var1
					#print i
				if existing2 == False:
					existing = False				
			if existing2 == False:
				array.append(new_usr + " " + ":" + " " + "1000 \n")
				user = new_usr
				q = i
				newline = array[q]
				valid = 2
				#print newline
				save_info.write(newline)
				save_info.close()
		else:
			print("You entered an inccoret value, please try again")

def player():
	global turn
	global pstay
	global pcard1
	global pcard2
	global pcard3
	global pcolor1
	global pcolor2
	global pcolor3
	global plose
	global pwin
	global pjack
	global pqueen
	global pking
	global pace
	global correct
	global ptotal
	global diamond
	global spade
	global heart
	global club
	global suit
	global number
	global number2
	global p_card1
	global suit2
	global Cash
	global bet
	#print(turn)
	correct = False
	same = False
	number = "none"
	number2 = "none"
	pcard_dig = False
	card2_dig = False
	card1face = ""
	card2face = ""
	print("\n")
	for g in range(10):
			sys.stdout.write("\r{0}>".format("="*g))
			sys.stdout.flush()
			time.sleep(0.2)
	print("Your turn")
	
	if turn == 0:
		for g in range(10):
			sys.stdout.write("\r{0}>".format("="*g))
			sys.stdout.flush()
			time.sleep(0.2)
		print("You have $" + str(Cash))
		for g in range(10):
			sys.stdout.write("\r{0}>".format("="*g))
			sys.stdout.flush()
			time.sleep(0.2)
		inp = raw_input("How much would you like to bet? \n")
		while Cash - int(inp) < 0:
			inp = raw_input("Invalid bet, enter a new amount \n")
		bet = int(inp)
		print("\n")
		print("You Draw")
		for x in range(1):
			pcard1 = random.randint(2,14)
			pcolor1 = random.randint (1,4)
			if pcolor1 == 1:
				diamond = True
				suit1 = "Diamonds"
			if pcolor1 == 2:
				heart = True
				suit1 = "Hearts"
			if pcolor1 == 3:
				spade = True
				suit1 = "Spades"
			if pcolor1 == 4:
				club = True
				suit1 = "Clubs"
			if pcard1 == 11:
				pjack = True
				number = "Jack"
				pcard1 = 10
			if pcard1 == 12:
				pqueen = True
				number = "Queen"
				pcard1 = 10
			if pcard1 == 13:
				pking = True
				number = "King"
				pcard1 = 10
			if pcard1 == 14:
				pace = True
				number = "Ace"
				pcard1 = 11
			#p_card1 = number + " " + "of" + " " + suit
			if number != "none":
				print("Card 1 is: ",number + " " + "of" + " " + suit1)
			else: 
				print("Card 1 is: ",str(pcard1) + " " + "of" + " " + suit1)
			#print pcard1
		for y in range(1):
			pcard2 = random.randint(2,14)
			pcolor2 = random.randint (1,4)
			#import pdb; pdb.set_trace()
			#print pcard2
			if pcolor2 == 1:
				diamond = True
				suit2 = "Diamonds"
			if pcolor2 == 2:
				heart = True
				suit2 = "Hearts"
			if pcolor2 == 3:
				spade = True
				suit2 = "Spades"
			if pcolor2 == 4:
				club = True
				suit2 = "Clubs"
			if pcard2 == 11:
				pjack = True
				number2 = "Jack"
				pcard2 = 10
			if pcard2 == 12:
				pqueen = True
				number2 = "Queen"
				pcard2 = 10
			if pcard2 == 13:
				pking = True
				number2 = "King"
				pcard2 = 10
			if pcard2 == 14:
				pace = True
				number2 = "Ace"
				pcard2 = 11
			#p_card1 = number + " " + "of" + " " + suit	
			
			#print pcard2
			if pcard2 == pcard1 and suit2 == suit1:  
				if pcard1 == 10 and number == "none":
					pcard_dig = True
				if pcard2 == 10 and number2 == "none":
					card2_dig = True
				if number != "none":
					card1face = number
				if number2 != "none":
					card2face = number2
				if pcard_dig == card2_dig or card1face == card2face:
					print("Same card")
					same = True
				else:
					same = False
			while same == True:	
				pcard2 = random.randint(2,14)
				pcolor2 = random.randint (1,4)
				if pcard2 != pcard1 or suit2 != suit1:  
					#print("Same card")
					if pcolor2 == 1:
						diamond = True
						suit2 = "Diamonds"
					if pcolor2 == 2:
						heart = True
						suit2 = "Hearts"
					if pcolor2 == 3:
						spade = True
						suit2 = "Spades"
					if pcolor2 == 4:
						club = True
						suit2 = "Clubs"
					if pcard2 == 11:
						pjack = True
						number2 = "Jack"
						pcard2 = 10
					if pcard2 == 12:
						pqueen = True
						number2 = "Queen"
						pcard2 = 10
					if pcard2 == 13:
						pking = True
						number2 = "King"
						pcard2 = 10
					if pcard2 == 14:
						pace = True
						number2 = "Ace"
						pcard2 = 11
						
					same = False
				#if number2 != "none":
				#	print("Card 2 is: ",number2 + " " + "of" + " " + suit2)
				#else: 
				#	print("Card 2 is: ",str(pcard2) + " " + "of" + " " + suit2)
			if number2 != "none":
				print("Card 2 is: ",number2 + " " + "of" + " " + suit2)
			else: 
				print("Card 2 is: ",str(pcard2) + " " + "of" + " " + suit2)
		ptotal = pcard1+pcard2
	#print(pcard1,pcard2)
	turn += 1
	print("\n")
	#print(turn)
	#print(total)


	if turn > 1 and pstay == False and plose == False and pwin == False:
		print('You have:', ptotal)
		if ptotal > 21:
			print("You busted")
			plose = True
		elif ptotal == 21:
			print("21! you win")
			pwin = True
		else:
			#print correct
			while correct == False:
				#print("here")
				inp = raw_input("stay or draw again, type stay to stay or draw to draw again \n")
				if inp != 'stay' and inp != 'draw':
					print("you entered an incorrect command")
				elif inp == 'stay':
					#print("stay")
					pstay = True
					correct = True
				else:
					#print("draw")
					for x in range(1):
						pcard3 = random.randint(1,14)
						pcolor3 = random.randint (1,4)
						if pcolor3 == 1:
							diamond = True
							suit = "Diamonds"
						if pcolor3 == 2:
							heart = True
							suit = "Hearts"
						if pcolor3 == 3:
							spade = True
							suit = "Spades"
						if pcolor3 == 4:
							club = True
							suit = "Clubs"
						if pcard3 == 11:
							pjack = True
							number = "Jack"
							pcard3 = 10
						if pcard3 == 12:
							pqueen = True
							number = "Queen"
							pcard3 = 10
						if pcard3 == 13:
							pking = True
							number = "King"
							pcard3 = 10
						if pcard3 == 14 or pcard3 == 1:
							pace = True
							number = "Ace"
							pcard3 = 11
						#p_card1 = number + " " + "of" + " " + suit
						if number:
							print("Card 3 is: ",number + " " + "of" + " " + suit)
						else: 
							print("Card 3 is: ",str(pcard3) + " " + "of" + " " + suit)
						print pcard3
						ptotal = ptotal + pcard3
						print('You have:', ptotal)
						if ptotal > 21:
							print("You busted")
							plose = True
						correct = True
						break
		#pass
		print("\n")
		return turn


def dealer():
	global turn
	global dstay
	global dcard1 
	global dcard2
	global dcard3
	global dtotal
	global plose
	global pwin

	for g in range(10):
			sys.stdout.write("\r{0}>".format("="*g))
			sys.stdout.flush()
			time.sleep(0.1)
	print("Dealers turn")


	if turn == 1:
		for x in range(1):
			dcard1 = random.randint(1,10)
		for y in range(1):
			dcard2 = random.randint(1,10)
		dtotal = dcard1 + dcard2
	#print(dcard1, dcard2)
	#print("dealer total:",dtotal)
	turn += 1

	if turn > 2 and plose == False and pwin == False:
		if dtotal == 21:
			for g in range(10):
				sys.stdout.write("\r{0}>".format("="*g))
				sys.stdout.flush()
				time.sleep(0.1)
			print("Dealer has 21!")
			plose = True
			dstay = True 
		elif dtotal > 21:
			for g in range(10):
				sys.stdout.write("\r{0}>".format("="*g))
				sys.stdout.flush()
				time.sleep(0.1)
			print("Dealer busted!")
			pwin = True
		elif dtotal > 16:
			for g in range(10):
				sys.stdout.write("\r{0}>".format("="*g))
				sys.stdout.flush()
				time.sleep(0.1)
			print("Dealer stays")
			dstay = True
			#pass
		else:
			for g in range(10):
				sys.stdout.write("\r{0}>".format("="*g))
				sys.stdout.flush()
				time.sleep(0.1)
			print("dealer draws")
			for x in range(1):
				dcard3 = random.randint(1,14)
				#print dcard3
				dtotal = dtotal + dcard3
				if dtotal > 21:
					for g in range(10):
						sys.stdout.write("\r{0}>".format("="*g))
						sys.stdout.flush()
						time.sleep(0.1)
					print("Dealer busted, you win")
					pwin = True
				#print('Dealer has:', dtotal)	
	
		
	#print(turn)
		print("\n")
		return turn

def reset():
	global turn
	global dstay
	global pstay
	global pcard1
	global pcard2
	global pcard3
	global pcolor1
	global pcolor2
	global pcolor3
	global plose
	global pwin
	global pjack
	global pqueen
	global pking
	global pace
	global correct
	global ptotal
	global dcard1
	global dcard2
	global dcard3
	global dtotal
	global diamond
	global club
	global spade
	global heart
	global suit 
	global number 
	global p_card1 
	global cont


	turn = 0
	dstay = False
	pstay = False
	pcard1 = 0
	pcard2 = 0
	pcard3 = 0
	pcolor1 = 0
	pcolor2 = 0
	pcolor3 = 0
	plose = False
	pwin = False
	pjack = False
	pqueen = False
	pking = False
	pace = False
	correct = False
	ptotal = 0
	dcard1 = 0
	dcard2 = 0
	dcard3 =0 
	dtotal = 0
	diamond = False
	club = False
	spade = False
	heart = False
	suit = ""
	number = ""
	p_card1 = ""
	cont = True

def game():
	global cont
	global turn
	global pwin
	global plose
	global dstay
	global pstay
	global dtotal
	global ptotal
	global Cash
	global bet
	global user


	while pwin == False and plose == False:
		while pstay == False:
			#print("here")
			player()
			time.sleep(2)
			break
		if plose == False and pwin == False:
			while dstay == False:
				dealer()
				time.sleep(1)
				break
		if dstay and pstay:
			print("you have:", ptotal)
			print("dealer has:", dtotal)
			if ptotal > dtotal:
				print("you win")
				pwin = True
			else:
				print("dealer wins")
				plose = True
		
	if pwin:
		Cash = Cash + bet
		print("You now have $" + str(Cash))
	if plose:
		Cash = Cash - bet
		print("You now have $" + str(Cash))
	if pwin or plose:
		if Cash > 0:
			inp2 = raw_input("Would you like to play again Yes or No: ")
			if inp2 == "No":
				print("you selected no, saving your info")
				i = 0
				save_info = open("blackjack.txt", "r+")
				array = []
				#newline = ""
				#array.append("hello")
				#print i
				for line in save_info:
				#print line
					array.append(line)
					i += 1
				save_info.close()
				x = len(user)
					#print x
				y = 0
				while y <= i:
					if array[y][0:x] == user:
						z = len(array[y])
							#print z
						w = z-x
			#			print w
						#print array[y][w+1:z]
						#print Cash
						#array.append(new_usr + " " + ":" + " " + "1000")
						array[y] = user + " " + ":" + " " + str(Cash) + "\n"
						break
					else:	
						y+=1
				q = 0
				file = open("blackjack.txt", "w")
				while q < i:
					#print q
					newline = array[q]
					#print newline
					q+=1
					file.write(newline)
					file.truncate()
				file.close()	
					
				cont = False
			else:
				reset()
		elif Cash <= 0:
			print("You have no money")
			cont = False

if __name__ == '__main__':
	#print(pstay)
	#print(dstay)
	save_file()
	while cont:
		game()
	#save_info.close()