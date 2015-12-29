#!/usr/bin/python
import sys
import zmq

# We wait for 1 subscriber
SUBSCRIBERS_EXPECTED = 1
context = zmq.Context()

# Socket to talk to clients
publisher = context.socket(zmq.PUB)
# set SNDHWM, so we don't drop messages for slow subscribers
publisher.sndhwm = 1100000
publisher.bind('tcp://*:5561')

# Socket to receive signals
syncservice = context.socket(zmq.REP)
syncservice.bind('tcp://*:5562')

# Get synchronization from subscribers
subscribers = 0
while subscribers < SUBSCRIBERS_EXPECTED:
	# wait for synchronization request
	msg = syncservice.recv()
	# send synchronization reply
	syncservice.send(b'')
	subscribers += 1
	print("+1 subscriber (%i/%i)" % (subscribers, SUBSCRIBERS_EXPECTED)) 

class Publisher():
		
	def publisher(self, Forward, Reverse,Left,Right):
		publisher.send(b'%.3f %.3f %.3f %.3f' % (Forward, Reverse,Left,Right),zmq.NOBLOCK)


