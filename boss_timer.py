import datetime

schedule = [
    {0:"Karanda", 180:"Kzarka", 420:"Kzarka", 600:"Offin", 840:"Kutum", 1020:"Nouver", 1215:"Kzarka", 1275:"NONE", 1335:"Karanda"},
    {0:"Kutum", 180:"Kzarka", 420:"Nouver", 600:"Kutum", 840:"Nouver", 1020:"Karanda", 1215:"Garmoth", 1275:"NONE", 1335:"Kzarka/Kutum"},
    {0:"Karanda", 180:"NONE", 420:"Karanda", 600:"Nouver", 840:"Kutum/Offin", 1020:"Vell", 1215:"Karanda/Kzarka", 1275:"Quint/Muraka", 1335:"Nouver"},
    {0:"Kutum", 180:"Kzarka", 420:"Kutum", 600:"Nouver", 840:"Kzarka", 1020:"Kutum", 1215:"Garmoth", 1275:"NONE", 1335:"Karanda/Kzarka"},
    {0:"Nouver", 180:"Karanda", 420:"Kutum", 600:"Karanda", 840:"Nouver", 1020:"Kzarka", 1215:"Kzarka/Kutum", 1275:"NONE", 1335:"Karanda"},
    {0:"Offin", 180:"Nouver", 420:"Kutum", 600:"Nouver", 840:"Quint/Muraka", 1020:"Karanda/Kzarka", 1215:"NONE", 1275:"NONE", 1335:"Nouver/Kutum"},
    {0:"Kzarka", 180:"Kutum", 420:"Nouver", 600:"Kzarka", 840:"Vell", 1020:"Garmoth", 1215:"Kzarka/Nouver", 1275:"NONE", 1335:"Karanda/Kutum"}
]

def btimer():
    now = datetime.datetime.now()
    day = datetime.datetime.today().weekday()

    for x in schedule[day].key():
        if(now.minute <= x):
            return schedule[day][x]