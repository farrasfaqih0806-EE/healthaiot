import json
import time

import config

from mqtt.mqtt_client import create_client

if config.SIMULATION:

    from sources.mitbih_source import stream

else:

    from sources.serial_source import stream


client = create_client()

client.connect(

    config.BROKER,

    config.PORT

)

client.loop_start()

client.publish(

    config.TOPIC_STATUS,

    json.dumps({

        "device_id": config.DEVICE_ID,

        "status": "online"

    }),

    qos=1

)

print("Publisher Started")

buffer = []

try:

    for sample in stream():

        buffer.append(float(sample))

        if len(buffer) < config.WINDOW_SIZE:

            continue

        payload = {

            "device_id": config.DEVICE_ID,

            "timestamp": time.time(),

            "sampling_rate": config.SAMPLING_RATE,

            "samples": buffer

        }

        client.publish(

            config.TOPIC_ECG,

            json.dumps(payload),

            qos=1

        )

        print(

            f"Published {len(buffer)} ECG Samples"

        )

        buffer = []

except KeyboardInterrupt:

    print("Publisher Stopped")

finally:

    client.publish(

        config.TOPIC_STATUS,

        json.dumps({

            "device_id": config.DEVICE_ID,

            "status": "offline"

        }),

        qos=1

    )

    client.loop_stop()

    client.disconnect()

    print("Disconnected")