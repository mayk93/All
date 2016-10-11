import asyncio


def hello_world(loop, message):
    print(message)
    loop.stop()

loop = asyncio.get_event_loop()

# Schedule a call to hello_world()
loop.call_soon(hello_world, loop, "X")

# Blocking call interrupted by loop.stop()
loop.run_forever()
loop.close()