europe = {'spain':{'capital':'madrid','population':46.77},
          'france':{'capital':'paris','population':66.03},
          'germany':{'capital':'berlin','population':80.62},
          'poland':{'capital':'oslo','population':5.084}}
#print capital of france
print(europe['france'],['capital'])

#create subdictionary 'data'
data = {'capital':'rome','population': 59.83}
europe['italy']= 'data'

print(europe)