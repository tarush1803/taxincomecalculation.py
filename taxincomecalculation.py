mtab=("\t\t\t\t\t")
date=input("Enter the Date :- ")
a=input("Enter the type/name of Taxholder : DOMESTIC COMPANY, FOREIGN COMPANY,INDIVIDUAL(RESIDENT AND NON RESIDENT),SENIOR CITIZEN(RESIDENT INDIVIDUAL AGE 60YEAR OR MORE),FOR SUPER SENIOR CITIZEN(RESIDENT INDIVIDUAL AGE 80 YEARS OR MORE),For Partnership Firm :-  ")
cn=input("Enter the Name of Company / Person :- ")
b=int(input("Enter the Income :- "))
ay=input("Enter the Assesment Year :- ")
print("***********************************************************************************************************************\n")
print(mtab,"TAX RATES FOR Assesment YEAR",ay,"\n")
print("Date :- ",date,"\n")
print(a,"\n")
print(cn)
print("-----------------------------------------------------------------------------------------------------------------------\n")
print("Income Slip","\n")
print("Income :- ",b, "Ruppess \n")
if a=="INDIVIDUAL" and b<=250000:
    print("Tax Rate :- Nil")
    print("Tax Amount:- ","0","Ruppess")
    print("Actual Income after TAX Deduction :-",b,"Ruppess","\n\n","THANK YOU \n INCOME TAX DEPARTMENT")
elif a=="INDIVIDUAL" and b>250000 and b<=500000:
        at=b-250000
        d=250000+(at-(at*0.05))
        taxamount=at*0.05
        print("Tax Rate :- 5%")
        print("Tax Amount:- ",taxamount,"Ruppess")
        print("Actual Income after TAX Deduction :-",d,"Ruppess","\n\n","THANK YOU \n INCOME TAX DEPARTMENT")
elif a=="INDIVIDUAL" and b>500000 and b<=750000:
        at=b-500000
        d=250000+237500+(at-(at*0.1))
        taxamount=(250000*0.05)+(at*0.1)
        print("Tax Rate :- 10%")
        print("Tax Amount:- ",taxamount,"Ruppess")
        print("Actual Income after TAX Deduction :-",d,"Ruppess","\n\n","THANK YOU \n INCOME TAX DEPARTMENT")
elif a=="INDIVIDUAL" and b>750000 and b<=1000000:
        at=b-750000
        d=250000+237500+225000+(at-(at*0.15))
        taxamount=(250000*0.05)+(250000*0.1)+(at*0.15)
        print("Tax Rate :- 15%")
        print("Tax Amount:- ",taxamount,"Ruppess")
        print("Actual Income after TAX Deduction :-",d,"Ruppess","\n\n","THANK YOU \n INCOME TAX DEPARTMENT")
elif a=="INDIVIDUAL" and b>1000000 and b<=1250000:
        at=b-1000000
        d=250000+237500+225000+212500+(at-(at*0.2))
        taxamount=(250000*0.05)+(250000*0.1)+(250000*0.15)+(at*0.2)
        print("Tax Rate :- 20%")
        print("Tax Amount:- ",taxamount,"Ruppess")
        print("Actual Income after TAX Deduction :-",d,"Ruppess","\n\n","THANK YOU \n INCOME TAX DEPARTMENT")
elif a=="INDIVIDUAL" and b>1250000 and b<=1500000:
        at=b-1250000
        d=250000+237500+225000+212500+200000+(at-(at*0.25))
        taxamount=(250000*0.05)+(250000*0.1)+(250000*0.15)+(250000*0.2)+(at*0.25)
        print("Tax Rate :- 25%")
        print("Tax Amount:- ",taxamount,"Ruppess")
        print("Actual Income after TAX Deduction :-",d,"Ruppess","\n\n","THANK YOU \n INCOME TAX DEPARTMENT")
elif a=="INDIVIDUAL" and b>1500000:
        at=b-1500000
        d=250000+237500+225000+212500+200000+187500+(at-(at*0.3))
        taxamount=(250000*0.05)+(250000*0.1)+(250000*0.15)+(250000*0.2)+(250000*0.25)+(at*0.3)
        print("Tax Rate :- 30%")
        print("Tax Amount:- ",taxamount,"Ruppess")
        print("Actual Income after TAX Deduction :-",d,"Ruppess","\n\n","THANK YOU \n INCOME TAX DEPARTMENT")
elif a=="SENIOR CITIZEN" and b<=300000:
    print("Tax Rate :- Nil")
    print("Tax Amount:- ","0","Ruppess")
    print("Actual Income after TAX Deduction :-",b,"Ruppess","\n\n","THANK YOU \n INCOME TAX DEPARTMENT")
elif a=="SENIOR CITIZEN" and b>300000 and b<=500000:
        at=b-300000
        d=300000+(at-(at*0.05))
        taxamount=at*0.05
        print("Tax Rate :- 5%")
        print("Tax Amount:- ",taxamount,"Ruppess")
        print("Actual Income after TAX Deduction :-",d,"Ruppess","\n\n","THANK YOU \n INCOME TAX DEPARTMENT")
elif a=="SENIOR CITIZEN" and b>500000 and b<=1000000:
        at=b-500000
        d=300000+190000+(at-(at*0.2))
        taxamount=(200000*0.05)+(at*0.2)
        print("Tax Rate :- 20%")
        print("Tax Amount:- ",taxamount,"Ruppess")
        print("Actual Income after TAX Deduction :-",d,"Ruppess","\n\n","THANK YOU \n INCOME TAX DEPARTMENT")
elif a=="SENIOR CITIZEN" and b>1000000:
        at=b-1000000
        d=300000+190000+400000+(at-(at*0.3))
        taxamount=(200000*0.05)+(500000*0.2)+(at*0.3)
        print("Tax Rate :- 30%")
        print("Tax Amount:- ",taxamount,"Ruppess")
        print("Actual Income after TAX Deduction :-",d,"Ruppess","\n\n","THANK YOU \n INCOME TAX DEPARTMENT")
elif a=="SUPER SENIOR CITIZEN" and b<=500000:
    print("Tax Rate :- Nil")
    print("Tax Amount:- ","0","Ruppess")
    print("Actual Income after TAX Deduction :-",b,"Ruppess","\n\n","THANK YOU \n INCOME TAX DEPARTMENT")
elif a=="SUPER SENIOR CITIZEN" and b>500000 and b<=1000000:
        at=b-500000
        d=500000+(at-(at*0.2))
        taxamount=at*0.2
        print("Tax Rate :- 20%")
        print("Tax Amount:- ",taxamount,"Ruppess")
        print("Actual Income after TAX Deduction :-",d,"Ruppess","\n\n","THANK YOU \n INCOME TAX DEPARTMENT")
elif a=="SUPER SENIOR CITIZEN" and b>1000000:
        at=b-1000000
        d=500000+400000+(at-(at*0.3))
        taxamount=(500000*0.2)+(at*0.3)
        print("Tax Rate :- 20%")
        print("Tax Amount:- ",taxamount,"Ruppess")
        print("Actual Income after TAX Deduction :-",d,"Ruppess","\n\n","THANK YOU \n INCOME TAX DEPARTMENT")
elif a=="DOMESTIC COMPANY":
        d=(b-(b*0.3))
        taxamount=b*0.3
        print("Tax Rate :- 30%")
        print("Tax Amount:- ",taxamount,"Ruppess")
        print("Actual Income after TAX Deduction :-",d,"Ruppess","\n\n","THANK YOU \n INCOME TAX DEPARTMENT")
elif a=="FOREIGN COMPANY":
        d=(b-(b*0.4))
        taxamount=b*0.4
        print("Tax Rate :- 40%")
        print("Tax Amount:- ",taxamount,"Ruppess")
        print("Actual Income after TAX Deduction :-",d,"Ruppess","\n\n","THANK YOU \n INCOME TAX DEPARTMENT")
elif a=="PARTNERSHIP FIRM":
        d=(b-(b*0.3))
        taxamount=b*0.3
        print("Tax Rate :- 30%")
        print("Tax Amount:- ",taxamount,"Ruppess")
        print("Actual Income after TAX Deduction :-",d,"Ruppess","\n\n","THANK YOU \n INCOME TAX DEPARTMENT")
else:
    print("PLEASE ENTER CORRECT TYPE OF TAXHOLDER NAME ND CORRECT DATA\n","RE-ENTER THE DETAIL\n","\n\n","THANK YOU \n INCOME TAX DEPARTMENT")



    
    

    



    