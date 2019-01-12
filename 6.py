from collections import defaultdict


def find_message(using_max):
  lines = []

  for line in open('6.in').read().split('\n'):
    if line:
      lines.append(line)

  message = ''

  for idx in range(8):
    totals_col = defaultdict(int)

    for line in lines:
      totals_col[line[idx]] += 1

    if using_max:
      char = max(totals_col, key=totals_col.get)
    else:
      char = min(totals_col, key=totals_col.get)
    message += char

  return message

print('part 1', find_message(using_max=True))
print('part 2', find_message(using_max=False))