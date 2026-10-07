import pandas as pd
import validators as v

FILE_NAME = "customers.csv"


def add_c(name, phone, email):

    customers = pd.read_csv(FILE_NAME, dtype={"Phone": str})

    name = v.validate_name(name)
    phone = v.validate_phone(phone)
    email = v.validate_email(email)

    cid = f"C{len(customers) + 1:03d}"
    customers.loc[len(customers)] = [cid, name, phone, email]
    customers.to_csv(FILE_NAME, index=False)

    return f"Customer added successfully. Customer ID: {cid}"


def view_c():

    customers = pd.read_csv(FILE_NAME, dtype={"Phone": str})

    if customers.empty:
        return "No customer records found."

    return customers.to_string(index=False)


def search_c(cid):

    customers = pd.read_csv(FILE_NAME, dtype={"Phone": str})

    cid = str(cid).strip().upper()
    result = customers[customers["Customer_ID"].astype(str).str.upper() == cid]

    if result.empty:
        return "Customer not found."

    return result.to_string(index=False)


def update_c(cid, choice, new_value):

    customers = pd.read_csv(FILE_NAME, dtype={"Phone": str})

    cid = str(cid).strip().upper()
    result = customers[customers["Customer_ID"].astype(str).str.upper() == cid]

    if result.empty:
        raise ValueError("Customer not found.")

    index = result.index[0]

    if choice == "Name":
        new_value = v.validate_name(new_value)
        customers.loc[index, "Name"] = new_value

    elif choice == "Phone":
        new_value = v.validate_phone(new_value)
        customers.loc[index, "Phone"] = new_value

    elif choice == "Email":
        new_value = v.validate_email(new_value)
        customers.loc[index, "Email"] = new_value

    else:
        raise ValueError("Invalid update option.")

    customers.to_csv(FILE_NAME, index=False)

    return "Customer updated successfully."