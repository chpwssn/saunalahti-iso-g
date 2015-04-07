#This processes the input file line by line, makes the HTTP request and records the response code
#for each url in the result file in the format <url>[space]<response code>
import requests, time
from optparse import OptionParser

parser = OptionParser()
parser.add_option("-f", "--file", dest="filename",
                  help="write results to FILE", metavar="FILE")
parser.add_option("-i", "--in",
                  dest="infile", metavar="FILE",
                  help="line separated file of URLs to parse")
parser.add_option("-s", "--sleep", dest="sleep",
                  metavar="SEC", default=10, type="float",
                  help="seconds to wait between requests (float), def: 10.0")

(options, args) = parser.parse_args()
if not options.infile:
    print "We need an input file! --help for info";
    exit()
if not options.filename:
    print "We need a filename to write! --help for info";
    exit()

with open(options.filename, "w") as outfile:
    with open(options.infile, "r") as infile:
        for line in infile.read().split():
            print "Requesting "+line
            r = requests.get(line)
            result = line+" "+str(r.status_code)
            print "Result "+ result
            outfile.write(result+"\n")
            time.sleep(options.sleep)
