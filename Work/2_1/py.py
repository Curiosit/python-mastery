
import tracemalloc
f = open('ctabus.csv')
tracemalloc.start()
data = f.read()