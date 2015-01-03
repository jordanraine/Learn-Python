from sys import argv

script, user_name = argv
prompt = '> '

print "hi %s, Im the %s script." % (user_name, script)
print "Yo fool, i gots some questions."
print "do you want deez nuts %s?" % user_name
likes = raw_input(prompt)

print "Where do you live so i can come steal your things %s?" % user_name
lives = raw_input(prompt)

print "Does your computer have sweet ass graphics?"
computer = raw_input(prompt)

print """
alright, so you said %r about my nuts.
You live in %r. Sounds easy to break in
And your computer has %r . Sick bro...
""" % (likes, lives, computer)

