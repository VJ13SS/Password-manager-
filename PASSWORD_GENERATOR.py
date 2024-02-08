'''Welcome to random password generator...This will create passwords as your convinience...You can enter the respective number of letters,symbols and numbers for your password...and The interpreter will generate it....
Make your strong password'''
'''Last modified at 9/10/2023 4:38pm
 Author VJ 13 SS'''
import random
def password_generate():
	print('WELCOME TO PASSWORD GENERATOR')
	print('Enter your requirements in the password ')
	char=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
	sym=['@','#','/','&','_','+','?','*',':','!','%','€','¥','$']
	c=int(input('ENTER THE NUMBER OF LETTERS YOU WANT  IN YOUR PASSWORD: '))
	n=int(input('ENTER HOW MANY NUMBERS YOU WANT IN YOUR PASSWORD: '))
	s=int(input('ENTER THE NUMBER OF SYMBILS YOU WANT IN YOUR PASSWORD: '))
	password=[ ]
	for i in range(0,c):
		a=random.choice(char)
		password=password+[a]#To demonstrate list concatenation
	for j in range(0,n):
		b=random.randint(0,9)
		password=password+[b]
	for k in range (0,s):
		c=random.choice(sym)
		password=password+[c]
	result=" "
	random.shuffle(password)
	for i in password:
		result=result+str(i)
	return result
