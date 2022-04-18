

import pandas as pd




data=pd.read_csv("jsrt_metadata.csv")





import matplotlib.pyplot as plt
bins=[0,5,10,15,20,25,30,35,40,45,50,55,60]
#plt.title('Programming for BigData Practice')
#plt.pyplot.xlabel('X-Axis')
#plt.pyplot.ylabel('Y-Axis')
plt.hist(data['diagnosis'].value_counts(),bins=10,color='black', edgecolor='white')
data['diagnosis'].value_counts()





plt.axis("equal")
malignant=data[data['state']=='malignant']['diagnosis'].value_counts()
benign=data[data['state']=='benign']['diagnosis'].value_counts()
plt.pie(malignant,radius=2,shadow=True, autopct='%1.1f%%')
plt.show()
data[data['state']=='malignant']['diagnosis'].value_counts()



plt.pie(benign,radius=2,shadow=True, autopct='%1.1f%%')
plt.show()
data[data['state']=='benign']['diagnosis'].value_counts()





male=data[data['gender']=='Male']['diagnosis'].value_counts()
female=data[data['gender']=='Female']['diagnosis'].value_counts()





plt.pie(male,radius=2,shadow=True, autopct='%1.1f%%')
plt.show()
data[data['gender']=='Male']['diagnosis'].value_counts()




plt.pie(female,radius=2,shadow=True, autopct='%1.1f%%')
plt.show()
data[data['gender']=='Female']['diagnosis'].value_counts()







