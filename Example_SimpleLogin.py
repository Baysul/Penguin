from Penguin.ClubPenguin import ClubPenguin

cp = ClubPenguin()

cp.connect(username="Username", password="Password", server="Blizzard")

"""
!! Note - not yet (fully) implemented !!
The following lines of code demonstrate how you can specify custom
classes for the login procedures of both the initial-log-in and
game servers.

By specifying your own classes, which are derived from Chinstrap
and Penguin respecitvely, you gain more control over how packets are
handled. Although, the listener system job (should) generally does a
good job at helping users achieve this, users may for whatever reason
want to get rid of the listener system altogether.

By initial log-in server, I'm referring to the server which supplies
the login keys.

They also demonstate usage of the options that are available when
adding a penguin to the Club Penguin instance.

def myHeartbeatHandler(bot, data):
	.. etc

cp.connect(
	username="Username2", password="Password1", server="Frozen", \
	module="Examples", "class"="FollowBot", \
	heartbeat="On", heartbeatHandler="myHeartbeatHandler"
)
"""

cp.start()
