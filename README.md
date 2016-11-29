# Twitter-Weather-Bot
A twitter bot that tweets each five minute update for areas currently raining in Singapore. The actual bot is [@SGRaincloud](http://twitter.com/sgraincloud). The data and map are retrieved from the [Meteorological Service Singapore](http://www.weather.gov.sg/weather-rain-area-50km/).

## Dependencies
This script uses:
* `tweepy` as a python wrapper for the twitter API
* `requests` and `BeautifulSoup4` to pull data off the website (html text as well as image data)
* `pillow` for image manipulation
* `sys` to create an absolute path to the folder containing the script, for use in `crontab`
* `os` to check if `history` exists: if not, the main script will create an empty `history`

## Files
* `sgraincloud.py` is the main script dealing with parsing and retrieving information from the MSS website
* `getauth.py` is the script dealing with twitter's OAuth process. The object `API`, which deals with twittter, is created and called from the main script here
* `merge.py` is the `pillow` script that changes the transparency of the overlay, scales it to the map size, pastes it on the map, then adds the text for date and time
* `townshipmap_compressed.PNG` is the Singapore map with townships, retrieved from the MSS website
* `legend.png` is the edited legend available at weather.gov.sg
* `Aileron-Regular.otf` is the font file used to generate the text in merge.py (public domain)
