import paho.mqtt.client as mqtt   #MQTT-Client-Bibliothek

def on_connect(client, userdata, flags, rc):    #Callback-Funktion, die aufgerufen wird, wenn der Client sich mit dem Broker verbindet
    print("✅ Verbunden mit MQTT-Broker")
    client.subscribe("factory/line1/temperature")

def on_message(client, userdata, msg):      #Callback-Funktion, die aufgerufen wird, wenn eine Nachricht empfangen wird
    try:
        temp = float(msg.payload.decode())              #Dekodieren der empfangenen Nachricht und Umwandlung in einen Float-Wert
        print(f"🌡️ Temperatur empfangen: {temp} °C")
        if temp > 30:
            client.publish("factory/line1/cooling", "on")   #Veröffentlichen einer Nachricht, um die Kühlung einzuschalten
            print("❄️ Kühlung eingeschaltet")
        elif temp < 28:
            client.publish("factory/line1/cooling", "off")  #Veröffentlichen einer Nachricht, um die Kühlung auszuschalten
            print("🛑 Kühlung ausgeschaltet")
    except ValueError:                                      #Fehlerbehandlung, falls die empfangene Nachricht kein gültiger Temperaturwert ist
        print("⚠️ Ungültiger Temperaturwert")

client = mqtt.Client()                                  #Erstellen eines neuen MQTT-Clients
client.on_connect = on_connect             #Zuweisen der Callback-Funktion für die Verbindung   
client.on_message = on_message          #Zuweisen der Callback-Funktion für empfangene Nachrichten
client.connect("localhost", 1883, 60)       #Verbinden mit dem MQTT-Broker auf localhost, Port 1883, mit einer Keep-Alive-Zeit von 60 Sekunden
client.loop_forever()                   #Starten der Endlosschleife, um auf eingehende Nachrichten zu warten und die Callback-Funktionen auszuführen
