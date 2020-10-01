import datetime

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

def get_current_time():
    now = datetime.datetime.now(datetime.timezone.utc)
    return now
    
def convert_minutes(now):
    return (now.hour * 60) + now.minute

def convert_day(now):
    return now.weekday()

#Returns time from now till x in format 00:00
def minute_delta(x, now):
    return '{:02d}:{:02d}'.format(*divmod(x-convert_minutes(now), 60))

#Valid boss
def valid_boss(inputstr):
    return inputstr.upper() in ["KZARKA", "KARANDA", "OFFIN", "KUTUM", "NOUVER", "GARMOTH", "QUINT", "MURAKA", "VELL"]

#Returns upcoming boss as string
def next_boss(): 
    now = get_current_time()
    day = convert_day(now)

    for x in schedule[day].keys():
        if(convert_minutes(now) <= x):
            return schedule[day].get(x) 

#Returns string containing time till upcoming boss
def till_next_boss():
    now = get_current_time()
    day = convert_day(now)

    for x in schedule[day].keys():
        if(convert_minutes(now) <= x): 
            return schedule[day].get(x) + " in " + minute_delta(x, now)

#Returns list of times input string boss spawns
def showme(inputstr):
    now = get_current_time()
    day = convert_day(now)

    spawntimes = [spawntime for spawntime, bossname in schedule[day].items() if inputstr in bossname.upper() and spawntime >= convert_minutes(now)]

    print(spawntimes) #TODO: convert to human readable format
    return spawntimes 



#!showme kzarka
#
#kzarka -> KZARKA 
