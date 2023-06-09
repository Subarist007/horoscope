import gettext
from horoscope.models import Forecast
from datetime import date, timedelta
from django.shortcuts import render

"""Словарь соответствия знаков зодиака и описаний"""
zodiac_dict = {
    'aries': 'Овен - первый знак зодиака, планета Марс (с 21 марта по 20 апреля).',
    'taurus': 'Телец - второй знак зодиака, планета Венера (с 21 апреля по 21 мая).',
    'gemini': 'Близнецы - третий знак зодиака, планета Меркурий (с 22 мая по 21 июня).',
    'cancer': 'Рак - четвёртый знак зодиака, Луна (с 22 июня по 22 июля).',
    'leo': 'Лев - пятый знак зодиака, солнце (с 23 июля по 21 августа).',
    'virgo': 'Дева - шестой знак зодиака, планета Меркурий (с 22 августа по 23 сентября).',
    'libra': 'Весы - седьмой знак зодиака, планета Венера (с 24 сентября по 23 октября).',
    'scorpio': 'Скорпион - восьмой знак зодиака, планета Марс (с 24 октября по 22 ноября).',
    'sagittarius': 'Стрелец - девятый знак зодиака, планета Юпитер (с 23 ноября по 22 декабря).',
    'capricorn': 'Козерог - десятый знак зодиака, планета Сатурн (с 23 декабря по 20 января).',
    'aquarius': 'Водолей - одиннадцатый знак зодиака, планеты Уран и Сатурн (с 21 января по 19 февраля).',
    'pisces': 'Рыбы - двенадцатый знак зодиака, планеты Юпитер (с 20 февраля по 20 марта).',
}

"""Обрабатывает главную страницу"""
def index(request):
    context = {
        'title': 'Гороскоп',
    }
    return render(request, 'horoscope/index.html', context)

"""О проекте"""
def about(request):
    context = {
        'title': 'О проекте',
    }
    return render(request, 'horoscope/about.html', context)

"""Контакты"""
def contacts(request):
    context = {
        'title': 'Контакты',
    }
    return render(request, 'horoscope/contacts.html', context)

"""Обрабатывает знаки зодиака"""
def sign_zodiac(request, zodiac_sign):
    today = date.today().isoformat() # Формирует сегодняшнюю дату
    yesterday = date.today() - timedelta(days=1) # Формирует вчерашнюю дату
    context = {
        'title': zodiac_dict[zodiac_sign].split()[0], # Выбранный знак зодиака
        'sign': zodiac_dict[zodiac_sign], # Описание выбранного знака
        'description': Forecast.objects.filter(data=today, name=zodiac_sign)[0].description, # Описание прогноза гороскопа
        'lucky_number': Forecast.objects.filter(data=today, name=zodiac_sign)[0].lucky_number, # Счастливое число
        'color': Forecast.objects.filter(data=today, name=zodiac_sign)[0].color, # Счастливый цвет
        'date': today # Выводит настоящую дату
    }
    return render(request, 'horoscope/sign_zodiac.html', context)


