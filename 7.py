num_ips = 0

for line in open('7.in').read().split('\n'):
  if line:
    level = 0
    support_tls = True
    contains_ip = False

    for idx, char in enumerate(line):
      if char is '[':
        level += 1
      if char is ']':
        level -= 1

      if idx + 3 == len(line):
        break

      if line[idx] is line[idx + 3] and line[idx  + 1] is line[idx + 2] and line[idx] is not line[idx + 1]:
        # found pattern
        if level is not 0:
          support_tls = False
          break
        contains_ip = True

    if contains_ip and support_tls:
      num_ips += 1

print('part 1', num_ips)
