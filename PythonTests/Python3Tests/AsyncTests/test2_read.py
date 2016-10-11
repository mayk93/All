# import asyncio
# try:
#     from socket import socketpair
# except ImportError:
#     from asyncio.windows_utils import socketpair
#
# # Create a pair of connected file descriptors
# rsock, wsock = socketpair()
# loop = asyncio.get_event_loop()
#
# def reader():
#     data = rsock.recv(100)
#     print("Received:", data.decode())
#     # We are done: unregister the file descriptor
#     loop.remove_reader(rsock)
#     # Stop the event loop
#     loop.stop()
#
# # Register the file descriptor for read event
# loop.add_reader(rsock, reader)
#
# # Simulate the reception of data from the network
# loop.call_soon(wsock.send, 'abc'.encode())
#
# # Run the event loop
# loop.run_forever()
#
# # We are done, close sockets and the event loop
# rsock.close()
# wsock.close()
# loop.close()

# -----

import os
import fcntl
import asyncio

print("Starting")

receive_pipe_name = "communication_pipe"
receive_pipe = open(receive_pipe_name, "r")
receive_pipe_no = receive_pipe.fileno()
fcntl.fcntl(receive_pipe_no, fcntl.F_SETFL, os.O_RDONLY | os.O_NONBLOCK)

print("Pipe setup")

def read():
    data = ""
    try:
        while True:
            read_input = receive_pipe.read(1)
            # if len(read_input) > 0:
            #     print("Received some input: ", str(read_input))
            if read_input == "\n":
                break
            data += read_input
    except IOError:
        pass
    except Exception as e:
        print(e)

    print("Received data: ", str(data))
    loop.stop()


loop = asyncio.get_event_loop()
loop.add_reader(receive_pipe, read())

loop.run_forever()
loop.close()