import hashlib


def get_password(sequential):
  door_id = 'cxdnnyjw'

  password = [-1] * 8

  i = 0
  while -1 in password:
    hash = hashlib.md5('{}{}'.format(door_id, i).encode('utf-8')).hexdigest()

    if hash.startswith('00000'):
      if sequential:
        index = password.index(-1)
        password[index] = hash[5]
      else:
        position = hash[5]
        char = hash[6]

        if str.isdigit(position):
          position = int(position)

          if position in range(0, 8) and password[position] is -1:
            password[position] = char

    i += 1
  return ''.join(password)

print('part 1', get_password(sequential=True))
print('part 2', get_password(sequential=False))
