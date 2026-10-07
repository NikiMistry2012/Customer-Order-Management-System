import pandas as pd
import validators as v

FILE_NAME = "orders.csv"
CUSTOMER_FILE = "customers.csv"

def add_o(customer_id, product, quantity, price, status, date):

    orders = pd.read_csv(FILE_NAME)
    customers = pd.read_csv(CUSTOMER_FILE, dtype={"Phone": str})

    if orders.empty:
        order_id = "O001"
    else:
        numbers = (orders["Order_ID"].astype(str).str.extract(r"(\d+)")[0].astype(int))
        order_id = f"O{numbers.max() + 1:03d}"

    customer_id = v.validate_customer_id(customer_id)

    if customer_id not in customers["Customer_ID"].values:
        raise ValueError("Customer ID does not exist.")

    product = v.validate_product(product)
    quantity = v.validate_quantity(quantity)
    price = v.validate_price(price)
    status = v.validate_status(status)

    date = str(date).strip()

    if not date:
        raise ValueError("Date cannot be empty.")

    new_order = {
        "Order_ID": order_id,
        "Customer_ID": customer_id,
        "Product": product,
        "Quantity": quantity,
        "Price": price,
        "Status": status,
        "Date": date
    }

    orders.loc[len(orders)] = new_order
    orders.to_csv(FILE_NAME, index=False)

    return (
        "Order added successfully.\n"
        f"Order ID: {order_id}")

def view_o():

    orders = pd.read_csv(FILE_NAME)
    if orders.empty:
        return "No orders found."
    return orders.to_string(index=False)


def search_o(choice, value):

    orders = pd.read_csv(FILE_NAME)
    value = str(value).strip()

    if not value:
        raise ValueError("Search value cannot be empty.")

    if choice == "Order ID":
        value = value.upper()
        result = orders[orders["Order_ID"].astype(str).str.upper() == value]

    elif choice == "Customer ID":
        value = value.upper()
        result = orders[orders["Customer_ID"].astype(str).str.upper() == value]

    elif choice == "Status":
        value = value.title()
        result = orders[orders["Status"].astype(str).str.title() == value]

    elif choice == "Product":
        result = orders[orders["Product"].astype(str).str.lower().str
                        .contains(value.lower(),na=False)]

    else:
        raise ValueError("Invalid search option.")

    if result.empty:
        return "No matching orders found."
    return result.to_string(index=False)


def update_status(order_id, new_status):

    orders = pd.read_csv(FILE_NAME)
    order_id = str(order_id).strip().upper()

    result = orders[orders["Order_ID"].astype(str).str.upper() == order_id]

    if result.empty:
        raise ValueError("Order not found.")

    new_status = v.validate_status(new_status)

    index = result.index[0]
    orders.loc[index, "Status"] = new_status

    orders.to_csv(FILE_NAME, index=False)
    return "Order status updated successfully."


def calculate_order_values():

    orders = pd.read_csv(FILE_NAME)

    if orders.empty:
        return "No orders found."

    orders["Quantity"] = pd.to_numeric(orders["Quantity"])
    orders["Price"] = pd.to_numeric(orders["Price"])
    orders["Order_Value"] = (orders["Quantity"] *orders["Price"])

    result = orders[
        [
            "Order_ID",
            "Product",
            "Quantity",
            "Price",
            "Order_Value"
        ]].to_string(index=False)

    total_sales = orders["Order_Value"].sum()
    result += ("\n\nTotal Sales: " + str(total_sales))
    return result