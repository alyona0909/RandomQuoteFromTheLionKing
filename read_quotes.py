import requests
from bs4 import BeautifulSoup
import csv

pages = list(range(2, 5))

# function to form https request and get links and subs for a page
def get_links_and_subs_for_page(page_number):
	https = 'http://itmydream.com/citati/mult/korol-lev-the-lion-king/'
	https +='?page=' + str(page_number)
	res = requests.get(https)
	if not res.status_code == 200:
		raise Exception(f"Error with opening page {page_number}")
	bs = BeautifulSoup(res.text, 'html.parser')
	# in select : argument '.smth' means class, '#smth' means id
	all_page_text =  bs.select('.col-sm-8')
	all_stuff = all_page_text[0].select('.quote ')
	return all_stuff

# function to select quotes and heros
def create_custom(all_stuff):
	lst=[]
	for index, item in enumerate(all_stuff):
		is_hero = all_stuff[index].select('.quote__characters-list')
		# not all quotes have heroes
		if len(is_hero):
			hero = is_hero[0].getText().split('\n')
			heroes = hero[1:len(hero) - 1]
			if ' и ' in heroes[0]:
				heroes = heroes[0].split(' и')
			quote = all_stuff[index].select('.quote__content')[0].getText()
			quote = quote.replace(' — ', '\n — ')
			lst.append({'heroes' : heroes, 'quote' : quote})
	return (lst)

# function to write data to csv file
def write_to_file_csv(data):
	with open('result.csv', 'w', newline='', encoding='utf-8') as file:
		csv_writer  = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
		csv_writer.writerow(['heroes', 'quote'])
		for record in data:
			hero = ""
			for tmp in record["heroes"]:
				hero += tmp
			hero.replace(' и ', '')
			csv_writer.writerow([hero, record["quote"]])

# function to write data to csv file
def write_to_file_txt(data):
	with open('result.txt', 'w', encoding='utf-8') as file:
			for dict_record in data:
				for key, value in dict_record.items():
					file.write(f"{key} : {value} \n")
				file.write(f"\n")

def main():
	try:
		all_stuff = get_links_and_subs_for_page(1)
		for num_page in pages:
			all_stuff += get_links_and_subs_for_page(num_page)			
	except Exception as err:
		print(err)
	finally:
		my_list = create_custom(all_stuff)
		write_to_file_csv(my_list)
		write_to_file_txt(my_list)
		

if __name__ == '__main__':
	main()