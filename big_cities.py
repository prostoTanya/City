from opencage.geocoder import OpenCageGeocode
from tkinter import *

def get_coordinates(city, key):
    try:
        geocoder = OpenCageGeocode(key)
        results = geocoder.geocode(city, language='ru')
        if results:
            lat = round(results[0]['geometry']['lat'], 2)
            lng = round(results[0]['geometry']['lng'], 2)
            country = results[0]['components']['country']
            region = results[0]['components']['state']
            return f'широта {lat}, долгота {lng},\n страна: {country}, регион: {region}'
        else:
            return 'Город не найден'
    except Exception as e:
        return f'Возникла ошибка: {e}'


def show_coordinates(event=None):
    city = entry.get()
    coordinates = get_coordinates(city, key)
    label.config(text=f'Координаты города {city}:\n {coordinates}')


key = 'd5b71846be824325962bacae0dfc5ebd'

window = Tk()
window.title('Координаты городов')
window.geometry('300x200')

entry = Entry()
entry.pack()
entry.bind('<Return>', show_coordinates)

button = Button(text='Поиск координат', command=show_coordinates)
button.pack()

label = Label(text='Введите город и нажмите на кнопку')
label.pack()

window.mainloop()
