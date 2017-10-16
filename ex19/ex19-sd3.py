def non_va_choy(non_soni, choy_soni):
	print "Let's organize a dinner!"
	print "How many people? If we have  %d non and %d tea for each, would that be enough?" % (non_soni, choy_soni)
	thought = raw_input("Please, let us know what you think! \n")
	print "Your %s is important for us" % thought
	print "I hope we are not wasting %d non and %d tea." % ((non_soni - 2), (choy_soni -1))
	advice = int(raw_input("How much non should we be getting? \n"))
	print "I think %d  would be good enough" % advice

non_hajmi = 4
choy_hajmi = 3

print "Let's!"
non_va_choy(5, 6)
non_va_choy(non_hajmi, choy_hajmi)
non_va_choy(5 * 3, choy_hajmi)
non_va_choy(10, 4 - 5 + 6 / 3)
