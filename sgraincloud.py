import getauth, merge
import requests, bs4, os, sys, time

PATH = sys.path[0] + '/'
html = requests.get('http://www.weather.gov.sg/weather-rain-area-50km/')
soup = bs4.BeautifulSoup(html.text, 'html.parser')

if not os.path.isfile(PATH + 'history'):
    with open(PATH + 'history', 'w') as file:
        file.write('new history, 0')
        print("history file note found! Creating...")
with open(PATH + 'history', 'r') as file:
    history = (file.read())

try:
    datetime = soup.select('p#issueDate')[0].string
    overlay_url = soup.select('img#picture')[0].get('src')
except IndexError:
    # Notifies me if unable to obtain time or overlay_url
    print("IndexError in generated time or overlay_url!")
    # This is the user_id for @ningOTI
    getauth.API.send_direct_message(user_id='',
            text=time.strftime('[%H:%M %d/%m/%Y] - ') + 'IndexError!')

if datetime not in history:
    print("New update detected, starting tweet loop...")
    overlay_data = requests.get(overlay_url)
    with open(PATH + 'overlay.png', 'wb') as file:
        print("Writing overlay.png to working directory...")
        for chunk in overlay_data.iter_content(10000):
            file.write(chunk)

    # merge.generate creates overlaid_map.png in current directory
    print("Generating overlaid_map.png...")
    merge.generate(datetime, PATH + 'overlay.png') 

    print("Tweeting...")
    getauth.API.update_with_media(PATH + 'overlaid_map.png')

    with open(PATH + 'history', 'w') as file:
        print("Tweet loop successful, writing new history...")
        file.write("{}, {}".format(datetime, len(html.text)))
