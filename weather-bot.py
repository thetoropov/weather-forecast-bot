import discord
import requests
from discord.ext import commands

DISCORD_TOKEN = 'YOUR_TOKEN'
bot = commands.Bot(command_prefix='!')

WEATHER_API_KEY = "YOUR_API_KEY"
base_url = "http://api.openweathermap.org/data/2.5/weather?"

result = ""


@bot.command(pass_context=False)
async def helper(ctx):
    await ctx.send("!weather <city name or city code> - return today weather forecast")


@bot.command(pass_context=True)
async def weather(ctx, arg):
    city_name = arg
    full_url = base_url + "q=" + city_name + "&appid=" + WEATHER_API_KEY

    response = requests.get(full_url)
    data = response.json()

    if data["cod"] != "404":
        main_part = data["main"]
        current_temperature = main_part["temp"]
        current_pressure = main_part["pressure"]
        current_humidity = main_part["humidity"]
        wind_part = data["wind"]
        current_wind_speed = wind_part["speed"]
        weather_part = data["weather"]
        weather_description = weather_part[0]["description"]

        result = " Temperature: " + str(round(current_temperature - 273.15, 2)) + " °C" + \
                 "\n Atmospheric pressure: " + str(current_pressure) + " hpa" + \
                 "\n Humidity: " + str(current_humidity) + " %" + \
                 "\n Wind speed: " + str(current_wind_speed) + " m/s" + \
                 "\n Description: " + str(weather_description)

        if weather_description == "shower rain" or weather_description == "rain":
            result += "\n Tips: " + "Grab an umbrella"
        elif weather_description == "thunderstorm" or weather_description == "mist":
            result += "\n Tips: " + "Better stay in"
        elif weather_description == "snow" or current_temperature < 0:
            result += "\n Tips: " + "Dress warmly"
        elif weather_description == "broken clouds":
            result += "\n Tips: " + "Dress as usual and grab an umbrella"
        elif weather_description == "scattered clouds" or weather_description == "few clouds":
            result += "\n Tips: " + "Dress as usual"
        elif weather_description == "clear sky" and current_temperature > 10:
            result += "\n Tips: " + "Leave your jacket at home"
        else:
            result += "\n Tips: " + "Sorry, no tips today"
    else:
        result = " City not found"

    await ctx.send(result)

bot.run(DISCORD_TOKEN)
