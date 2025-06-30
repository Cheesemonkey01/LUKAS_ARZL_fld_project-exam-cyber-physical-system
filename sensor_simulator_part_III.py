import time             #Zeitbibliothek für Pausen
import random           #Zufallsbibliothek für die Generierung von Temperaturwerten
import paho.mqtt.client as mqtt     #MQTT-Client-Bibliothek

client = mqtt.Client()                  #Erstellen eines neuen MQTT-Clients
client.connect("localhost", 1883, 60)       #Verbinden mit dem MQTT-Broker auf localhost, Port 1883, mit einer Keep-Alive-Zeit von 60 Sekunden

while True:
    temp = round(random.uniform(25.0, 35.0), 2)     #Generieren eines zufälligen Temperaturwerts zwischen 25.0 und 35.0, auf 2 Dezimalstellen gerundet
    client.publish("factory/line1/temperature", str(temp))      #Veröffentlichen des Temperaturwerts auf dem MQTT-Thema "factory/line1/temperature"
    print(f"🔼 Temperatur gesendet: {temp} °C")         #Ausgabe des gesendeten Temperaturwerts in der Konsole               
    time.sleep(5)           #Warten für 5 Sekunden, bevor der nächste Temperaturwert gesendet wird
