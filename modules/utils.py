from datetime import datetime


def get_timestamp():
    return datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f")


def timestamp_filename(filename):
    timestamp = get_timestamp()
    return "_".join([timestamp, filename])
