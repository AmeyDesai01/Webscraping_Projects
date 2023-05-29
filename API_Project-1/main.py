import requests
import os
from datetime import datetime

user_api = os.environ['Weather_API']  #stored key in Environment variable
#print(user_api)

location = input("Enter the city name:") #city name

#pasted from website : https://api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}
complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+user_api

api_link = requests.get(complete_api_link)
api_data = api_link.json()
#print (api_data)

if api_data['cod']=='404':
    print ("Invalid City : {}, Please check your city name".format(location))
else:
    #create vaaribles to store and display data
    temp_city = ((api_data['main']['temp']) -273.15) #line calculates the temperature in Celsius by subtracting 273.15 from the temperature obtained from the 'main' section of the api_data dictionary.
    weather_desc = api_data['weather'][0]['description'] #line retrieves the weather description from the 'weather' section of the api_data dictionary.
    hmdt = api_data['main']['humidity']
    wind_spd = api_data['wind']['speed']
    date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %P") #line gets the current date and time using the datetime module and formats it to the specified string format ("%d %b %Y | %I:%M:%S %P").


    print ("________________________________________________________________")
    print ("Weather Stats for -{} || {}".format(location.upper(),date_time))   #statements are used to print separators and the location along with the date and time.
    print ("________________________________________________________________")

    print ("Current temperature is: {:.2f} deg C" .format(temp_city)) #displays the current temperature with two decimal places.
    print ("Current weather desc :",weather_desc) #display the weather description.
    print ("Current Humidity  :",hmdt, '%')  #displays the humidity percentage.
    print ("Current wind speed  :",wind_spd,'kmph') #display the wind speed in kilometers per hour.


