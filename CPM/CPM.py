# get execution time
import time
import pandas as pd
from task import *

start_time = time.time()

# load for xlsx files
mydata = pd.read_excel("data.xlsx", sheet_name='Sheet1')
#print(mydata)

# compute for the Critical PATH
mydata = computeCPM(mydata)
printTask(mydata)

# Number of tasks
ntask = mydata.shape[0]

# The critical path
cp = []
for i in range(ntask):
    if (mydata['SLACK'][i] == 0):
        cp.append(mydata['CODE'][i])
print('The critical path is: ' + '-'.join(cp))

# Computing Total project duration
tdur = 0
for i in range(ntask):
    if (mydata['SLACK'][i] == 0):
        tdur = tdur + mydata['DAYS'][i]

print('Total project duration is: ' + str(tdur) + 'unit time')

# Execution time
print('Execution time : %s milli-seconds' % ((time.time() - start_time) * 1000))
