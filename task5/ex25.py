seconds_per_day = 86400
seconds_per_hour = 3600
seconds_per_minute = 60

second = int(input())

day = int(second / seconds_per_day)
hour = int(second/ seconds_per_hour)%24
minute = int(second / seconds_per_minute)%60
second %= 60

print("D:", day, "H:", hour, "M:", minute, "S:", second)