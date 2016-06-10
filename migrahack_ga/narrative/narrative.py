from courts.models import *
import json


def roll_thru_states():
    states = set([x.state for x in Court.objects.all()])
    narratives = {}
    for state1 in states:
        narratives[state1] = {}
        for state2 in states:
            if state1 != state2:
                narrative = write_narrative(state1,state2)
                narratives[state1][state2] = {}
                narratives[state1][state2]['narrative'] = narrative
                narratives[state1][state2]['data'] = {}
    write_out_to_json(narratives)


def write_narrative(state1, state2):
    narrative = ''
    
    state1_asy = combine_asylum_rates(state1)
    state2_asy = combine_asylum_rates(state2)
   
    if state2_asy:
        asy_diff = round(float(state1_asy/state2_asy),2)
    else:
        asy_diff = 0
    asy_quant = "<span class='quant'>" + str(abs(asy_diff) * 100) + "%</span>"
    asy_qual = ' less than ' if state1_asy > state2_asy else ' greater than '

    state1_det = Detainers.objects.filter(state__icontains=state1.lower(),year=2014)[0]
    state2_det = Detainers.objects.filter(state__icontains=state2.lower(),year=2014)[0]
    
    det_diff = state1_det.detainer_count - state2_det.detainer_count
    det_quant = "<span class='quant'>" + str(abs(det_diff)) + "</span>"
    det_qual = ' fewer ' if state1_det < state2_det else ' more '

    asy_nar = 'The rate at which immigration courts in ' + state1.title() + \
            ' grant asylum is ' + asy_quant + asy_qual + state2.title() + '.'

    det_nar = state1.title() + ' detained ' + det_quant + det_qual + ' individuals than ' + state2.title() +  '.'

    narrative = det_nar + ' ' + asy_nar

    payload = {
               'narrative': narrative,
               'data'     : {},
               }
    

    return payload




def write_out_to_json(narratives):
    jnar = json.dumps(narratives)
    outfile = open('narratives.json','w')
    outfile.write(jnar)
    outfile.close()


def combine_asylum_rates(state,year=2015):
    qs = Court.objects.filter(state=state)
    grants = 0
    denied = 0
    for q in qs:
        for asy in q.asylum_set.all():
            if asy.year == year:
                grants += asy.grants
                denied += asy.denials
    if grants + denied:
        return round(grants/float(grants+denied),2)
    else:
        return 0

def compare_asylum_rates():
    pass


def compare_detainers():
    pass



if __name__ == '__main__':
    roll_thru_states()
