def Temprerature_Converter(Ctemp):
   Ftemp = 9*Ctemp/5 + 32 
   return(Ftemp)

def Print_Temprerature(Ctemp, Ftemp):
   print(f"{Ctemp} Celcius Temperature in Fahrenheit Temperature is : {Ftemp}")

def main():
   while True:
      Ctemp = input("Enter Celcius Temperature : ")
      print(type(Ctemp))
      if type(Ctemp) ==  'str' :
         print("Type of Ctemp is String")
      if Ctemp:
         Ctemp = float(Ctemp)
         Ftemp = Temprerature_Converter(Ctemp)
         Print_Temprerature(Ctemp, Ftemp)
         break
      else :
         print("Hey, you haven't Enter Celcius Temperature yet Bro")
         continue

 

if __name__ == "__main__" :
    main()