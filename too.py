class FlashCard:

  def __init__self(Self):
    self.fruits = {"strawberries":"pink", "watermelon":"green", "apple":"red", "banana":"yellow"} 
    print("Welcome to Fruit Quiz")
    self.game()
  def game(self):
    fr = random.choice(self.fruits)
    user = input(f"What is the colour of {fr}")
    if user == fr["strawberries"]:
      print("correct")
    else:
      print("Wrong")
    user = int(input("Enter 0, if you want to play again: "))
    if user == 0:
      self.game()
    else:
      return
      
game = FlashCard()