import readrides
rows = readrides.read_rides_as_dicts('ctabus.csv')



## 1 Unique routes
uni_routes = { s['route'] for s in rows }
len(uni_routes)

## 2 Specific date and route
x =[s for s in rows if s['date'] == '02/02/2011' and s['route']=='22' ]
x[0]['rides']

## 3 Count rides
totals = { s['route']: 0 for s in rows }
for s in rows:
        totals[s['route']] += s['rides']

## Specific date and route
x =[s for s in rows if '2001' in s['date']]
totals = { s['route']: 0 for s in x }
for s in x:
        totals[s['route']] += s['rides']


## Specific date and route
x =[s for s in rows if '2001' in s['date']]
totals2001 = Counter()
for s in x:
        totals2001[s['route']] += s['rides']

x =[s for s in rows if '2011' in s['date']]
totals2011 = Counter()
for s in x:
        totals2011[s['route']] += s['rides']


totals = totals2011-totals2001
totals.most_common(5)