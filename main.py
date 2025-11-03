import requests
from bs4 import BeautifulSoup
zmienna_1: str = 'Kasia'
zmienna_2: str = 'Michasia'
zmienna_3: str = 'Zdzisia'
zmienna_4: str = 'Mateusz'

users: list = [
    {'name': zmienna_1, 'location': 'Łódź', 'posts': 67, "img_url":""},
    {'name': zmienna_2, 'location': 'Paryż', 'posts': 22, "img_url":""},
    {'name': zmienna_3, 'location': 'Wrocław', 'posts': 55, "img_url":""},
    {'name': zmienna_4, 'location': 'Warszawa', 'posts': 3, "img_url":""}

]

def user_info(users_data: list) -> None:
    print('Wybrano funkcje wyświetlania aktywności znajomych')
    for user in users_data:
        print(f'Your user {user['name']}, from {user['location']}, has {user['posts']} posts.')

def add_user(users_data: list) -> None:
    print('Wybrano funkcje dodawania znajomego')
    name: str = input('Enter your name: ')
    location: str = input('Enter your location: ')
    posts: int = int(input('Enter number of posts: '))
    img_url: str = input('Enter your image url: ')
    users_data.append({'name': name, 'location': location, 'posts': posts, "img_url": img_url})
    print('User added!')

def remove_user(users_data: list) -> None:
    print('Wybrano funkcje usuwania znajomego')
    tmp_name: str = input('Enter your name: ')
    for user in users:
        if user['name'] == tmp_name:
            users.pop(users.index(user))

def update_user(users_data: list) -> None:
    print('Wybrano funkcje aktualizacji użytkownika')
    tmp_name: str = input('Enter old name: ')
    for user in users:
        if user['name'] == tmp_name:
            user['name'] = input('Enter new name: ')
            user['location'] = input('Enter new location: ')
            user['posts'] = input('Enter new amount of posts: ')
def get_coordinates(city_name:str)->list:

    url:str = f'https://pl.wikipedia.org/wiki/{city_name.lower()}'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/122.0.0.0 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    # print(response.text)
    response_html = BeautifulSoup(response.text, 'html.parser')
    # print(response_html.prettify())
    latitude = float(response_html.select('.latitude')[1].text.replace(',','.'))
    longitude = float(response_html.select('.longitude')[1].text.replace(',','.'))
    # print(latitude, longitude)
    return [latitude, longitude]

def get_map(users_data:list)-> None:
    import folium
    m = folium.Map(location = [52.23 , 21.0], zoom_start = 6)
    for user in users_data:
         folium.Marker(
             location=get_coordinates(user['location']),
             tooltip="Click me!",
             popup=f"<h4> user: {user["name"]} </h4> {user["posts"]}, {user["location"]}, <img src = {user['img_url']}  alt = '1' />",
             icon=folium.Icon(icon="cloud"),
        ).add_to(m)

    m.save('notatnik.html')

while True:
    print("===================MENU=======================")
    print("0. Wyjscie z programu")
    print("1. Wyświetlanie użytkowników")
    print("2. Dodaj znajomego")
    print("3. Usuń znajomego")
    print("4. Aktualizuj znajomego")
    print("5. Generuj mape")
    print("=============================================")

    tmp_choice:int= int(input('Wybierz opcje menu: '))
    if tmp_choice == 0:
        break
    if tmp_choice == 1:
        user_info(users)
    if tmp_choice == 2:
        add_user(users)
    if tmp_choice == 3:
        remove_user(users)
    if tmp_choice == 4:
        update_user(users)
    if tmp_choice == 5:
        get_map(users)
