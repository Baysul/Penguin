from Penguin.ClubPenguin import ClubPenguin
from Example.MyPenguinFactory import MyPenguinFactory

cp = ClubPenguin()

myPenguinFactory = MyPenguinFactory()

cp.connect(username="Username", password="Password", server="Frostbite", \
	factory=myPenguinFactory)

cp.start()
