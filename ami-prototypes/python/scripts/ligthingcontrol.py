# Lighting control example
# The script set the time at night and then monitorices the bodies locations
# and switches on and off the ligths of the rooms
from jsonrpctcp import connect
from jsonrpctcp import logger

import json
import time

#To analyze JSON RPC messages exchange
#import logging
#logger.setLevel(logging.DEBUG)
#logger.addHandler(logging.StreamHandler())

# return the room name whera the character bodyId is located
def getRoom(conn, bodyId):
	result = conn.bodyInfo(bodyId)
	decoded = json.loads(result)
	return str(decoded["result"][0]["room"])

# return if someone is in roomId
def roomEmpty(conn, roomId):
	result = conn.bodyInfo()
	decoded = json.loads(result)
	for body in decoded["result"]:
		if body["room"] == roomId :
			return False
	return True

conn = connect('localhost', 44123)

# UpdateDateTime [hourOfDay] [hourOfDay] [min] [sec] [dayOfMonth] [month] [year]
# Updates the time to 20:00:00, e.i., the scenario is at night, it gets dark
result = conn.UpdateDateTime("20")
print result

# Get information of all bodies in the simulation
decoded = json.loads(conn.bodyInfo())
bodies = decoded["result"]

# Initial rooms where bodies are located
rooms = []
for i in range(len(bodies)):
	print "index: " + str(i)
	room = bodies[i]["room"]
	rooms.append(str(room))

# the lights where bodies are located are switched on
for body in bodies:
	conn.SwitchLight(body["room"], "true")

# For ever, check if the place of a body is changed and 
# lights are switch off and on depending the case
while True:
	for body in bodies:
		id = body["id"]
		index = bodies.index(body)
		nRoom = getRoom(conn, body["id"])
		pRoom = rooms[index]
		if nRoom != "None" and nRoom != pRoom :
			conn.SwitchLight(nRoom, "true")
			print id + ": from " + pRoom + " to " + nRoom
			rooms[index] = nRoom
			if roomEmpty(conn, pRoom) :
				conn.SwitchLight(pRoom, "false")
	time.sleep(1)
