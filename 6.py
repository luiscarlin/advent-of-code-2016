from collections import defaultdict

lines = []

for line in open('6.in').read().split('\n'):
  if line:
    lines.append(line)

message = ''

for idx in range(8):
  totals_col = defaultdict(int)

  for line in lines:
    totals_col[line[idx]] += 1

  char = max(totals_col, key=totals_col.get)
  message += char

print('part 1', message)