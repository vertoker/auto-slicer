import threading as th
import easygui as gui2
import pyperclip as clipboard
import PySimpleGUI as gui
import random as rnd

import staticdata
import render

data = [
	[rnd.randint(1000000000, 9999999999), (1920, 1080), 'G:\\Projects\\Python\\AutoSlicer\\result.mp4'],
	[],
	[]
]

updated = False
gui.theme('DarkAmber')
window = gui.Window('Auto Slicer', staticdata.layout)
event, values = window.read()

def logger(message):
	window['logger'].update(value = message)

def render():
	logger('Загрузка субтитров')
	#caption, name, language = sub.DownloadCaption(link)
	logger('Форматирование текста')
	#dataText = tf.TextFormater(caption, language)
	logger('Расстановка пунктуации нейросетью')
	#text = ai.PunctuationFormatter(dataText)
	#global data, updated
	#data = [text, name, caption]
	logger('Текст готов')
	updated = False

def selectPathSave():
	open(gui2.filesavebox(default = data[1] + '.txt'), 'w').write(data[0])
	logger('Текст сохранён')

def updateAll():
	languageUpdate()
	seedUpdate()
	resolutionUpdate()

def languageUpdate():
	global values
	index = staticdata.languages.index(values['language_select'])
	for key, value in staticdata.language_data.items():
		window[key].update(value[index])

def seedUpdate():
	global data
	window['seed_text'].update(data[0][0])

def resolutionUpdate():
	global data
	window['video_resolution_width'].update(data[0][1][0])
	window['video_resolution_heigth'].update(data[0][1][1])
	window['video_resolution_select'].update(str(data[0][1][0]) + 'x' + str(data[0][1][1]))

updateAll()


while True:
	event, values = window.read()
	print(event, values) #debug
	if not updated:
		if event in (None, 'Exit', 'Cancel'):
			break
		if event == 'render':
			updated = True
			updater = th.Thread(target = render)
			updater.start()
		# Основное
		if event == 'language_select':
			languageUpdate()
		if event == 'seed_refresh':
			data[0][0] = rnd.randint(1000000000, 9999999999)
			seedUpdate()
			logger('Text refreshed')
		if event == 'seed_copy':
			clipboard.copy(data[0][0])
			logger('Text copied')
		if event == 'video_resolution_width':
			data[0][1] = (values['video_resolution_width'], values['video_resolution_heigth'])
			resolutionUpdate()
		if event == 'video_resolution_heigth':
			data[0][1] = (values['video_resolution_width'], values['video_resolution_heigth'])
			resolutionUpdate()
		if event == 'video_resolution_select':
			data[0][1] = values['video_resolution_select'].split('x')
			resolutionUpdate()
		# Видео
		if event == '':
			pass
		if event == '':
			pass
		if event == '':
			pass
		if event == '':
			pass
		if event == '':
			pass
		if event == '':
			pass
		if event == '':
			pass
		if event == '':
			pass
