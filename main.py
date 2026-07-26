import matplotlib.pyplot as plt
import pandas as pd
#reading data
df=pd.read_csv("data/employees.csv")

print(df.info())
print(df.head())
print(df.columns)

maxsalary=df["Salary"].max()
minsalary=df["Salary"].min()
print("the highest salary is :",maxsalary,"of :",df.loc[df["Salary"].idxmax()]["Name"])
print("the lowest salary is :",minsalary,"of :",df.loc[df["Salary"].idxmin()]["Name"])

avrsalary=df["Salary"].mean()
totalsal=df["Salary"].sum()
totalemployees=df["Name"].count()
print("the average salary is :",avrsalary)
print("the total salary is :",totalsal)
print("total employees is :",totalemployees)


sumSA_bydepartement=df.groupby("Department")["Salary"].sum().sort_values(ascending=False)
print("Sum of salary in each department is :",sumSA_bydepartement)

AvrSa_bydepartement=df.groupby("Department")["Salary"].mean()
print("Average salary in each department is :",AvrSa_bydepartement)

numEM_bydepartment=df.groupby("Department")["Name"].count()
print("number of employees in each department is :",numEM_bydepartment)

sumSA_bycity=df.groupby("City")["Salary"].sum()
print("Sum of salary in each city is :",sumSA_bycity)

AvrSa_bycity=df.groupby("City")["Salary"].mean().sort_values(ascending=False)
print("Average salary in each city is :",AvrSa_bycity)

highSalery=df.groupby("City")["Salary"].max()
print("the highest salary in each city is :",highSalery)

#graph
color=[]
for salar in sumSA_bydepartement:
   if salar > 300000:
      color.append("green")
   elif salar <  100000:
      color.append("red")
   else :
      color.append("orange")
plt.title("departement by total sale")
plt.bar(sumSA_bydepartement.index,sumSA_bydepartement,color=color)
plt.xlabel("Department")
plt.ylabel("Salary")
plt.show()

plt.pie(
   numEM_bydepartment,
startangle=90,
labels=df["Department"].unique(),
colors=["green","red","yellow","blue","orange"],
labeldistance=0.5,
explode=[0.3,0,0,0,0]
)
plt.title("Employees by Department")
plt.show()

colors=[]
size=[]
for salar in df["Salary"]:
   if salar >100000:
      colors.append("green")
      size.append(50)
   else:
      colors.append("red")
      size.append(20)
plt.scatter(
df["Experience"],
df["Salary"],
c=colors,
s=size
)
plt.title("salary by experiance")
plt.xlabel("experience")
plt.ylabel("salary")
plt.show()