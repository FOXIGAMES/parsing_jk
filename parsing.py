'===========================================Parsing====================================================='
# парсинг - процесс автоматического сбора данных

# Библиотеки
# 1. requeats - отправляет запрос на сайт и в итоге получает html код страницы
# 2. Beautiful Soup - помогает извлечь информацию из html. Помогает обращаться к определенным тегам и вытаскивать инфо
# 3. lxml - выступает в роли парсера для Beautiful Soup (разбивает информацию на мелкие части и анализирует данные)

# python3 -m venv venv - создание виртуального окружения

# sourse venv/bin/activate - активировали вирутальрное окружение
# . venv/bin/activate

# import requests
# from bs4 import BeautifulSoup
# import csv

# URL = 'http://kenesh.kg/ru/news/all/list'

# def write_to_csv(data):
#     with open('data.csv', 'a') as file:
#         writer = csv.writer(file)
#         writer.writerow([data['title'], data['price'], data['image']])

# def get_html(url):
#     response = requests.get(url)
#     return response.text

# def get_data(html):
#     soup = BeautifulSoup(html, 'lxml')
#     list_comp = soup.find_all('div', class_ = 'row')
#     print(list_comp)
#     for comp in list_comp:
#         title = comp.find('span', class_ = 'prouct_name').text
#         price = comp.find('span', class_ = 'price').text
#         image = 'https://enter.kg' + comp.find('img').get('src')
#         dict_ = {'title':title, 'price': price, 'image':image}
#         write_to_csv(dict_)

# print(get_data(get_html(URL)))

# import requests
# from bs4 import BeautifulSoup
# import csv

# def get_page_data(url):
#     response = requests.get(url)
#     soup = BeautifulSoup(response.content, 'html.parser')
#     articles = soup.find_all('div', class_='col-xs-12 col-sm-6 col-md-6 col-lg-4')
#     data = []
#     for article in articles:
#         img = article.find('img')['src']
#         date = article.find('span', class_='date').text.strip()
#         title = article.find('h3').text.strip()
#         data.append({'img': img, 'date': date, 'title': title})
#     return data

# # Основная функция для парсинга и сохранения данных
# def scrape_website():
#     base_url = 'http://kenesh.kg/ru/news/all/list'
#     all_data = []
#     page = 1
#     while True:
#         url = base_url + f'?page={page}'
#         data = get_page_data(url)
#         if not data:
#             break
#         all_data.extend(data)
#         page += 1

#     # Сохранение данных в CSV-файл
#     filename = 'kenesh_data.csv'
#     with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
#         fieldnames = ['img', 'date', 'title']
#         writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
#         writer.writeheader()
#         writer.writerows(all_data)

#     print(f'Данные сохранены в файл: {filename}')

# # Вызов функции для выполнения парсинга
# scrape_website()

