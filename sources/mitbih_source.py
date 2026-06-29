import wfdb

import config


def stream():

    record = wfdb.rdrecord(

        f"{config.DATASET_PATH}/{config.MITBIH_RECORD}"

    )

    signal = record.p_signal[:, 0]

    print("MIT-BIH Loaded")

    print("Total Samples :", len(signal))

    for sample in signal:

        yield float(sample)