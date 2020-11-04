import datetime
import pytz

#list of dictionaries
schedule = [
    {60:"Garmoth", 255:"Kzarka/Nouver", 315:"NONE", 375:"Karanda/Kutum", 480:"Karanda", 660:"Kzarka", 900:"Kzarka", 1080:"Offin", 1320:"Kutum"},
    {60:"Nouver", 255:"Kzarka", 315:"NONE", 375:"Karanda", 480:"Kutum", 660:"Kzarka", 900:"Nouver", 1080:"Kutum", 1320:"Nouver"},
    {60:"Karanda", 255:"Garmoth", 315:"NONE", 375:"Kzarka/Kutum", 480:"Karanda", 660:"NONE", 900:"Karanda", 1080:"Nouver", 1320:"Kutum/Offin"},
    {60:"Vell", 255:"Karanda/Kzarka", 315:"Quint/Muraka", 315:"Nouver", 480:"Kutum", 660:"Kzarka", 900:"Kutum", 1080:"Nouver", 1320:"Kzarka"},
    {60:"Kutum", 255:"Garmoth", 315:"NONE", 375:"Karanda/Kzarka", 480:"Nouver", 660:"Karanda", 900:"Kutum", 1080:"Karanda", 1320:"Nouver"},
    {60:"Kzarka", 255:"Kzarka/Kutum", 315:"NONE", 375:"Karanda", 480:"Offin", 660:"Nouver", 900:"Kutum", 1080:"Nouver", 1320:"Quint/Muraka"},
    {60:"Karanda/Kzarka", 255:"NONE", 315:"NONE", 375:"Nouver/Kutum", 480:"Kzarka", 660:"Kutum", 900:"Nouver", 1080:"Kzarka", 1320:"Vell"}
]

#get and refresh datetime object
def get_current_time():
    now = datetime.datetime.now(datetime.timezone.utc)
    return now

#converts current datetime object to minutes
def convert_minutes(now):
    return (now.hour * 60) + now.minute

#get weekday integer from datetime object
def convert_day(now):
    return now.weekday()

#Returns time from now till x in format 00:00
def minute_delta(x, now):
    return '{:02d}h : {:02d}m'.format(*divmod(x-convert_minutes(now), 60))

#Valid boss string
def valid_boss(inputstr):
    return inputstr.upper() in ["KZARKA", "KARANDA", "OFFIN", "KUTUM", "NOUVER", "GARMOTH", "QUINT", "MURAKA", "VELL"]

#Returns upcoming boss as string
def next_boss(): 
    now = get_current_time()
    day = convert_day(now)

    if(convert_minutes(now) > 1320):
        now.day += 1
        if(day > 6):
            day = 0
        now.hour -= 22
        for x in schedule[day].keys():
            if(convert_minutes(now) <= x):
                return schedule[day].get(x)

    else:
        for x in schedule[day].keys():
            if(convert_minutes(now) <= x):
                return schedule[day].get(x) 

#Returns string containing time till upcoming boss
def till_next_boss():
    now = get_current_time()

    weekday = convert_day(now)

    if(convert_minutes(now) > 1320):
        weekday = weekday + 1
        if(weekday > 6):
            weekday = 0

        next_spawn = get_current_time() #create datetime object
        next_spawn = next_spawn + datetime.timedelta(days = 1) #increment to next day
        next_list = list(schedule[0].keys()) #create list containing all available spawn times
        next_hour = 0
        if(next_list[0]>=60): #if first spawn time for the day is greater than 1 hour, replace doesn't handle greater than 59 minutes
            next_hour += next_list[0] // 60
        next_minute = next_list[0] % 60
        
        next_spawn = next_spawn.replace(hour = next_hour, minute = next_minute) #datetime object containing next day's first spawn
        
        tdseconds = next_spawn - now #timedelta object containing difference between tomorrow's first spawn and now

        tdminutes = tdseconds.total_seconds() // 60

        return schedule[weekday][next_list[0]] + " in " + '{:02d}h : {:02d}m'.format(*divmod(int(tdminutes), 60)) #get tomorrow's dictionary's first value

    else:
        for x in schedule[weekday].keys():
            if(convert_minutes(now) <= x):
                return schedule[weekday].get(x) + " in " + minute_delta(x, now) 

#Returns list of times input string boss spawns
def showme(inputstr):
    now = get_current_time()
    day = convert_day(now)
    spawntimes=[]

    for spawntime in schedule[day]:
        if inputstr in schedule[day][spawntime].upper() and spawntime >= convert_minutes(now):
            spawntimes.append(spawntime)
    nextday = day + 1
    if(nextday > 6):
        nextday = 0
    for spawntime in schedule[nextday]:
        if inputstr in schedule[nextday][spawntime].upper() and spawntime < convert_minutes(now):
            spawntimes.append(spawntime)

    strspawntimes = ""
    for x in spawntimes:
        strspawntimes = strspawntimes + convert_read(x) + " "

    return strspawntimes

#Check if it is daylight savings time 
def is_dst(zonename):
    tz = pytz.timezone(zonename)
    now = pytz.utc.localize(datetime.datetime.utcnow())
    return now.astimezone(tz).dst() != datetime.timedelta(0)

#Converts to human readable format
def convert_read(spawntime):
    if spawntime < 0:
        return("You can't travel back in time!")

    #check if DST and convert UTC minutes to PTC minutes
    if is_dst("America/Los_Angeles"):
        now = spawntime - 420
    else:
        now = spawntime - 480

    #prevent negative PST time by adding another 24 hours
    if now < 0:
        now = now + 1440

    now = now % 1440
    PST_hour = now // 60
    PST_min = str(now % 60).zfill(2)
    if now < 720:
        if now == 0:
            PST_hour = 12
        return "{}:{}AM".format(PST_hour, PST_min)
    else:
        if now > 720:
            PST_hour -= 12
        return "{}:{}PM".format(PST_hour, PST_min)

#Prints out upcoming bosses for next 24 hours
def print_schedule():
    now = get_current_time()
    day = convert_day(now)

    day_schedule = []

    #Grab entries from the dictionary that are within 24 hours of current time
    for x in schedule[day].keys():
        if(x >= convert_minutes(now)):
            pair = (x, schedule[day].get(x))
            day_schedule.append(pair)
    day += 1
    if(day > 6):
        day = 0
    for x in schedule[day].keys():
        if(x <= convert_minutes(now)):
            pair = (x, schedule[day].get(x))
            day_schedule.append(pair)

    strschedule = ""

    #Create schedule string and adds each time and boss in order
    for a, b in day_schedule:
        strschedule += '{} {}\n'.format(convert_read(a), b)

    return strschedule    