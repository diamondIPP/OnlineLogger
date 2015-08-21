'''
Converts the logger outputfile to run_log.json, which is used by myPadAnalysis scripts (Mario Seeli)
'''

import json

source = open("outputfile.json", "r")
dumpfile = open("run_log.json", "w")

data = json.load(source)

data_formatted = {}

for i in xrange(len(data)):
    key = data[i].keys()[0]
    runinfo = data[i][key]
    data_formatted[key] = runinfo

json.dump(data_formatted, dumpfile, indent=3, sort_keys=True)

dumpfile.close()
source.close()
