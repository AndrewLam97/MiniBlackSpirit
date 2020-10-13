import datetime
import pytz

#list of dictionaries
schedule = [
    {0:"Garmoth", 195:"Kzarka/Nouver", 255:"NONE", 315:"Karanda/Kutum", 420:"Karanda", 600:"Kzarka", 840:"Kzarka", 1020:"Offin", 1260:"Kutum"},
    {0:"Nouver", 195:"Kzarka", 255:"NONE", 315:"Karanda", 420:"Kutum", 600:"Kzarka", 840:"Nouver", 1020:"Kutum", 1260:"Nouver"},
    {0:"Karanda", 195:"Garmoth", 255:"NONE", 315:"Kzarka/Kutum", 420:"Karanda", 600:"NONE", 840:"Karanda", 1020:"Nouver", 1260:"Kutum/Offin"},
    {0:"Vell", 195:"Karanda/Kzarka", 255:"Quint/Muraka", 315:"Nouver", 420:"Kutum", 600:"Kzarka", 840:"Kutum", 1020:"Nouver", 1260:"Kzarka"},
    {0:"Kutum", 195:"Garmoth", 255:"NONE", 315:"Karanda/Kzarka", 420:"Nouver", 600:"Karanda", 840:"Kutum", 1020:"Karanda", 1260:"Nouver"},
    {0:"Kzarka", 195:"Kzarka/Kutum", 255:"NONE", 315:"Karanda", 420:"Offin", 600:"Nouver", 840:"Kutum", 1020:"Nouver", 1260:"Quint/Muraka"},
    {0:"Karanda/Kzarka", 195:"NONE", 255:"NONE", 315:"Nouver/Kutum", 420:"Kzarka", 600:"Kutum", 840:"Nouver", 1020:"Kzarka", 1260:"Vell"}
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

    if(convert_minutes(now) > 1260):
        now.day += 1
        if(day > 6):
            day = 0
        now.hour -= 21
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
    day = convert_day(now)

    if(convert_minutes(now) > 1260):
        nextday = now - datetime.timedelta(seconds = 63000)
        day = day + 1
        if(day > 6):
            day = 0
        for x in schedule[day].keys():
            if(convert_minutes(nextday) <= x):
                return schedule[day].get(x) + " in " + minute_delta(x, now)

    else:
        for x in schedule[day].keys():
            if(convert_minutes(now) <= x):
                return schedule[day].get(x) + " in " + minute_delta(x, now) 

    # for x in schedule[day].keys():
    #     if(convert_minutes(now) <= x): 
    #         return schedule[day].get(x) + " in " + minute_delta(x, now)

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
    if is_dst("America/Los_Angeles"):
        now = spawntime - 420
    else:
        now = spawntime - 480
    if spawntime >= 1860:
        now = now % 1440
    if spawntime < 0:
        return("You can't travel back in time!")
    PST = now + 720
    PST_hour = PST // 60
    PST_min = str(PST % 60).zfill(2)
    if PST > 720 and PST <= 1440:
        PST_hour -= 12
    if PST >= 720 and PST < 1440:
        return "{}:{}AM".format(PST_hour, PST_min)
    else:
        if PST > 1440:
            PST_hour -= 24
        return "{}:{}PM".format(PST_hour, PST_min)