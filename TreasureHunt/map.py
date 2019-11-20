from random import choice
from time import sleep
from server_actions import *
from support import *

reverse = {'n':'s', 'e':'w', 's':'n', 'w':'e'}
backtrack = []
rooms_visited = 1
data = get_init()
rooms = make_blank_map()
sleep(data['cooldown'])

while rooms_visited < 500:
  current_room_id = data['room_id']
  exits = data['exits']
  valid_moves = find_unvisited_directions(exits, rooms[current_room_id])

  if valid_moves != []:
    move = choice(valid_moves)
    data = make_move({'direction': move})
    backtrack.append(reverse[move])
    rooms[current_room_id][move] = data['room_id']
    rooms[data['room_id']][reverse[move]] = current_room_id
    rooms_visited += 1
    print(rooms_visited)
  else:
    data = make_move({'direction':backtrack.pop(-1)})
  sleep(data['cooldown'])

json_to_file(rooms, 'map.txt')