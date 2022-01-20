import pandas as pd

name = ['United States','Austrailia','Japan','India','Russia','Morocco','Egypt']
dr = [True,False,False,False,True,True,True]
cpc =[809,731,588,18,200,70,45]
my_dict = {'country': name,'Driving rights': dr,'Cars per Capita':cpc}
cars=pd.DataFrame(my_dict)
print(cars)