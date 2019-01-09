'''
password is 8 chars

password = ''
while len(password) != 8:
  poss_pass_char = md5_hash(door_id, int_starting_at_0)

  if hex(poss_pass_char[0:5]) == "00000":
    next_char_in_pass = poss_pass_char[6]
    password += next_char_in_pass
'''


door_id = 'cxdnnyjw'

print(door_id)
