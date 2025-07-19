def Birth_year(NIC):
    "Extracting the birth year from the NIC"
    birthyear = NIC[:4]
    return birthyear

def Gender(NIC):
    "Checking the gender of the ID owner"
    digit = int(NIC[4:7])
    if digit in range(1, 367):
        gender = "male"
    elif digit in range(501, 867):
        gender = "female"
    else:
        gender = "error"
    return gender

def New_NIC_RUN(NIC):
    "Calling the Birth_year and Gender functions to extract information"
    Birth_Year_Result = Birth_year(NIC)
    Gender_Result = Gender(NIC)

    "Printing the extracted information"
    print(f"You were born on {Birth_Year_Result}\nYou are a {Gender_Result}")
    return
