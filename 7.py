def support_tls():
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
          if level is not 0:
            support_tls = False
            break
          contains_ip = True

      if contains_ip and support_tls:
        num_ips += 1
  return num_ips

def support_ssl():
  num_ips = 0

  for line in open('7.in').read().split('\n'):
    if line:
      level = 0

      in_brackets = ''

      pattern_to_search = []

      for idx, char in enumerate(line):
        if char is '[':
          level += 1
        if char is ']':
          level -= 1

        if char in '[]':
          continue

        if level is not 0:
          in_brackets += char
          continue

        if idx + 2 == len(line):
          break

        if line[idx] is line[idx + 2] and line[idx] is not line[idx + 1]:
          pattern_to_search.append(line[idx + 1] + line[idx] + line[idx + 1])

      for pattern in pattern_to_search:
        if in_brackets.find(pattern) is not -1:
          num_ips += 1
          break
  return num_ips

print('part 1', support_tls())
print('part 2', support_ssl())
