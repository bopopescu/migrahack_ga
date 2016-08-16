from courts.models import *
import csv
from migrahack_ga.settings import BASE_DIR


### CONFIG START ###
detainers_filename = BASE_DIR + '/data/detainers_by_state.csv'
### CONFIG END ###

detainers_file = open(detainers_filename)
detainers_csv  = csv.DictReader(detainers_file)

for row in detainers_csv:
    detainer = Detainers.objects.create(
                                        state = row['state'],
                                        year  = row['y'],
                                        detainer_count = row['c'],
                                  )
    detainer.save()



