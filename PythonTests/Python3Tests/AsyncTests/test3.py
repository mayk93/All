# import asyncio
#
# async def hello_world():
#     print("Hello World!")
#
# loop = asyncio.get_event_loop()
# # Blocking call which returns when the hello_world() coroutine is done
# loop.run_until_complete(hello_world())
# loop.close()

import time
import asyncio
import random

async def cor():
    time.sleep(5)
    return random.choice([0, 1]) == 0

async def hello_world():
    time.sleep(1)
    print("Partially complete")
    if await cor():
        print("True case")
    else:
        print("False case")
    time.sleep(1)
    print("Done")


loop = asyncio.get_event_loop()
# Blocking call which returns when the hello_world() coroutine is done
loop.run_until_complete(hello_world())
loop.close()