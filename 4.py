from collections import defaultdict

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

print('part 1', total)