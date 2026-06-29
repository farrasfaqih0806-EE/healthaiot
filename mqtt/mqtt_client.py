import ssl
import paho.mqtt.client as mqtt
import config


def create_client():
    client = mqtt.Client()

    client.username_pw_set(
        config.USERNAME,
        config.PASSWORD
    )

    client.tls_set(
        cert_reqs=ssl.CERT_REQUIRED
    )

    return client


if __name__ == "__main__":
    client = create_client()

    def on_connect(client, userdata, flags, rc):
        print("Connected with code:", rc)
        client.subscribe(config.TOPIC_ECG)
        client.subscribe(config.TOPIC_STATUS)

    def on_message(client, userdata, msg):
        print(msg.topic, msg.payload.decode())

    client.on_connect = on_connect
    client.on_message = on_message

    client.connect(config.BROKER, config.PORT, 60)

    print("MQTT starting loop...")
    client.loop_forever()