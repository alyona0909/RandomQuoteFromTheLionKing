from flask import Flask
from flask import render_template  # to open html files
import os
from flask import url_for, send_from_directory # to open any files like pictures
from flask import request # to send data to server from web page
from flask import redirect # to open page by clicking 
from choose_phrase import result, result_for_pick_hero
from requests import post
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/<string:page_name>')
def launch_html_page(page_name = None):
	return render_template(page_name)

@app.route('/generate.html')
def generate():
	choose_hero, choose_quote, choose_image = result()
	heroes = ""
	for index, hero in enumerate(choose_hero):
		if index != len(choose_hero) - 1:
			heroes += hero + ' и '
		else:
			heroes += hero
	image = choose_image[0]
	return render_template('generate.html', hero=heroes, quote=choose_quote, image=image)

@app.route('/zazu.html')
def generate_zazu():
	choose_quote, choose_image = result_for_pick_hero(' Зазу')
	return render_template('zazu.html', quote=choose_quote, image=choose_image)

@app.route('/rafiki.html')
def generate_rafiki():
	choose_quote, choose_image = result_for_pick_hero(' Рафики')
	return render_template('rafiki.html', quote=choose_quote, image=choose_image)

@app.route('/mufasa.html')
def generate_mufasa():
	choose_quote, choose_image = result_for_pick_hero(' Муфаса')
	return render_template('mufasa.html', quote=choose_quote, image=choose_image)

@app.route('/nala.html')
def generate_nala():
	choose_quote, choose_image = result_for_pick_hero(' Нала')
	return render_template('nala.html', quote=choose_quote, image=choose_image)

@app.route('/simba.html')
def generate_simba():
	choose_quote, choose_image = result_for_pick_hero(' Симба')
	return render_template('simba.html', quote=choose_quote, image=choose_image)

@app.route('/timon.html')
def generate_timon():
	choose_quote, choose_image = result_for_pick_hero(' Тимон')
	return render_template('timon.html', quote=choose_quote, image=choose_image)

@app.route('/pumbaa.html')
def generate_pumbaa():
	choose_quote, choose_image = result_for_pick_hero(' Пумба')
	return render_template('pumbaa.html', quote=choose_quote, image=choose_image)

@app.route('/scar.html')
def generate_scar():
	choose_quote, choose_image = result_for_pick_hero(' Шрам')
	return render_template('scar.html', quote=choose_quote, image=choose_image)