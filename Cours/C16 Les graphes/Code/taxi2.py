import json

# Opening JSON files
with open('dico_states.json') as json_file:
    states = json.load(json_file)

with open('dico_states_evol.json') as json_file:
    states_evol = json.load(json_file)

with open('dico_actions.json') as json_file:
    actions = json.load(json_file)

with open('dico_destinations.json') as json_file:
    destinations = json.load(json_file)

with open('dico_passenger.json') as json_file:
    passenger = json.load(json_file)

with open('dico_q_table.json') as json_file:
    q_table = json.load(json_file)

print('row', 'col', 'pass_idx', 'dest_idx')
print(actions)
print(destinations)
print(passenger)
print('\n')


print('228',states['228'],states_evol['228'])
print(q_table['228'])
print('208',states['208'],states_evol['208'])
print(q_table['208'])
print('308',states['308'],states_evol['308'])

