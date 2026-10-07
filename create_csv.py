import pandas as pd

data_cust = {
    "Customer_ID": ["C001", "C002","C003"],
    "Name": ["Raj", "Priya","Kripa"],
    "Phone": ["9876543210", "9876543211","987654654"],
    "Email": ["raj2000@gmail.com", "priya2003@gmail.com","kripa2006@gmail.com"]
}

df = pd.DataFrame(data_cust)

df.to_csv("customers.csv", index = False)

data_ord = {
    "Order_ID": ["O001","O002","O003","O004","O005"],
    "Customer_ID": ["C001", "C002","C001","C003","C002"],
    "Product": ["Mouse", "Headphones", "Keyboard", "Printer", "Laptop Bag"],
    "Quantity": ["3", "1", "1", "1", "2"],
    "Price": ["1500", "2000", "2500", "25000", "1600"],
    "Status": ["Deliverd", "Processing", "Shipped", "Cancelled", "Pending"],
    "Date": ["25-9-2026", "26-9-2026","26-9-2026", "29-9-2026", "1-10-2026"]
}

df = pd.DataFrame(data_ord)

df.to_csv("orders.csv", index=False)
