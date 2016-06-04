from courts.models import *
import csv
from migrahack_ga.settings import BASE_DIR

### START CONFIG ###
courts_file_name = BASE_DIR + '/data/immigration_courts.csv'
### END CONFIG ###

court_file = open(courts_file_name)
court_csv  = csv.DictReader(court_file)

for line in court_csv:
    court = Court.objects.create(
                                 name = line['Immigration Court'],
                                 location = line['City'],
                                 state = line['State'],
                                )
    court.save()
