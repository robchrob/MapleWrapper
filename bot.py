from maplewrapper import wrapper

with wrapper('Geho', mobs=['Mixed Golem']) as w:
    while True:
        player, stats, mobs = w.observe(verbose=1)
