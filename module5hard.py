
from time import sleep

"""
Класс User: содержит пользователей с атрибутами:
nickname(имя пользователя, строка), password(в хэшированном виде, число), age(возраст, число)
"""
class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age
        self.nick_pass_hash = hash(nickname + password)


"""
Класс Video: содержит видео с атрибутами:
title(заголовок, строка), duration(продолжительность, секунды), time_now(секунда остановки (изначально 0)),
adult_mode(ограничение по возрасту, bool (False по умолчанию))
"""
class Video:
    def __init__(self, title, duration, time_now=0, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode


"""
Класс UrTube: содержит зарегистрированного пользователя в системе в данный момент:
users(список объектов User), videos(список объектов Video), current_user(текущий пользователь, User)
"""
class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = []

    """
    Метод log_out для сброса текущего пользователя.
    """
    def log_out(self):
        self.current_user = []


    """
    Метод log_in, который принимает на вход аргументы: nickname, password и пытается найти пользователя в users с такими
    же логином и паролем. Если такой пользователь существует, то current_user меняется на найденного. Помните, что
    password передаётся в виде строки, а сравнивается по хэшу.
    """
    def log_in(self, nickname, password):
        self.current_user = []
        for user in self.users:
            if user.nick_pass_hash == hash(nickname + password) and user.password == hash(password):
                self.current_user = [user.nickname,user.age]                    #для упрощения проверки возраста передаю его в Current_user.
                return
        print('Пользователь не найден')
       

    """
    Метод register, который принимает три аргумента: nickname, password, age, и добавляет пользователя в список, если
    пользователя не существует (с таким же nickname). Если существует, выводит на экран: "Пользователь {nickname} уже
    существует". После регистрации, вход выполняется автоматически.
    """
    def register(self, nickname, password, age):
        UrTube.log_out(self)
        for user in self.users:
            if user.nickname == nickname:
                print(f'Пользователь {nickname} уже существует')
                return
        self.users.append(User(nickname, password, age))
        print(f'Пользователь {nickname} успешно зарегистрирован')
        UrTube.log_in(self, nickname, password)
    """
    Метод add, который принимает неограниченное кол-во объектов класса Video и все добавляет в videos, если с таким же
    названием видео ещё не существует. В противном случае ничего не происходит.
    """
    def add(self, *videos):
        for video in videos:
            if video.title not in [video.title for video in self.videos]:
                self.videos.append(video)

    """
    Метод get_videos, который принимает поисковое слово и возвращает список названий всех видео, содержащих поисковое
    слово. Следует учесть, что слово 'UrbaN' присутствует в строке 'Urban the best' (не учитывать регистр).
    """
    def get_videos(self, search_word):
        return [video.title for video in self.videos if search_word.lower() in video.title.lower()]

    """
    Метод watch_video, который принимает название видео и пытается найти его в videos. Если видео найдено, то выводится
    на экран: "Вы смотрите видео {title}". Если видео не найдено, то выводится на экран: "Видео не найдено".
    Метод watch_video, который принимает название фильма, если не находит точного совпадения(вплоть до пробела), то
    ничего не воспроизводится, если же находит - ведётся отчёт в консоль на какой секунде ведётся просмотр. После текущее
    время просмотра данного видео сбрасывается.
    Для метода watch_video так же учитывайте следующие особенности:
    Для паузы между выводами секунд воспроизведения можно использовать функцию sleep из модуля time.
    Воспроизводить видео можно только тогда, когда пользователь вошёл в UrTube. В противном случае выводить в консоль
    надпись: "Войдите в аккаунт, чтобы смотреть видео"
    Если видео найдено, следует учесть, что пользователю может быть отказано в просмотре, т.к. есть ограничения 18+.
    Должно выводиться сообщение: "Вам нет 18 лет, пожалуйста покиньте страницу"
    После воспроизведения нужно выводить: "Конец видео"
    """
    def watch_video(self, title):
        if self.current_user == []:
                print('Войдите в аккаунт, чтобы смотреть видео')
                return
        for video in self.videos:
            if video.title == title:
                if video.adult_mode and self.current_user[1] < 18:
                    print('Вам нет 18 лет, пожалуйста покиньте страницу')
                    return
                if video.title == title:
                    print(f'Вы смотрите видео {video.title}')
                    for i in range(video.duration):
                        sleep(1)                                                # лучше закоментировать перед тестом
                        print(i)
                    print('Конец видео')
                    return
        print('Видео не найдено')

    """
    Метод delete, который принимает название видео и пытается найти его в videos. Если видео найдено, то выводится на
    print('Видео не найдено')
    """
    def delete(self, title):
        for video in self.videos:
            if video.title == title:
                print(f'Видео {video.title} удалено')
                return
        print('Видео не найдено')

         
    




ur = UrTube()                                                               # Загружаем оболочку видеохостинга
v1 = Video('Лучший язык программирования 2024 года', 200)                   # передаем список видео
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(f"Текущий пользователь: {ur.current_user}")

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')
print(f"Текущий пользователь: {ur.current_user}")
ur.log_in('vasya_pupkin', 'lolkekcheburek')
ur.watch_video('Лучший язык программирования 2024 года!')
print(f"Текущий пользователь: {ur.current_user}")
