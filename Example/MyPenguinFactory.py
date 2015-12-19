from Penguin.ClubPenguin import PenguinFactory
from MyPenguin import MyPenguin

class MyPenguinFactory(PenguinFactory):

	def __init__(self):
		super(MyPenguinFactory, self).__init__()

		self.logger.debug("MyPenguinFactory constructed")

	def buildProtocol(self, addr):
		player = self.queue.pop()

		penguin = MyPenguin(player)

		return penguin