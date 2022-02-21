3
inp = "target area: x=175..227, y=-134..-79"
x_min, x_max = [int(x) for x in inp.split(', ')[0].split('=')[1].split('..')]
y_min, y_max = [int(x) for x in inp.split(', ')[1].split('=')[1].split('..')]

vx, vy, n = 0, 0, 0
run = 400
starting_velocities = []
for vx in range(1, run):
    vx_start = vx
    for vy in range(-run, run):
        vy_start = vy
        k = vx
        l = vy
        x, y = 0, 0
        for n in range(1, run):
            x += k
            k = k-1 if k > 0 else k+1 if k < 0 else k
            y += l
            l = l-1
            if x_min <= x <= x_max and y_min <= y <= y_max:
                starting_velocities.append((vx_start, vy_start))

ans = 0
for velocity in starting_velocities:
    vx, vy = velocity
    k = vy
    x, y = 0, 0
    while k > 0:
        y = y+k
        k = k-1
        ans = max(ans, y)

print('Part 1:', ans)
print('Part 2:', len(set(starting_velocities)))
