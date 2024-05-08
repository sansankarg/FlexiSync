import sqlite3
data1 = None
data2 = None
data3 = None
def main():
    from app import mqtt
    mqtt.subscribe('data1')
    mqtt.subscribe('data2')
    mqtt.subscribe('data3')
    while(True):
        @mqtt.on_message()
        def handle_mqtt_message(client, userdata, message):
            data = dict(
                topic=message.topic,
                payload=message.payload.decode()
            )
            data = message.payload.decode().split(",")
            data1 = data[0]
            data2 = data[1]
            data3 = data[2]
            connection = sqlite3.connect('Database/sensordata.db')
            cur = connection.cursor()
            cur.execute("DELETE FROM data;")
            cur.execute("INSERT INTO data (s1, s2, s3)VALUES (?, ?, ?);",
                             (data1, data2, data3))
            print(data1, data2, data3)
            connection.commit()


if __name__ == '__main__':
    main()