import asyncio

x=2
def hello_world(loop):
    print('Hello World')
    #loop.stop()
    print(x)

def hello_irwan(loop):
    print('Irwan')
    #loop.stop()
	 

loop = asyncio.get_event_loop()

# Schedule a call to hello_world()
loop.call_soon(hello_world, loop)
loop.call_soon(hello_irwan, loop)

# Blocking call interrupted by loop.stop()
loop.run_forever()
#loop.close()
