from os import system 
from datetime import datetime
from json import load, dump
import time 

print("Welcome")
print("Please, input your account")
account = "project01@gmail.com"
password = "manueleblasius"
user_account = input("Enter Your Account : ")
while user_account != account:
	print("Wrong Account, Please Try Again")
	user_account = input("Enter Your Account : ")
	
user_password = input("Enter Your Password : ")
while user_password != password:
	print("Wrong Password, Please Try Again")
	user_password = input("Enter Your Password : ")
else:
	print("Welcome to Book Collection")
	time.sleep(1)

def menu():
	system("cls")
	menu = """
Book Collection
[1] - ADD NEW BOOK
[2] - SHOW ALL BOOK
[3] - SEARCH FOR BOOKS BY NAME
[4] - UPDATE BOOKS
[5] - DELETE BOOK
[6] - ABOUT APLICATION
[E] - EXIT
	"""
	print(menu)

def verify_ans(char):
	char = char.upper()
	if char == "Y":
		return True
	else:
		return False

def print_header(msg):
	system("cls")
	print(msg)

def create_book_id():
	today = datetime.now()
	year = today.year
	month = today.month
	hari = today.day
	counter = len(book_data)+1
	book_id = str("%4d%02d%02d-EZ%03d" % (year, month, hari, counter))
	return book_id

def print_book_data(book_id = None, all_field = False, volume = True):
	if book_id != None and all_field == False:
		print(f"""
		-DATA FOUND-
	ID \t: {book_id}
	Name \t: {book_data[book_id]["name"]}
	Writer \t: {book_data[book_id]["writer"]}
	Volume \t: {book_data[book_id]["volume"]}
			""")
	elif book_id != None and volume == False:
		print(f"""
		-DATA FOUND-
	ID \t: {book_id}
	Name \t: {book_data[book_id]["name"]}
	Writer \t: {book_data[book_id]["writer"]}
			""")
	elif all_field == True:
		for book_id in book_data:
			name = book_data[book_id]["name"]
			writer = book_data[book_id]["writer"]
			volume = book_data[book_id]["volume"]
			print(f"ID:{book_id}\tNAME:{name}\tWRITER:{writer}\tVOLUME:{volume}")

def add_book():
	print_header("-ENTER NEW BOOK DATA-")
	name = input("NAME\t: ").title()
	writer = input("WRITER\t: ").title()
	volume = imput("VOLUME\t: ")

	user_ans = input("Press Y to save(Y/N) : ").upper()

	if verify_ans(user_ans): 
		book_id = create_book_id()
		time.sleep(1)
		print("Saving Data.....")
		time.sleep(1)
		book_data[book_id] = {
			"name" : name,
			"writer" : writer,
			"volume" : volume
		}
		save_data_book()
		time.sleep(1)
		print("Data Saved")
	else:
		time.sleep(1)
		print("Data Not Saved")
	time.sleep(1)
	input("Press ENTER to return to MENU")

def print_book():
	print_header("-ALL BOOK")
	if len(book_data) == 0:
		print("<NOTHING IS SAVED YET>")
	else:
		print_book_data(all_field = True)
	time.sleep(1)
	imput("Press ENTER to return to MENU")

def searching_by_name(book):
	for book_id in book_data:
		if book_data[book_id]["name"] == book:
			print_book_data(book_id = book_id)
			return True
		else:
			print("DATA NOT FOUND")
			return False

def get_book_id_from_name(book):
	for book_id in book_data:
		if book_data[book_id]["name"] == book:
			return book_id

def seaching_by_id(book_id):
	for book_id in book_data:
		print_book_data(book_id = book_id)
		return True
	else:
		print("-DATA NOT FOUND-")
		return False

def find_book():
	print_header("-SEARCH BOOK-\n")
	name = input("The Name of Book You Are Looking For : ").title()
	result = searching_by_name(name)
	time.sleep(1)
	input("Press ENTER to return to MENU")

def delete_book():
	print_header("-DELETE BOOK-")
	name = input("Enter The Name Of Boom To Be Deleted : ").title()
	result = searching_by_name(name)
	if result:
		respon = input(f"Sure You Want To Deleted {name} ? (Y/N): ").upper()
		if verify_ans(respon):
			del book_data[name]
			save_data_apps()
			time.sleep(1)
			print("DATA has been deleted")
		else:
			time.sleep(1)
			print("DATA cancel to deleted")
		time.sleep(1)
		input("Press ENTER to retutn to MENU")

def update_name(book):
	print(f"Name Previously \t: {book}")
	new_name = input("New Name\t: ").title()
	respon = input("Are you sure want to change the data (Y/N) : ").upper()
	if verify_ans(respon):
		book_id = get_book_id_from_name(book)
		book_data[book_id]["name"] = new_name
		save_data_apps()
		time.sleep(1)
		print("Data has been update")
	else:
		time.sleep(1)
		print("Data cancel to update")

def update_book():
	print_header("-UPDATE BOOK DATA-\n")
	name = input("The name of book you want to update : ").title()
	result = searching_by_name(name)
	if result :
		respon = input("Press A to update data : ")
		if respon == "A":
			update_name(name)
		else:
			print("System Erorr! Please Try Again!")
	time.sleep(1)
	input("Press ENTER to return to MENU")

def about_book():
	print_header("-ABOUT BOOK-")
	Print("O===================================================================================================================O")
	print("Book Collection est un endroit pour stocker, créer, rechercher, mettre à jour et supprimer des données de livre")
	print("Ici, vous ne pouvez pas voir le contenu du livre, mais seulement les données.")
	print("Il existe de nombreux livres de données dans ce monde, vous pouvez entrer les données dans cette application.")
	print("J'ai créé cette application uniquement pour stocker les données du livre uniquement.")
	print("Merci!")
	print("O====================================================================================================================O")

def check_input(char):
	char = char.upper()
	if char == "E":
		return True
	elif char == "1":
		add_book()
	elif char == "2":
		print_book()
	elif char == "3":
		find_book()
	elif char == "4":
		update_book()
	elif char == "5":
		delete_book()
	elif char == "6":
		about_book()

def load_data_apps():
	with open(file_path, 'r') as document:
		book_data = load(document)
		return book_data

def save_data_apps():
	with open(file_path, 'w') as document:
		dump(book_data, document)

file_path = 'storage/book_table.json'
book_data = None
stop = False 

book_data = load_data_apps()

while not stop:
	menu()
	user_input = input("Enter Key : ").upper()
	stop = check_input(user_input)