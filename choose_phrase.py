import pandas as pd
import numpy as np

def get_random_phrase(df):
	choose_row = np.random.randint(df.index.start, df.index.stop)
	choose_hero = df.loc[choose_row]["heroes"].split()
	choose_quote = df.loc[choose_row]["quote"]
	choose_image_index = np.random.randint(1, 4)
	choose_image = []
	heroes=""
	for hero in choose_hero:
		heroes += hero
	choose_image.append('./static/assets/images/' + heroes + str(choose_image_index) + '.png')
	# print(choose_hero, choose_quote, choose_image)
	return choose_hero, choose_quote, choose_image

def get_phrase_from_hero(pick_hero, df):
	quotes = []
	for i in range(len(df)):
		if df.loc[i, "heroes"] == pick_hero:
			quotes.append(df.loc[i, "quote"])
        
	choose_index = np.random.randint(0, len(quotes))
	choose_image_index = np.random.randint(1, 4)
	choose_image = './static/assets/images/' + pick_hero[1:] + str(choose_image_index) + '.png'
	return quotes[choose_index], choose_image

def result():
	df = pd.read_csv(open('result.csv', 'r', encoding='utf-8'))
	return get_random_phrase(df)

def result_for_pick_hero(pick_hero):
	df = pd.read_csv(open('result.csv', 'r', encoding='utf-8'))
	return get_phrase_from_hero(pick_hero, df)

if __name__ == '__main__':
	result()
	pick_hero = ' Симба'
	print(result_for_pick_hero(pick_hero))
