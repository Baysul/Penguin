""" Credits
Zephyr (https://github.com/Zephyr-Vi) for the interval formula
"""

from math import ceil
from twisted.internet import reactor

from Penguin.ClubPenguin import ClubPenguin
from Penguin.ClubPenguin import PenguinFactory
from Penguin.Penguin import Penguin

class CoinPenguin(Penguin):

	def __init__(self, player, coins, loops):
		super(CoinPenguin, self).__init__(player)

		self.coins = coins
		self.loops = loops
		self.looped = 0

		# Amount of time to wait (in seconds) to send the zo packet
		self.interval = ceil(float(coins) / 30)

		self.addListener("jr", self.handleJoinRoom)
		self.addListener("jg", self.handleJoinGame)
		self.addListener("lp", self.handleLoadPlayer)
		self.addListener("zo", self.handleGameOver)

	def handleGameOver(self, data):
		playerCoins = int(data[3]) # New amount of coins

		self.logger.info("You've earned {0} coins!".format(playerCoins - self.playerCoins))

		self.playerCoins = playerCoins

		if self.looped == self.loops and self.loops > 0:
			self.logger.info("Done adding coins. You now have {0} coins.".format(playerCoins))

		else:
			if self.loops > 0:
				self.looped += 1
				self.logger.info("{0} loops left".format(self.loops - self.looped))

			self.joinRoom(810)

	def handleLoadPlayer(self, data):
		self.playerCoins = int(data[4]) # Initial amount of coins

		self.logger.info("You currently have {0} coins".format(self.playerCoins))

	def handleJoinGame(self, data):
		self.logger.info("Joined catchin' waves")

		reactor.callLater(self.interval, self.sendGameOver, self.coins)

	def handleJoinRoom(self, data):
		self.logger.info("Joined room!")

		self.logger.info("Receiving coins in {0} seconds".format(self.interval))

		# Join catchin' waves
		self.joinRoom(912)

class CoinFactory(PenguinFactory):

	def __init__(self, **kw):
		super(CoinFactory, self).__init__()

		self.coins = int(kw["coins"])
		self.loops = int(kw["loops"]) if "loops" in kw else 0

		self.logger.debug("CoinFactory constructed")

	def buildProtocol(self, addr):
		player = self.queue.pop()

		penguin = CoinPenguin(player, self.coins, self.loops)

		return penguin

cp = ClubPenguin()

# Loops keyword is optional
coinFactory = CoinFactory(coins=1000)

cp.connect(username="Username", password="Password", server="Frostbite", \
	factory=coinFactory)

cp.start()
