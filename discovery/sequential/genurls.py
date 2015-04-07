with open("saunalahti.fi.nls.txt", "w") as file:
    for x in xrange(0,100000):
        file.write("http://www.saunalahti.fi/nl%05d\n" % x)
    for x in xrange(0,100000):
        file.write("http://www.saunalahti.fi/~nl%05d\n" % x)
