from random import choice
from time import sleep
from server_actions import *
from support import *


# Setup in case Treasure Hunt Section is skipped
data = get_init()
map = file_to_json('full_map.txt')
sleep(1)

# Treasure Hunt
while get_status()['gold'] < 1000:
    data = treasure_hunt()
    data = move_to_location(data['room_id'], KEY_ROOMS['Shop'], data, map)
    data = shop_check(data)
print('Treasure Hunt Complete')

# Name Change
data = move_to_location(data['room_id'], KEY_ROOMS["Pirate Ry's"], data, map)
# data = change_name('<YOUR NAME HERE>')  # Parameter should be your name in quotes
print('Name Change Complete')

# Finding Mine Location
data = move_to_location(data['room_id'], KEY_ROOMS['Wishing Well'], data, map)
get_binary_from_well()
message = translate_binary('binary.txt')
print(message)

# Mining - Incomplete
mine_location = int(message[-3:])
data = move_to_location(data['room_id'], mine_location, data, map)
data = get_last_proof()
print('\nMining To Do List')
print('------------------------')
print('Bring in Blockchain File from SC')
print('Modify Blockchain File for Project - Maybe?')
print('Wrap Mining Loop in Function')
print('Be done with this project')