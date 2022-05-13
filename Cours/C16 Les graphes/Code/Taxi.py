import gym
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sys
import time
from pynput import keyboard
import json
    
skip=False
def on_press(key):
    global skip
    try:
        if key.char == 's':
            print('Skipping')
            skip=True
    except AttributeError:
        print('Press s to skip')
    
np.set_printoptions(threshold=sys.maxsize)
np.set_printoptions(precision=4)

from IPython.display import clear_output

env = gym.make('Taxi-v3')

#################################################################################################################

print('row', 'col', 'pass_idx', 'dest_idx')
dico_actions={0: 'move south', 1: 'move north', 2: 'move east', 3: 'move west', 4: 'pickup passenger', 5: 'drop off passenger'}
dico_passenger={0: 'R(ed)', 1: 'G(reen)', 2: 'Y(ellow)', 3: 'B(lue)', 4: 'in taxi'}
dico_destinations={0: 'R(ed)', 1: 'G(reen)', 2: 'Y(ellow)', 3: 'B(lue)'}

print('Actions',dico_actions)
print('Passenger_loc',dico_passenger)
print('Destinations',dico_destinations)

dict_states={}
i=0
num_rows = 5
num_columns = 5
locs = [(0, 0), (0, 4), (4, 0), (4, 3)]
for row in range(num_rows):
    for col in range(num_columns):
        for pass_idx in range(len(locs) + 1):  # +1 for being inside taxi
            for dest_idx in range(len(locs)):
                dict_states[str(i)]={'0':row, '1':col, '2':pass_idx, '3':dest_idx}
                i+=1

dict_states_evol={}
for i in env.P.keys():
    dico={}
    for j in env.P[i].keys():
        dico[j]=env.P[i][j][0][1]
    dict_states_evol[i]=dico

for dic_name, dic_file in [[dict_states,'dico_states.json'],[dict_states_evol,'dico_states_evol.json'],[dico_actions,'dico_actions.json'],[dico_passenger,'dico_passenger.json'],[dico_destinations,'dico_destinations.json']]:
    with open(dic_file, 'w') as jsonfile:
        json.dump(dic_name, jsonfile)


def decode_state(i):
    out = []
    out.append(i % 4)
    i = i // 4
    out.append(i % 5)
    i = i // 5
    out.append(i % 5)
    i = i // 5
    out.append(i)
    assert 0 <= i < 5
    return reversed(out)

#################################################################################################################

action_space_size = env.action_space.n
obs_space_size = env.observation_space.n

q_table = np.zeros((obs_space_size, action_space_size))

games_to_play = 10000

learning_rate = 0.1
discount_rate = 0.6

exploration_rate = 1
max_exploration_rate = 1
min_exploration_rate = 0.01
exploration_rate_decay = 0.0005

rewards = []
exploration_rates = []

for episode in range(games_to_play):
    state = env.reset()
    temp_reward = 0
    
    exploration_rates.append(exploration_rate)
    
    while True:
        thresh = np.random.uniform(0, 1)
        if thresh > exploration_rate:
            action = np.argmax(q_table[state, :])
        else:
            action = env.action_space.sample()

#        print(state,env.P[state])        
        new_state, reward, done, info = env.step(action)
        q_table[state, action] = q_table[state, action] * (1 - learning_rate) + learning_rate * (reward + discount_rate * np.max(q_table[new_state, :]))
        
        state = new_state
        temp_reward += reward
        
        if done:
            break
            
    exploration_rate = min_exploration_rate + (max_exploration_rate - min_exploration_rate) * np.exp(- exploration_rate_decay * episode)
    
    rewards.append(temp_reward)

dico_q_table={}
leni,lenj=np.shape(q_table)
for i in range(leni):
    dico_q_table[str(i)]={}
    for j in range(lenj):
        dico_q_table[str(i)][str(j)]=q_table[i, j]
        

for dic_name, dic_file in [[dico_q_table,'dico_q_table.json']]:
    with open(dic_file, 'w') as jsonfile:
        json.dump(dic_name, jsonfile)

rewards_per_thousand_episodes = np.split(np.array(rewards), games_to_play / 1000)
count = 1000

# print('******Average reward per thousand episodes******\n')
# for r in rewards_per_thousand_episodes:
#     print(f'{count}: {sum(r/1000)}')
#     count += 1000
    
plt.figure(figsize = (18, 6))

plt.subplot(121)
plt.scatter(range(games_to_play), rewards)
plt.title('Rewards')
plt.grid()

plt.subplot(122)
plt.plot(range(games_to_play), exploration_rates)
plt.title('Exploration rate')
plt.grid()

plt.show()

listener = keyboard.Listener(
    on_press=on_press)
listener.start()

for i in range(10):
    total_reward = 0
    state=env.reset()
    start=list(env.decode(state))[2]
    end=list(env.decode(state))[3]
    points=['R','G','Y','B']
    
    while True:
        clear_output(wait = True)
        print(f'Episode {i+1}: {points[start]} -> {points[end]}')
        
        env.render()
        action = np.argmax(q_table[state])
        state, reward, done, debug = env.step(action)
        total_reward += reward
        print(f'Step reward: {reward}')
        print(f'Total reward: {total_reward}')
        
        time.sleep(0.5)
        
    
        if done or skip:
            print('Episode done')
            time.sleep(2)
            skip=False
            break

