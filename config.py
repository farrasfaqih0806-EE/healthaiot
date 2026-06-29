# ==========================================
# MQTT
# ==========================================

BROKER = "dc9a3b7715844cab948560ca9187d5d0.s1.eu.hivemq.cloud"

PORT = 8883

USERNAME = "rekayasasisteminternet"

PASSWORD = "Rekayasasisteminternet11"

TOPIC_ECG = "healthaiot/ecg/window"

TOPIC_STATUS = "healthaiot/device/status"

DEVICE_ID = "RPI3-001"

# ==========================================
# ECG
# ==========================================

SAMPLING_RATE = 250

WINDOW_SIZE = 250

# ==========================================
# SOURCE
# ==========================================

SIMULATION = False

# ==========================================
# SERIAL
# ==========================================

SERIAL_PORT = "/dev/ttyACM0"

SERIAL_BAUDRATE = 115200

# ==========================================
# MIT-BIH
# ==========================================

DATASET_PATH = "dataset"

MITBIH_RECORD = 100