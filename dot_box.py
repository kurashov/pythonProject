def parse_coordinates(line):
    return (float(x) for x in line.split(','))


x, y, z = parse_coordinates(input())
min_coordinates = max_coordinates = (x, y, z)
line = input()
while len(line) != 0:
    x, y,z = parse_coordinates(line)
    min_coordinates = (min(min_coordinates[0], x), min(min_coordinates[1], y), min(min_coordinates[2], z))
    max_coordinates = (max(max_coordinates[0], x), max(max_coordinates[1], y), max(max_coordinates[2], z))
    line = input()
v = (max_coordinates[0] - min_coordinates[0]) \
    * (max_coordinates[1] - min_coordinates[1]) \
    * (max_coordinates[2] - min_coordinates[2])
print(v)
