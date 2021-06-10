import paho.mqtt.client as mqtt  # import the client1
import time


client = mqtt.Client("Anton")  # создание клиента
print("Подключение к брокеру")
client.connect("127.0.0.1", 1883, 60)  # подключение к брокеру
client.loop_start()  # start the loop
print("Отправка сообщений в топик", "sensors")
while True:
    for i in range(10):
        value = i
        client.publish("sensors/values", value)
        time.sleep(4)
    for i in range(10, 0, -1):
        value = i
        client.publish("sensors/values", value)
        time.sleep(4)