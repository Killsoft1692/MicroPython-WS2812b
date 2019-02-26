import uasyncio


def init_val():
    return ('r', (0, 7)), ('g', (7, 13)), ('b', (13, 20))


async def light(c='r', pos=(0, 7), br=40):
    sch = (br, 0, 0) if c == 'r' else (0, br, 0) if c == 'g' else (0, 0, br)
    while True:
        for i in range(*pos):
            await uasyncio.sleep(0.2)
            if i > pos[0]:
                np[i-1] = (0, 0, 0)
            else:
                np[pos[1]-1] = (0, 0, 0)
                np[i] = sch
                np.write()

loop = uasyncio.get_event_loop()
for c in init_val():
    loop.create_task(light(br=5, c=c[0], pos = c[1]))
loop.run_forever()
