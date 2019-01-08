from collections import defaultdict

def shift_by_one(string_to_shift):
  new_string = ''

  for ch in string_to_shift:
    if ch != ' ' :
      if ch is 'z':
        replacement = 'a'
      else:
        replacement = chr(ord(ch) + 1)
    else:
      replacement = " "

    new_string += replacement

  return new_string

rooms = []

total = 0

for line in open('./4.in').read().split('\n'):

  reps = defaultdict(int)

  if line:
    words = line.split('-')

    instructions = ''.join(words[:-1])

    last = words[-1]
    id, checksum = last[:-1].split('[')

    for ch in instructions:
      reps[ch] += 1

    reps = sorted(reps.items(), key = lambda item: (-item[1], item[0]))

    most_common = ''

    for item in reps:
      if len(most_common) is 5:
        break
      most_common += item[0]

    if most_common == checksum:
      total += int(id)
      rooms.append((' '.join(words[:-1]), int(id)))

print('part 1', total)

for room in rooms:
  name, id = room[0], room[1]

  for _ in range(id):
    name = shift_by_one(name)

  if 'orth' in name:
    print('part 2', name, id)