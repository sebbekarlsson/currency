convert = lambda string, unit: unit + '.'.join(''.join(c for c in p if c.isdigit()) for i, p in enumerate(string.split('.')) if i < 2)
