beverage = raw_input("What beverage is in the song?")
third_line = raw_input("What should the third line be? E.g. If one of those bottles should happen to fall,")
bottles = 99
bob="%d bottles of %s on the wall"
bob2="%d bottles of %s."
while (bottles > 2):
  print bob+"," % (bottles, beverage)
  print bob2 % (bottles, beverage)
  print third_line
  bottles = bottles - 1
  print bob+"!" % (bottles, beverage)
print bob+"," % (bottles, beverage)
print bob2 % (bottles, beverage)
print third_line
bottles = bottles - 1
print bob+"!" % (bottles, beverage) # One bottle is a special case.
print bob+"," % (bottles, beverage)
print bob2 % (bottles, beverage)
print third_line
bottles = bottles - 1
print bob+"!" % (bottles, beverage)
print bob+"," % (bottles, beverage)
print bob2 % (bottles, beverage)
print "Go to the store and buy some more,"
bottles = 99
print bob+"!" % (bottles, beverage)
