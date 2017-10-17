

print "What is you fave food?",
food = raw_input()
print "What is your fave restaurants?",
restaurant = raw_input()
print "How much do you usually spend there?",
money = int(raw_input())

things = (food, restaurant, money)
print "So, you love %r, usually get it from %r and only spent $%s." % things
