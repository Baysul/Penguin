from Penguin.ClubPenguin import ClubPenguin
from Penguin.ClubPenguin import PenguinFactory
from Penguin.Penguin import Penguin

class MyPenguin(Penguin):

	def __init__(self, player):
		super(MyPenguin, self).__init__(player)

		self.addListener("jr", self.handleJoinRoom)

		# Joins room 800 (the dock) at coordinates 223 and 333
		self.addListener("partycookie", lambda x: self.joinRoom(800, 223, 333))

	def handleJoinRoom(self, data):
		self.logger.info("Joined room!")

		self.sendPhraseMessage("hi master")

class MyPenguinFactory(PenguinFactory):

	def __init__(self):
		super(MyPenguinFactory, self).__init__()

		self.logger.debug("MyPenguinFactory constructed")

	def buildProtocol(self, addr):
		player = self.queue.pop()

		penguin = MyPenguin(player)

		return penguin

cp = ClubPenguin()

myPenguinFactory = MyPenguinFactory()

cp.connect(username="Username", password="Password", server="Frostbite", \
	factory=myPenguinFactory)

cp.start()
