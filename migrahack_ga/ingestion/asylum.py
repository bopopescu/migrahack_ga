from courts.models import *
import csv
from migrahack_ga.settings import BASE_DIR


### CONFIG START ###
asylum_filename = BASE_DIR + '/data/asylum.csv'
### CONFIG END ###

asylum_file = open(asylum_filename)
asylum_csv  = csv.DictReader(asylum_file)

for row in asylum_csv:
    # first, get or create the court objects
    courts  = Court.objects.filter(
                                   name  = row['Immigration Court'],
                                  )
    if len(list(courts)) == 1:
        print 'got it'
        court = courts[0]
    
    else:
        x = raw_input(row['Immigration Court'])
        if x:
            court = Court.objects.get(id=x)
            print court.name
        else:
            continue
    
    #court.save()
    
    # then save the asylum record referencing the court
    asylum = Asylum.objects.create(
                                   court      = court,
                                   year       = row['Year'],
                                   grants     = row['Grants'].replace(',',''),
                                   denials    = row['Denials'].replace(',',''),
                                   grant_rate = row['Grant Rate'].replace('%','')
                                  )
    asylum.save()



