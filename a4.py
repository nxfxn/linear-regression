import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv("/Users/neildafarrar/Dropbox/UH/Spring 2017/ELET 6318/Assignments/Assignment 4/data.txt", index_col=False, sep = " ", names = ['Tasks', 'Time'])

data['xy']=data.Tasks * data.Time
data['x2']=data.Tasks * data.Tasks

summ=data.sum(axis=0)
n=len(data.index)

sum_x=summ[0]
sum_y=summ[1]
sum_xy=summ[2]
sum_x2=summ[3]

ave_x = summ[0]/n
ave_y =summ[1]/n
ave_xy = summ[2]/n
ave_x2 = summ[3]/n

b1_num=float(sum_xy-(n*ave_x*ave_y))
b1_den=float(sum_x2-(n*ave_x*ave_x))
b1=float(b1_num)/float(b1_den)
b0=float(ave_y)-float(b1*ave_x)

print "\nLinear regression parameters:\n=========================\nb1 = %f\nb0 = %f" %(b1, b0)

y=[]
for i in data["Tasks"]:
    y.append(b0+b1*i)
new_y=pd.Series(y)
data['y_']=new_y.values

e=[]
for i in range(data['Time'].size):
    e.append(data.get_value(i,'Time') - data.get_value(i,'y_'))        
new_e=pd.Series(e)
data['e']=new_e.values

e2=[]
for i in range(data['Time'].size):
    e2.append(data.get_value(i,'e')**2)             
new_e2=pd.Series(e2)
data['e2']=new_e2.values

summ2=data.sum(axis=0)
sse=summ2[6]/n

sst_y=[]
for i in range(data['Time'].size):
    s=data.get_value(i,'Time')-data.get_value(i,'y_')
    sst_y.append(s**2)             
new_sst=pd.Series(sst_y)
data['(y-y_)^2']=new_sst.values



sst=data['(y-y_)^2'].values.sum()

ssr=sst-sse
r2=ssr/sst


#print data
print "Coefficient of determination (R^2) = %f\n" %(r2)

#plt.plot(kind='scatter', x='Tasks', y='Time', c="c" , s=6, figsize=(16, 8))
#plt.plot(kind='line', x='Tasks', y='y_', c='r')

plt.figure(figsize=(16, 8))
plt.scatter(data['Tasks'], data['Time'], c='c', s=6, label='Sample scatter plot')
plt.plot(data['Tasks'], data['y_'], c='r', label='y=%f+%f Concurrent Tasks'%(b0,b1))

plt.title('Linear Regression')
plt.xlabel('Concurrent compression tasks (Count)')
plt.ylabel('Total completion time (Time units)')
plt.legend()
plt.show()

