import requests
from datetime import datetime
api_key = '34dd060a0fa3b8e49b8dfc4df699be8a'
import requests

apikey1='5c8f76db28e4ce2797d0da6162596d23e7b426f6'
url1=f"https://api.waqi.info/feed/{location1}/?token={apikey1}"
resp =requests.get(url1)
data1 = resp.json()
aqi = data1['data']['aqi']

def mainpart():
  A="Agriculture"
  B="Air Quality"
  C="Allergy Outlook"
  D="Tourism"
  E="Weather Alert"
  print("'A' for Agriclture" )
  print("'B' for Air Quality")
  print("'C' for Allergy Outlook")
  print("'D' for Tourism")
  print("'E' for Weather Alert")

mainpart()
k=input("Enter your need: ")

if k=='A':
  print("---------------------------------------------------------------------------------")
  print("                      Welcome To Agricultural Field                        ")
  print("---------------------------------------------------------------------------------")
  location=input("Enter the city name:")
  complete_api_link ="http://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+api_key
  api_link = requests.get(complete_api_link)
  api_data = api_link.json()
  temp_city =((api_data['main']['temp'])-273.15)
  weather_desc = api_data['weather'][0]['description']
  hmdt = api_data['main']['humidity']
  wind_spd = api_data['wind']['speed']
  date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p") 
  print("---------------------------------------------------------------------------------")
  print("Weather Status for - {} || {}".format(location.upper(),date_time))
  print("---------------------------------------------------------------------------------")
  print("Current temperature : {:.2f} deg C".format(temp_city))
  print("Current Weather Description :",weather_desc )
  print("Current Humidity :",hmdt,'%')
  print("Current Wind Speed :",wind_spd, 'kmph')
  print("                                                                              ")
  print("Crops that can be cultivated in this city are:                                ")
  print("                                                                                ")                                             
  if temp_city >=0 and temp_city <=10 :
    li=["cardamo, flax, sugar beet"]
    print(li)
  elif temp_city >=11 and temp_city <=20:
    li1=["Rice, wheat, maize, millets, pulses, rabi, oil seeds, groundnut, sugar cane, sugar beet, cotton, tea, cofee, cocoa, flax, black pepper, cardamom, turmeric"]
    print(li1)
  elif temp_city >=21 and temp_city <=30: 
    li2=["Rice, wheat, maize, millets, bajra, pulses, rabi, oilseeds, groundnut, sugarcane, sugar beet, cotton, tea, coffee,cocoa, rubber, jute, coconut, oil plam, clove, blace pepper, cardamom,turmeric"]
    print(li2)
  elif temp_city >=31 and temp_city <=40:
    li3=["Millets, bajra,sugar cane, tea, cocoa, jute, oil palm, clove, black pepper, cardamom"]
  else:
    print("Crops can't be cultivated at these climate")
  


elif k=='B': 
  print("-----------------------------------------------------------------------------------")                           
  print("                                 Air Quality                                       ")
  print("-----------------------------------------------------------------------------------")
  import requests
  location1=input("Enter the city name:")
  apikey1='5c8f76db28e4ce2797d0da6162596d23e7b426f6'
  url1=f"https://api.waqi.info/feed/{location1}/?token={apikey1}"
  resp =requests.get(url1)
  data1 = resp.json()
  aqi = data1['data']['aqi']
  from matplotlib import colors
  aqi = data1['data']['aqi']
  print("\033[1;30;47m The air quality index of",location1, "is", aqi)
  print("")
  iaqi = data1['data']['iaqi']

  print("\033[1;30;47m Pollutants present in air and their amount:")                                                                                                  
  print("\033[5;37;0m")                                                   
  for i in iaqi.items():
    print( i[0],':',i[1]['v'])
  print("") 

  print("\033[1;31;47m Current Condition!!!  \n")


  if aqi >=0 and aqi <=50 :
    print("\033[1;32;47m Good  \n")
    print("\033[0;30;0m Air quality is considered satisfactory, and air pollution poses little or no risk")
  elif aqi >=51 and aqi <=100:
    print("\033[1;32;47m Moderate  \n")
    print("\033[0;30;0m Air quality is acceptable; however, for some pollutants there  may be a \n moderate health concern for a very small number of  people  who are \n unusually sensitive to air pollution.")
  elif aqi >=101 and aqi <=150: 
    print("\033[1;32;47m Unhealthy for sensitive groups  \n")
    print("\033[0;30;0m Members of sensitive groups may experience health effects. The general public is not \n likely to be affected.")
  elif aqi >=151 and aqi <=200:
    print("\033[1;32;47m Unhealthy  \n")
    print("\033[0;30;0m Everyone may begin to experience health effects; members of sensitive groups may\n experience more serious health effects")
  elif aqi >=201 and aqi <=300: 
    print("\033[1;32;47m Very Unhealthy \n")
    print("\033[0;30;0m Health warnings of emergency conditions. The entire population is more likely to \n be affected.")
  elif aqi >300:
    print("\033[1;32;47m Hazardous  \n")
    print("\033[0;30;0m	Health alert: everyone may experience more serious health effects")
    
  from matplotlib.widgets import TextBox
  import matplotlib.pyplot as plt
  print("")
  Pollutants = [i for i in iaqi]
  values = [i['v'] for i in iaqi.values()]

  plt.figure(figsize=(6,5))
  #plt.pie(values,labels=Pollutants,autopct='%1.01f%%')
  plt.title("Pollutants",fontsize=20)
  plt.show
  plt.bar(Pollutants,values)
  plt.show
  

elif k=='C':
    print("---------------------------------------------------------------------------------")
    print("                      Allergy Outlook                      ")
    print("---------------------------------------------------------------------------------")

    import requests
    location1=input("Enter the city name:")
    apikey1='5c8f76db28e4ce2797d0da6162596d23e7b426f6'
    url1=f"https://api.waqi.info/feed/{location1}/?token={apikey1}"
    resp =requests.get(url1)
    data1 = resp.json()
    aqi = data1['data']['aqi']
    from matplotlib import colors
    aqi = data1['data']['aqi']
    print("\033[1;30;47m Chances of getting allergy in ",location1, "is : ")
    print("")
    iaqi = data1['data']['iaqi']


    if aqi >=0 and aqi <=50 :
      print("\033[1;32;47m Chance of getting allergy is very low...  \n")
      
    elif aqi >=51 and aqi <=100:
        print("\033[1;32;47m Chance of getting allergy is low... \n")
      
    elif aqi >=101 and aqi <=150: 
        print("\033[1;32;47m Chances of getting allergy  \n")
        
    elif aqi >=151 and aqi <=200:
        print("\033[1;32;47m Chance of getting allergy is more... \n")
        
    elif aqi >=201 and aqi <=300: 
        print("\033[1;32;47m Chance of getting allergy is very high... \n")
      
    elif aqi >300:
        print("\033[1;32;47m Chance of getting allergy is very very high... \n")
        
        iaqi = data1['data']['iaqi']

    print("\033[1;30;47m Pollutants present in air and their amount:")                                                                                                  
    print("\033[5;37;0m")                                                   
    for i in iaqi.items():
      print( i[0],':',i[1]['v'])
    print("") 
  
elif k=='D':
  print("**********************************************************************************************")
  print("                                Welcome to Tourism Area                                       ")
  print("**********************************************************************************************")
  location=input("Enter the city name:")
  complete_api_link ="http://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+api_key


  api_link = requests.get(complete_api_link)
 
  api_data = api_link.json()
 
  temp_city =((api_data['main']['temp'])-273.15)
  weather_desc = api_data['weather'][0]['description']
  hmdt = api_data['main']['humidity']
  wind_spd = api_data['wind']['speed']
  date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p") 
  

  print("---------------------------------------------------------------------------------")
  print("Weather Status for - {} || {}".format(location.upper(),date_time))
  print("---------------------------------------------------------------------------------")
  print("Current temperature : {:.2f} deg C".format(temp_city))
  print("Current Weather Description :",weather_desc )
  print("Current Humidity :",hmdt,'%')
  print("Current Wind Speed :",wind_spd, 'kmph')
  print("__Current tourist update__")

  if temp_city >=-10 and temp_city <=0 :
    print("Extreme cold \n Good place for people who \n loves extreme cold climate")
  elif temp_city >=1 and temp_city <=10:
    print("Cold \n Good place for people who \n loves cold climate.")
  elif temp_city >=11 and temp_city <=20: 
    
    print("Little cold \n Good place")
  elif temp_city >=21 and temp_city <=30:
    print ("Moderate Climate")
  elif temp_city >=31 and temp_city <=40:
    print ("Hot")
  elif temp_city >=41 and temp_city <=50:
    print ("Very Hot")
  else:
    print("Bad climate")
  import requests
  city_name = input("Enter the name of the City : ")  
    # Function to Generate Report
  def Gen_report(C):
        url = 'https://wttr.in/{}'.format(C)
        try:
            data = requests.get(url)
            T = data.text
        except:
            T = "Error Occurred"
        print(T)
        
  Gen_report(city_name)

elif k=='E':
    print("----------------------------------------------------------")
    print("                   SKY STATUS                             ")
    print("----------------------------------------------------------")
 

 
    location=input("Enter the city name:")
    complete_api_link ="http://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+api_key
    api_link = requests.get(complete_api_link)
    api_data = api_link.json()
    temp_city =((api_data['main']['temp'])-273.15)
    weather_desc = api_data['weather'][0]['description']
    hmdt = api_data['main']['humidity']
    wind_spd = api_data['wind']['speed']
    date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p") 
    print("---------------------------------------------------------------------------------")
    print("Weather Condition for - {} || {}".format(location.upper(),date_time))
    print("---------------------------------------------------------------------------------")
    print("Current temperature : {:.2f} deg C".format(temp_city))
    print("Current Weather Description :",weather_desc )
    print("Current Humidity :",hmdt,'%')
    print("Current Wind Speed :",wind_spd, 'kmph')
    if weather_desc=='clear sky':
      import matplotlib.pyplot as plt
      import matplotlib.image as mpimg
      img = mpimg.imread('/content/drive/MyDrive/Colab Notebooks/clear sky.jpg')
      imgplot = plt.imshow(img)
      plt.show()
    elif weather_desc=='few clouds':
      import matplotlib.pyplot as plt
      import matplotlib.image as mpimg
      img = mpimg.imread('/content/drive/MyDrive/Colab Notebooks/few clouds.jpg')
      imgplot = plt.imshow(img)
      plt.show()
    elif weather_desc=='scattered clouds':
      import matplotlib.pyplot as plt
      import matplotlib.image as mpimg
      img = mpimg.imread('/content/drive/MyDrive/Colab Notebooks/scattered clouds.jpg')
      imgplot = plt.imshow(img)
      plt.show()
    elif weather_desc=='broken clouds':
      import matplotlib.pyplot as plt
      import matplotlib.image as mpimg
      img = mpimg.imread('/content/drive/MyDrive/Colab Notebooks/broken clouds.jpg')
      imgplot = plt.imshow(img)
      plt.show()
    elif weather_desc=='shower rain':
      import matplotlib.pyplot as plt
      import matplotlib.image as mpimg
      img = mpimg.imread('/content/drive/MyDrive/Colab Notebooks/shower rain.jpg')
      imgplot = plt.imshow(img)
      plt.show()
    elif weather_desc=='rain':
      import matplotlib.pyplot as plt
      import matplotlib.image as mpimg
      img = mpimg.imread('/content/drive/MyDrive/Colab Notebooks/rain.jpg')
      imgplot = plt.imshow(img)
      plt.show()
    elif weather_desc=='heavy intensity rain':
      import matplotlib.pyplot as plt
      import matplotlib.image as mpimg
      img = mpimg.imread('/content/drive/MyDrive/Colab Notebooks/rain.jpg')
      imgplot = plt.imshow(img)
      plt.show()  
    elif weather_desc=='thunderstorm':
      import matplotlib.pyplot as plt
      import matplotlib.image as mpimg
      img = mpimg.imread('/content/drive/MyDrive/Colab Notebooks/thunderstorm.jpg')
      imgplot = plt.imshow(img)
      plt.show()
    elif weather_desc=='snow':
      import matplotlib.pyplot as plt
      import matplotlib.image as mpimg
      img = mpimg.imread('/content/drive/MyDrive/Colab Notebooks/snow.jpg')
      imgplot = plt.imshow(img)
      plt.show()
    elif weather_desc=='mist':
      import matplotlib.pyplot as plt
      import matplotlib.image as mpimg
      img = mpimg.imread('/content/drive/MyDrive/Colab Notebooks/mists.jpg')
      imgplot = plt.imshow(img)
      plt.show()

