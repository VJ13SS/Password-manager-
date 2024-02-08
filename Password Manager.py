import PASSWORD_GENERATOR as pg

def read():
	with open('passwords.txt','r') as fp:
		fp.seek(0)
		passwords=[line.strip().split() for line in fp.readlines()]#Reads each line as a list
		return passwords
def display():
		passwords=read()
		if not passwords:
			print('Empty...No Information Added')
		else:
			for i in passwords:
				print(i[0].ljust(10),' ',i[1])
				
def write():
	with open('passwords.txt','a') as fp:
		make=input('\nDo ypu wish to generate pawword(Type yes or no): ').lower()
		if(make=='yes'):
			password=pg.password_generate()
			print('\nYour Created password:\n ',password)
		else:
			password=input('\nEnter the password: ')
		type=input('\nEnter the password category: ')
		fp.write(f'{type} {password}\n')
	print('\nPassword Added Successfully')
	
def search():
	passwords=read()
	to_search=input('\nEnter the password or the category which you had given: ')
	for i in passwords:
		if to_search in i:
			print(i[0],' ',i[1])

def main():
	while True:
		print('\nWhat do you wish to do? ')
		print('1. Store Passwords')
		print('2. Display Passwords')
		print('3. Search Passwords ')
		print('4. Exit\n')
		try:
			choice=int(input('Enter your choice by selecting the number near to each option: '))
		except(ValueError):
			print('Invalid Input')
		else:
			if(choice==1):
				write()
			elif(choice==2):
				print('Your passwords: ')
				display()
			elif(choice==3):
				print('Your password: ')
				search()
			else:
				print('THANK YOU')
				break
			
main()		
