from datetime import datetime

def elapsed_time(time1, time2):
    t1 = datetime.strptime(time1, "%H:%M:%S")
    t2 = datetime.strptime(time2, "%H:%M:%S")

    time_delta = t2 - t1

    total_seconds = round(time_delta.total_seconds())

    hours = total_seconds // 3600
    minutes = (total_seconds % 3600) // 60
    seconds = total_seconds % 60

    if hours < 0:
        hours += 24
    
    return ("%02d" % hours) + ":" + ("%02d" % minutes) + ":" + ("%02d" % seconds)


print(elapsed_time("11:00:00", "12:00:00"))
print(elapsed_time("13:01:43", "21:41:57"))
print(elapsed_time("17:34:43", "17:34:42"))
