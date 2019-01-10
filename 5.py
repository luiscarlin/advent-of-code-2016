'''
password is 8 chars

password = ''
while len(password) != 8:
  poss_pass_char = md5_hash(door_id, int_starting_at_0)

  if hex(poss_pass_char[0:5]) == "00000":
    next_char_in_pass = poss_pass_char[6]
    password += next_char_in_pass
'''

import hashlib

door_id = 'cxdnnyjw'

password = ''

i = 0
while len(password) != 8:
  hash = hashlib.md5('{}{}'.format(door_id, i).encode('utf-8')).hexdigest()

  if hash.startswith('00000'):
    password += hash[5]

  i += 1

print('part 1', password)