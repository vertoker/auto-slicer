languages = [
    'English', 'Русский'
]

resolution_templates = [
    '1920x1080', '1080x1920',
    '1600x900', '900x1600',
    '1280x720', '720x1280',
    '1080x1080', '1920x1920'
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