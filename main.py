import matplotlib.pyplot as plt
import pandas as pd
#reading data
employees_df=pd.read_csv("data/employees.csv")
def discription(df):
     print(df.info())
     print(df.head())
     print(df.columns)

def max(df):
   maxsalary=df["Salary"].max()
   print("the highest salary is :",maxsalary,"of :",df.loc[df["Salary"].idxmax()]["Name"])

def min(df):
    minsalary=df["Salary"].min()
    print("the lowest salary is :",minsalary,"of :",df.loc[df["Salary"].idxmin()]["Name"])

discription(employees_df)
max(employees_df)
min(employees_df)

avrsalary=employees_df["Salary"].mean()
totalsal=employees_df["Salary"].sum()
totalemployees=employees_df["Name"].count()
print("the average salary is :",avrsalary)
print("the total salary is :",totalsal)
print("total employees is :",totalemployees)

def Department_analysis(df):
      sumSA_bydepartement=df.groupby("Department")["Salary"].sum().sort_values(ascending=False)
      print("Sum of salary in each department is :",sumSA_bydepartement)
      AvrSa_bydepartement=df.groupby("Department")["Salary"].mean()
      print("Average salary in each department is :",AvrSa_bydepartement)
      numEM_bydepartment=df.groupby("Department")["Name"].count()
      print("number of employees in each department is :",numEM_bydepartment)
      highsal=df.groupby("Department")["Salary"].max()
      print("the highest salary in each departement is ",highsal,"by",df.loc[df["Salary"]].idxmax()["Name"])

def City_analysis(df):
       sumSA_bycity=df.groupby("City")["Salary"].sum()
       print("Sum of salary in each city is :",sumSA_bycity)
       
       AvrSa_bycity=df.groupby("City")["Salary"].mean().sort_values(ascending=False)
       print("Average salary in each city is :",AvrSa_bycity)
       
       highSalery=df.groupby("City")["Salary"].max()
       print("the highest salary in each city is :",highSalery)

Department_analysis(employees_df)
City_analysis(employees_df)
#graph
color=[]
for salar in sumSA_bydepartement:
   if salar > 110000:
      color.append("blue")
   elif salar > 70000 and salar < 90000:
      color.append("yellow")
   elif salar > 90000 and salar < 110000 :                    
      color.append("green")
   else :
      color.append("red")
plt.title("departement by total sale")
plt.bar(sumSA_bydepartement.index,sumSA_bydepartement,color=color)
plt.xlabel("Department")
plt.ylabel("Salary")
plt.show()

plt.pie(
   numEM_bydepartment,
startangle=90,
labels=employees_df["Department"].unique(),
colors=["green","red","yellow","blue","orange"],
labeldistance=0.5,
explode=[0.3,0,0,0,0]
)
plt.title("Employees by Department")
plt.show()

colors=[]
size=[]
for salar in employees_df["Salary"]:
   if salar >100000:
      colors.append("green")
      size.append(50)
   else:
      colors.append("red")
      size.append(20)
plt.scatter(
employees_df["Experience"],
employees_df["Salary"],
c=colors,
s=size
)
plt.title("salary by experiance")
plt.xlabel("experience")
plt.ylabel("salary")
plt.show()





def findemplo(df,name):
    name=input("What is the employeer name ?:")
    for n in df["Name"]:
        if name == df["Name"]:
            print()
        else :
            print("employeer not found")






