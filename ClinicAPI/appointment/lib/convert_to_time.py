import datetime


def convert(value):
    total_seconds = (int(value[0]) * 60 * 60) + (int(value[1]) * 60)
    day = total_seconds//86400
    hour = (total_seconds - (day * 86400)) // 3600
    min_val = (total_seconds - ((day * 86400) + (hour * 3600))) // 60
    seconds = total_seconds - ((day * 86400) + (hour * 3600) + (min_val * 60))

    real_time = datetime.time(hour, min_val, seconds)
    return real_time
