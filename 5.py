import hashlib


def get_password(sequential):
  door_id = 'cxdnnyjw'

  password = ''

  i = 0
  while len(password) != 8:
    hash = hashlib.md5('{}{}'.format(door_id, i).encode('utf-8')).hexdigest()

    if hash.startswith('00000'):
      if sequential:
        password += hash[5]
      else:
        # do it based on position

    i += 1
  return password

print('part 1', get_password(sequential=True))
