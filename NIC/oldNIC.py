# Defining the function to check voting eligibility based on NIC
def NIC_voting(NIC):
    "Check if the ID owner can vote"
    if "v" in NIC:
        voting = "Voter"
    elif "x" in NIC:
        voting = "Non-Voter"
    else:
        voting = "Error"
    return voting

# Defining the function to extract the birth year from the NIC
def Birth_year(NIC):
    "Extracting the birth year from the NIC"
    birthyear = "19" + NIC[:2]
    return birthyear

# Defining the function to check the gender of the ID owner
def Gender(NIC):
    "Checking the gender of the ID owner"
    digit = int(NIC[2:5])
    if digit in range(1, 367):
        gender = "male"
    elif digit in range(501, 867):
        gender = "Female"
    else:
        gender = "error"
    return gender

# Main function for processing old NIC information
def Old_NIC_RUN(NIC):
    "Calling the NIC_voting, Birth_year, and Gender functions to extract information"
    voting_result = NIC_voting(NIC)
    birth_year_result = Birth_year(NIC)
    gender_result = Gender(NIC)
    
    "Printing the extracted information"
    print(f"You were born on {birth_year_result}\nYou are a {gender_result}\nYou are a {voting_result}")
    return
