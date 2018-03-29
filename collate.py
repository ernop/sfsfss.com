data='''1952
1969
2017
1983
2006
1978
1958
1986
1998
"2017
2017"
2010
2010
"1954
2000"
1991
2005
2010
"2015
2009"
1977
2011
2009
1980
1956
2007
2007'''

counts={}
for line in data.split('\n'):
    l=line.replace('"','')
    l=l.strip()
    n=int(l)
    counts[n]=counts.get(n,0)+1

ii=sorted(counts.items())
min=ii[0][0]
max=ii[-1][0]
SCALE=20
out=open('chart.html','w')
for n in range(min,max+1):
    line='<br>%d<br>%d <span class="bar" style="width:%dpx;"></span>'%(n, counts.get(n,0), counts.get(n,0)*SCALE)
    print(line)
    out.write(line+'\n')
out.close()

