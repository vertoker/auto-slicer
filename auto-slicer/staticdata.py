from tkinter import DISABLED
import PySimpleGUI as gui

languages = [
    'English', 'Русский'
]

resolution_templates = [
    '1920x1080', '1080x1920',
    '1600x900', '900x1600',
    '1280x720', '720x1280',
    '1080x1080', '1920x1920'
]

language_data = {
    'language_text': ('Language', 'Язык'),
    'seed_refresh': ('Refresh', 'Обновить'),
    'seed_copy': ('Copy', 'Скопировать'),
    'video_resolution_text': ('Resolution', 'Разрешение'),
    'video_path_text': ('Video path', 'Путь к видео'),
    'video_path_button': ('Search', 'Найти'),
    'video_slice_input': ('Slice video?', 'Нарезать видео?'),
    'audio_mute_input': ('Audio mute?', 'Без звука?'),
    'min_slice_length_checkbox': ('Min slice length', 'Минимальная длина фрагмента нарезки'),
    'max_slice_length_checkbox': ('Max slice length', 'Максимальная длина фрагмента нарезки'),
    'start_video_text': ('Start video', 'Начало видео'),
    'end_video_text': ('End video', 'Конец видео'),
    'audio_path_text': ('Audio path', 'Путь к аудио'),
    'audio_path_button': ('Search', 'Найти'),
    'start_audio_text': ('Start audio', 'Начало аудио'),
    'end_audio_text': ('End audio', 'Конец аудио'),
    'audio_fade_in_checkbox': ('Fade in', 'Появление'),
    'audio_fade_out_checkbox': ('Fade out', 'Затухание'),
    'result_video_path_text': ('Result video path', 'Путь к экспорту готового видео'),
    'result_video_path_button': ('Search', 'Найти'),
    'render': ('Render', 'Рендер')
}

language_data_logger = {
    '': ('', ''),
    '': ('', ''),
    '': ('', ''),
    '': ('', ''),
    '': ('', ''),
    '': ('', ''),
    '': ('', ''),
}

layout = [
	# Основные параметры
    [gui.Text('Language', key='language_text'), 
    gui.Combo(languages, default_value=languages[0], key='language_select', enable_events=True)],
	[gui.Text('1234567890', size = (10, 1), key='seed_text'), 
    gui.Button('Refresh', key='seed_refresh'), 
    gui.Button('Copy', key='seed_copy')],

	#[gui.Text('Length of result video', key='video_result_length_text'), 
    #gui.InputText('', key='video_result_length', enable_events=True),],

	[gui.Text('Resolution', key='video_resolution_text'), 
    gui.InputText('', size = (5, 1), key='video_resolution_width', enable_events=True),
    gui.InputText('', size = (5, 1), key='video_resolution_heigth', enable_events=True),
    gui.Combo(resolution_templates, default_value=resolution_templates[0], key='video_resolution_select', enable_events=True)],

	# Видео параметры
    [gui.Text('Video path', key='video_path_text', enable_events=True), 
    gui.Input('', key='video_path_input', enable_events=True),
    gui.Button('Search', key='video_path_button', enable_events=True)],
    [gui.Checkbox('Slice video?', key='video_slice_input', enable_events=True),
    gui.Checkbox('Audio mute?', key='audio_mute_input', enable_events=True)],

    [gui.Checkbox('Min slice length', key='min_slice_length_checkbox', enable_events=True), 
    gui.InputText('3', size = (5, 1), key='min_slice_length_input', enable_events=True)],
    [gui.Checkbox('Max slice length', key='max_slice_length_checkbox', enable_events=True), 
    gui.InputText('20', size = (5, 1), key='max_slice_length_input', enable_events=True)],

    [gui.Text('Start video', key='start_video_text'), 
    gui.InputText('', size = (5, 1), key='start_video_input', enable_events=True),
    gui.Text('End video', key='end_video_text'), 
    gui.InputText('', size = (5, 1), key='end_video_input', enable_events=True)],

	# Аудио параметры
    [gui.Text('Audio path', key='audio_path_text', enable_events=True), 
    gui.Input('', key='audio_path_input', enable_events=True),
    gui.Button('Search', key='audio_path_button', enable_events=True)],
    [gui.Text('Start audio', key='start_audio_text'), 
    gui.InputText('', size = (5, 1), key='start_audio_input', enable_events=True),
    gui.Text('End audio', key='end_audio_text'), 
    gui.InputText('', size = (5, 1), key='end_audio_input', enable_events=True)],

    [gui.Checkbox('Fade in', key='audio_fade_in_checkbox', enable_events=True), 
    gui.InputText('0', size = (5, 1), key='audio_fade_in_input', enable_events=True),
    gui.Checkbox('Fade out', key='audio_fade_out_checkbox', enable_events=True), 
    gui.InputText('0', size = (5, 1), key='audio_fade_out_input', enable_events=True)],

    [gui.Text('Result video path', key='result_video_path_text', enable_events=True), 
    gui.Input('', key='result_video_path_input', enable_events=True),
    gui.Button('Search', key='result_video_path_button', enable_events=True)],

    [gui.Text('', size = (30, 1), key='logger', enable_events=True),
    gui.Button('Render', key='render')]
]

# 0 - Основные данные для видео
#   0 - сид (для реализации предсказуемого рандома)
#   1 - разрешение итогового видео
#   2 - путь, куда сохранить видео
# 1 - Данные о видео материале для нарезки (двойной список)
#   0 - путь к видео
#   1 - нарезать видео? (True/False)
#   2 - перемешать (True/False)
#     Закидывает его в список и все видео, которые в него вошли 
#     перемешивает. Если видео нарезано, то значит нарезанные 
#     куски заносяться как отдельные видео
#   3 - убрать звук (True/False)
#   4 - минимальная длина slice
#   5 - максимальная длина slice
#     Если числа совпадают, то нарезка будет происходить равными
#     кусками. Минимум не может быть больше максимума и оба
#     должны быть не меньше 0.5 секунды и не больше длины видео.
#     Дефолтные значения - 3 секунды и 20 секунд соответственно
#   6 - начало видео
#   7 - конец видео
#     Расстояние между числами должно быть не меньше 1 секунды и
#     начало не может быть больше конца. Автоматически стоят на
#     0 секунде и длине видео соответственно
#   8 - вставить/заполнить/растянуть видео (3 варианта)
# 2 - Данные об аудио
#   0 - путь, где храниться аудиофайл
#   1 - начало аудио
#   2 - конец аудио
#     Длина аудио и видео существуют отдельно, поэтому
#     необходимо указывать пользователю на то, что они не
#     совпадают. Желательно, чтобы аудио было длиннее видео.
#     Если всё наоборот, то нужно предупредить об этом 
#     пользователя.
#   3 - длина плавного входа
#   4 - длина плавного выхода
#     Это эффект звукового нарастания и затухания
#     Сумма их длин не может быть больше длины аудио файла
#     Если значения равны 0, то они не работают
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 