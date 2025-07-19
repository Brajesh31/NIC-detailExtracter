# Importing the necessary modules from the NIC package
import NIC.NICtype
import NIC.oldNIC
import NIC.newNIC

# Taking input from the user for NIC Number
NIC_Number = input("Enter your NIC Number: ")

# Checking the type of NIC using the NIC_Type_Check function from NICtype module in NIC package
Ntype = NIC.NICtype.NIC_Type_Check(NIC_Number)

# If the NIC type is "Old", execute the Old_NIC_RUN function from oldNIC module in NIC package
if Ntype == "Old":
    print("NIC type : ", Ntype)
    NIC.oldNIC.Old_NIC_RUN(NIC_Number)
# If the NIC type is not "Old", execute the New_NIC_RUN function from newNIC module in NIC package 
else:
    print("NIC type : ", Ntype)
    NIC.newNIC.New_NIC_RUN(NIC_Number)
