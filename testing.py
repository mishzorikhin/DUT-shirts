"""import pymorphy2
morph = pymorphy2.MorphAnalyzer()


otv = morph.parse('Миша')[0]


print('nomn'+ " : " +otv.inflect({'nomn'})[0])
print('gent'+ " : " +otv.inflect({'gent'})[0])
print('accs'+ " : " +otv.inflect({'accs'})[0])
print('ablt'+ " : " +otv.inflect({'ablt'})[0])
print('loct'+ " : " +otv.inflect({'loct'})[0])
print('voct'+ " : " +otv.inflect({'voct'})[0])


markers = ['где' ,'находится' ,'пройти' ,'дехать' ,'добраться', 'попасть', 'как']
markersNorm = []

for i in markers:
    print(morph.parse(i)[0].normal_form)
"""
from bs4 import BeautifulSoup
import requests
from selenium import webdriver

# План:
# 1. Получиьт html
# 2. Получить view in game
# 3. Скинуть view in game на api csgo float
# 4. Проверить если паттерн == указанному пользователем, то пт. 5, иначе продолжить скан
# 5. Поставиьт в таблицу ссылку на просмотр скина, покупку скина, флоат, паттерн, и полное название скина

# steam://rungame/730/76561202255233023/+csgo_econ_action_preview%20M 2774699123308596407 A 16375236507 D 5684297427044664177
# https://steamcommunity.com/market/listings/730/AK-47%20%7C%20Redline%20%28Field-Tested%29

# class Bot:
#     def __init__(self):
#         self.driver = webdriver.Chrome('/home/dmax/Загрузки/chromedriver/chromedriver')
#         self.navigate()
#
#     def navigate(self):
#         self.driver.get('https://steamcommunity.com/market/listings/730/AK-47%20%7C%20Redline%20%28Field-Tested%29')
#
#         button = self.driver.find_element_by_xpath('//a[@id="listing_3523422564412371245_actionmenu_button"')
#         button.click()

extension='/home/user/.config/google-chrome/Default/Extensions/fdjsidgdhskifcclfjowijfwidksdj/2.3.4_22.crx'
options = webdriver.ChromeOptions()
options.add_extension(extension)

driver = webdriver.Chrome('D:/загрузки/chromedriver')  # загружает вебдрайвер для хрома
driver.set_window_size(1425, 1080)  # делает размер окна 425x720


def get_html(url):  # возвращает html страницы
    r = requests.get(url)
    return r.text


def get_pattern(url_inspect):  # возвращяет паттерн скина из кс го
    url = requests.get('https://api.csgofloat.com/?url=' + url_inspect)
    return url.json()['iteminfo']['paintseed']


def get_inspect_url(html, patterns, url):  # получает ссылку для осмотра оружия
    soup = BeautifulSoup(html, 'lxml')
    asd = soup.find('div', class_='item_desc_game_info').get('id')
    print(asd)

    things = soup.find('div', id='searchResultsRows').find_all('div', class_='market_action_popup')
    driver.get(url)

    for thing in things:
        # name, float, pattern, buy_href, inspect_href
        listing_id = thing.find('div', class_='market_action_popup')
        url_hoverable = driver.find_element_by_xpath('//div[@id="' +listing_id.get('id') + '"]/div[@class="market_listing_item_name_block"]/span[@class="market_listing_item_name economy_item_hoverable"]')
        url_hoverable.click()



def main():
    patterns = [15, 251]
    url = 'https://steamcommunity.com/market/listings/730/AK-47%20%7C%20Redline%20%28Field-Tested%29'
    get_inspect_url(get_html(url), patterns, url)


if __name__ == '__main__':
    main()
