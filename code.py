beverage = raw_input("What beverage is in the song?")
third_line = raw_input("What should the third line be? E.g. If one of those bottles should happen to fall,")

set bottles == 99
repeat 97
  print bottles "bottles of "beverage" on the wall,"
  print bottles "bottles of "beverage"."
  print third_line
  set bottles == bottles - 1
  print bottles "bottles of "beverage" on the wall!"
print bottles "bottles of "beverage" on the wall,"
print bottles "bottles of "beverage"."
print third_line
set bottles == bottles - 1
print bottle "bottle of "beverage" on the wall!" # One bottle is a special case.
print bottles "bottle of "beverage" on the wall,"
print bottles "bottle of "beverage"."
print third_line
set bottles == bottles - 1
print bottles "bottles of "beverage" on the wall!"
print bottles "bottles of "beverage" on the wall,"
print bottles "bottles of "beverage" on the wall."
print "Go to the store and buy some more,"
set bottles == 99
print bottles "bottles" of "beverage" on the wall!"
