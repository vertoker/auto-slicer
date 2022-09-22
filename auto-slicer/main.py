import PySimpleGUI as gui
import pyperclip as clipboard
import easygui as gui2
import threading as th

import staticdata

layout = [
	[gui.Text(key='seed_text'), gui.Button('', key='seed_replace'), gui.Button('', key='seed_delete'),
    gui.Text('Language', key='language_text'), 
    gui.Combo(staticdata.languages, default_value=staticdata.languages[0], key='language_select')],

	#[gui.Text('Length of result video', key='video_result_length_text'), 
    #gui.InputText('', key='video_result_length', enable_events=True),],

	[gui.Text('Resolution', key='video_resolution_text'), 
    gui.InputText('', size = (5, 1), key='video_resolution_width', enable_events=True),
    gui.InputText('', size = (5, 1), key='video_resolution_heigth', enable_events=True),
    gui.Combo(staticdata.resolution_templates, default_value=staticdata.resolution_templates[0], key='language_select')],

    [],
]

data = []

updated = False

gui.theme('DarkAmber')
window = gui.Window('Конвертация видео в статью', layout)

def logger(message):
	window['logger'].update(value = message)

def update(link):
	logger('Загрузка субтитров')
	caption, name, language = sub.DownloadCaption(link)
	logger('Форматирование текста')
	dataText = tf.TextFormater(caption, language)
	logger('Расстановка пунктуации нейросетью')
	text = ai.PunctuationFormatter(dataText)
	global data, updated
	data = [text, name, caption]
	logger('Текст готов')
	updated = False

def copy():
	global data, updated
	clipboard.copy(data[1] + '\n' + data[0])
	logger('Текст скопирован')
	updated = False

def paste():
	return clipboard.paste()

def save():
	global updated
	if (data[1] != ''):
		open(gui2.filesavebox(default = data[1] + '.txt'), 'w').write(data[0])
	logger('Текст сохранён')
	updated = False

def save_subtitle():
	global updated
	if (data[1] != ''):
		open(gui2.filesavebox(default = data[1] + ' sub.srt'), 'w').write(data[2])
	logger('Файл субтитров сохранён')
	updated = False

def save_youtube_subtitle():
	global updated
	if (data[1] != ''):
		open(gui2.filesavebox(default = data[1] + ' sbv.sbv'), 'w').write(sub.Caption2sbv(data[2]))
	logger('Файл субтитров сохранён')
	updated = False

while True:
	event, values = window.read()
	#print(event, values) #debug
	if not updated:
		if event in (None, 'Exit', 'Cancel'):
			break
		if event == 'submit':
			updated = True
			updater = th.Thread(target = update, args = [values['link']])
			updater.start()
		if event == 'copy':
			updated = True
			copy()
		if event == 'paste':
			window['link'].update(paste())
		if event == 'save':
			save()
		if event == 'save-subtitle':
			updated = True
			save_subtitle()
		if event == 'save-youtube-subtitle':
			updated = True
			save_youtube_subtitle()
