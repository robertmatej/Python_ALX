
slownik = {'consolidated_weather': [{'id': 5534184055504896, 'weather_state_name': 'Light Cloud', 'weather_state_abbr': 'lc',
            'wind_direction_compass': 'NW', 'created': '2018-11-29T19:52:27.052953Z', 'applicable_date': '2018-11-29',
            'min_temp': 1.2966666666666666, 'max_temp': 6.863333333333333, 'the_temp': 5.9350000000000005, 'wind_speed': 9.79340223887961,
            'wind_direction': 312.00826430746326, 'air_pressure': 1013.0899999999999, 'humidity': 60, 'visibility': 15.125417561441184,
            'predictability': 70}, {'id': 5271427922001920, 'weather_state_name': 'Heavy Cloud', 'weather_state_abbr': 'hc', 'wind_direction_compass': 'WSW',
            'created': '2018-11-29T19:52:29.797951Z', 'applicable_date': '2018-11-30', 'min_temp': -2.195, 'max_temp': 4.96, 'the_temp': 3.585, 'wind_speed': 2.886694968299796,
            'wind_direction': 247.80749059353582, 'air_pressure': 1018.63, 'humidity': 72, 'visibility': 10.922152131551737, 'predictability': 71}, {'id': 6705323557519360,
            'weather_state_name': 'Light Rain', 'weather_state_abbr': 'lr', 'wind_direction_compass': 'ENE', 'created': '2018-11-29T19:52:32.448885Z', 'applicable_date': '2018-12-01',
            'min_temp': -0.9650000000000001, 'max_temp': 7.539999999999999, 'the_temp': 5.58, 'wind_speed': 3.7900970756011563, 'wind_direction': 70.83172781476682, 'air_pressure': 1023.24,
            'humidity': 80, 'visibility': 13.534707309313609, 'predictability': 75}, {'id': 5121158122831872, 'weather_state_name': 'Heavy Rain', 'weather_state_abbr': 'hr', 'wind_direction_compass': 'SSW', 'created': '2018-11-29T19:52:35.793878Z',
            'applicable_date': '2018-12-02', 'min_temp': 8.756666666666666, 'max_temp': 16.186666666666667, 'the_temp': 15.725, 'wind_speed': 5.525163594424561, 'wind_direction': 197.84926866798511, 'air_pressure': 1005.0899999999999, 'humidity': 92,
            'visibility': 6.964639008192158, 'predictability': 77}, {'id': 6336917872312320, 'weather_state_name': 'Light Cloud', 'weather_state_abbr': 'lc', 'wind_direction_compass': 'W', 'created': '2018-11-29T19:52:39.096138Z',
            'applicable_date': '2018-12-03', 'min_temp': 3.7466666666666666, 'max_temp': 10.006666666666666, 'the_temp': 9.745, 'wind_speed': 8.314276594856702, 'wind_direction': 273.6593983425343, 'air_pressure': 1006.22, 'humidity': 69,
            'visibility': 12.50633798616082, 'predictability': 70}, {'id': 5062045716185088, 'weather_state_name': 'Heavy Rain', 'weather_state_abbr': 'hr', 'wind_direction_compass': 'N', 'created': '2018-11-29T19:52:42.654915Z',
            'applicable_date': '2018-12-04', 'min_temp': 1.37, 'max_temp': 4.986666666666667, 'the_temp': 6.48, 'wind_speed': 3.2959820647419074, 'wind_direction': 351.5, 'air_pressure': 1010.9, 'humidity': 70, 'visibility': 7.823063310268035,
            'predictability': 77}], 'time': '2018-11-29T17:01:55.171793-05:00', 'sun_rise': '2018-11-29T06:59:20.077342-05:00', 'sun_set': '2018-11-29T16:30:29.301941-05:00', 'timezone_name': 'LMT', 'parent': {'title': 'New Jersey',
            'location_type': 'Region / State / Province', 'woeid': 2347589, 'latt_long': '40.143230,-74.726707'}, 'sources': [{'title': 'BBC', 'slug': 'bbc', 'url': 'http://www.bbc.co.uk/weather/', 'crawl_rate': 180}, {'title': 'Forecast.io',
            'slug': 'forecast-io', 'url': 'http://forecast.io/', 'crawl_rate': 480}, {'title': 'Met Office', 'slug': 'met-office', 'url': 'http://www.metoffice.gov.uk/', 'crawl_rate': 180}, {'title': 'OpenWeatherMap', 'slug': 'openweathermap',
            'url': 'http://openweathermap.org/', 'crawl_rate': 360}, {'title': 'World Weather Online', 'slug': 'world-weather-online', 'url': 'http://www.worldweatheronline.com/', 'crawl_rate': 360}, {'title': 'Yahoo', 'slug': 'yahoo',
            'url': 'http://weather.yahoo.com/', 'crawl_rate': 180}], 'title': 'Newark', 'location_type': 'City', 'woeid': 2459269, 'latt_long': '40.731972,-74.174179', 'timezone': 'America/New_York'}

print (slownik)
print (type(slownik))

print (slownik['consolidated_weather'][2]['the_temp'])

slownik2 = {'poziom1': [{'klucz20': [{'klucz220':"wart220",'klucz221':'klucz221'}, {'klucz21': 'wart21','klucz22': 'wart22'},{'klucz30': "wart30", 'klucz31': 'wart31','klucz32': 'wart32'}]}]}


print (slownik2)
print (type(slownik2))
print(slownik2.values())
print (slownik2.items())
print (slownik2["poziom1"][0]['klucz20'][2]['klucz31'])
print (slownik2["poziom1"][0]['klucz20'][0]['klucz221'])