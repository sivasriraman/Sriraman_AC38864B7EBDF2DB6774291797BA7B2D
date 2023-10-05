# Define the base Class player
class player:
      def play (self):
          print(" The player is playing cricket.")
# define the derived class Batsman
class Batsman(player):
      def play(self):
          print("The batsman is batting.")
# define the derived class Bowden
class Bouler(player):
      def Play(self):
          print(" The bowder is bowling.")
# create objects of Batsman and Bowler classes
          batsman = Batsman()
          bowler = Bowler()
# call the play() method for each object
          batsman.play()
          bowler.play()
