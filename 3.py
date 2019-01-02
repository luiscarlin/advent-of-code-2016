possible = 0

for line in open('3.in').read().split('\n'):
  if line:
    side1, side2, side3 = list(map(int, line.strip().split()))

    if side1 + side2 <= side3 or side1 + side3 <= side2 or side3 + side2 <= side1:
      continue
    possible += 1

print('part 1', possible)