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