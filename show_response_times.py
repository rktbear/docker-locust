#!/usr/bin/python

import matplotlib.pyplot as plt
import sys

### Read load test results into memory.

f = open(sys.argv[1], "r")
lines = filter(lambda l: len(l.split()) == 5, f.readlines())
f.close()

### Extract response times.

response_times = [(int(l.split()[0]), int(l.split()[1])) for l in lines]

### Plot the graph.

epoch = [l[0] for l in response_times]
duration = [l[1] for l in response_times]

plt.scatter(epoch, duration, s=5, alpha=0.1)
plt.show()
