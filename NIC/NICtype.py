def NIC_Type_Check(NIC):
    "check if the NIC is new or old"
    if "v" in NIC:
        nic_type ="Old"
    elif "x" in NIC:
        nic_type ="Old"
    else:
        nic_type ="New"
    return nic_type
