seconds_per_day = 86400
seconds_per_hour = 3600
seconds_per_minute = 60

day = int(input())
hour = int(input())
minute = int(input())
second = int(input())

tot_sec = day * seconds_per_day
tot_sec = tot_sec + hour * seconds_per_hour
tot_sec = tot_sec + minute * seconds_per_minute
tot_sec += second

print("Total second is", tot_sec)