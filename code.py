beverage = raw_input("What beverage is in the song?")
third_line = raw_input("What should the third line be? E.g. If one of those bottles should happen to fall,")
bottles = 99
while (bottles > 2):
  print "%d bottles of %s on the wall," % (bottles, beverage)
  print "%d bottles of %s." % (bottles, beverage)
  print third_line
  bottles = bottles - 1
  print "%d bottles of %s on the wall!" % (bottles, beverage)
print "%d bottles of %s on the wall," % (bottles, beverage)
print "%d bottles of %s." % (bottles, beverage)
print third_line
bottles = bottles - 1
print "%d bottle of %s on the wall!" % (bottles, beverage) # One bottle is a special case.
print "%d bottle of %s on the wall," % (bottles, beverage)
print "%d bottle of %s." % (bottles, beverage)
print third_line
bottles = bottles - 1
print "%d bottles of %s on the wall!" % (bottles, beverage)
print "%d bottles of %s on the wall," % (bottles, beverage)
print "%d bottles of %s." % (bottles, beverage)
print "Go to the store and buy some more,"
bottles = 99
print "%d bottles of %s on the wall!" % (bottles, beverage)
