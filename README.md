# Умный сервис прогноза погоды
## Проектирование сервиса
**Язык программирования:** Python  
**Пользовательский интерфейс:** Discord-bot  
**Формат ответа:**  
Temperature: ___ °C  
Atmospheric pressure: ___ hpa  
Humidity: ___ %  
Wind speed: ___ m/s  
Description: ___  
Tips: ___  
## Демонстрация работы сервиса
![alt text](https://github.com/thetoropov/weather-forecast-bot/blob/master/work1.PNG)  
![alt text](https://github.com/thetoropov/weather-forecast-bot/blob/master/work2.PNG)
## Процесс работы программы
Чат-бот имеет две команды:
* ```!helper``` 
  * высылает инструкцию
* ```!weather <city_name or city_code> ```
  * Серсис получает данные от пользователя через интерфейс чата
  * Формирует запрос на API openweathermap.org
  * Формирует ответ по шаблону из полученных данных
  * Высылает информацию пользователю

## Как запустить бота?
* В discord создать новое приложение и скопировать Client ID  
* В разделе bot создать бота и скопировать Token  
* Зарегистрироваться на openweathermap.org, скопировать api key  
* Заменить ```DISCORD_TOKEN``` и ```WEATHER_API_KEY``` на свои значения  
* Добавить бота на сервер  
```https://discordapp.com/oauth2/authorize?&client_id={ClientID}&scope=bot&permissions=66395456``` 
* Запустить ```weather-bot.py```
* Воспользоваться ботом
