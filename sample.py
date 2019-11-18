import pandas as pd
import numpy as np
basic=286.00*1
basic_charge1=19.88
basic_charge2=26.46
basic_charge3=30.57
FR=-1.81
RR=2.95

df = pd.read_csv("data1.csv")
df=df.sum()
df=df*30/1000

if df.values<= 120:
    power=basic_charge1*df.values+FR*df.values
elif df.values >120 and df.values <=300:
    power=basic_charge1*120+basic_charge2*(df.values-120)+FR*df.values
else :
    power=basic_charge1*120+basic_charge2*180+(df.values-300)*basic_charge3+FR*df.values

renew=RR*df.all()
cost=basic+power+renew
cost=np.trunc(cost)

print("電気料金は"+str(cost[0])+"円です")
