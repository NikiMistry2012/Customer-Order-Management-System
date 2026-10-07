import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

ORDER_FILE = "orders.csv"
CUSTOMER_FILE = "customers.csv"

def order_summary():

    orders = pd.read_csv(ORDER_FILE)

    if orders.empty:
        return "No orders found."

    orders["Quantity"] = pd.to_numeric(orders["Quantity"])
    orders["Price"] = pd.to_numeric(orders["Price"])
    orders["Order_Value"] = (orders["Quantity"] * orders["Price"])
    
    total_orders = len(orders)
    total_sales = orders["Order_Value"].sum()
    average_order = np.mean(orders["Order_Value"])
    highest_order = np.max(orders["Order_Value"])
    lowest_order = np.min(orders["Order_Value"])

    result = (
        "===== ORDER SUMMARY =====\n\n"
        f"Total Orders: {total_orders}\n"
        f"Total Sales: {total_sales:.2f}\n"
        f"Average Order Value: {average_order:.2f}\n"
        f"Highest Order Value: {highest_order:.2f}\n"
        f"Lowest Order Value: {lowest_order:.2f}"
    )
    return result

def status_analysis():

    orders = pd.read_csv(ORDER_FILE)

    if orders.empty:
        return "No orders found."

    status_count = orders["Status"].value_counts()

    result = (
        "===== ORDERS BY STATUS =====\n\n"
        + status_count.to_string()
    )
    return result


def frequent_customers():

    orders = pd.read_csv(ORDER_FILE)
    customers = pd.read_csv(CUSTOMER_FILE, dtype={"Phone": str})

    if orders.empty:
        return "No orders found."

    customer_orders = (orders["Customer_ID"].value_counts())

    frequent = customer_orders[customer_orders >= 2]

    if frequent.empty:
        return (
            "===== FREQUENT CUSTOMERS =====\n\n"
            "No frequent customers found."
        )

    result = ("===== FREQUENT CUSTOMERS =====\n\n")

    for customer_id, order_count in frequent.items():
        customer = customers[customers["Customer_ID"] == customer_id]

        if not customer.empty:
            name = customer.iloc[0]["Name"]
            result += (
                f"{customer_id} - "
                f"{name} - "
                f"{order_count} orders\n"
            )
    return result

def product_analysis():

    orders = pd.read_csv(ORDER_FILE)

    if orders.empty:
        return "No orders found."

    orders["Quantity"] = pd.to_numeric(orders["Quantity"])
    orders["Price"] = pd.to_numeric(orders["Price"])
    orders["Order_Value"] = (orders["Quantity"] * orders["Price"])
    product_sales = (orders.groupby("Product")["Order_Value"].sum())

    result = (
        "===== SALES BY PRODUCT =====\n\n"
        + product_sales.to_string()
)
    return result


def status_chart():

    orders = pd.read_csv(ORDER_FILE)

    if orders.empty:
        raise ValueError("No orders available for chart.")

    status_count = (orders["Status"].value_counts())

    plt.figure(figsize=(7, 7))
    plt.pie(
        status_count.values,labels=status_count.index,
        autopct="%1.1f%%",startangle=90)
    plt.title("Orders by Status")
    plt.show()


def product_sales_chart():

    orders = pd.read_csv(ORDER_FILE)

    if orders.empty:
        raise ValueError("No orders available for chart.")

    orders["Quantity"] = pd.to_numeric(orders["Quantity"])
    orders["Price"] = pd.to_numeric(orders["Price"])
    orders["Order_Value"] = (orders["Quantity"] * orders["Price"])

    product_sales = (orders.groupby("Product")["Order_Value"].sum())

    plt.figure(figsize=(9, 5))
    plt.bar(product_sales.index, product_sales.values, width=0.4)
    plt.xlabel("Product")
    plt.ylabel("Sales Value")
    plt.title("Sales by Product")
    plt.xticks(rotation=30)
    plt.tight_layout()
    plt.show()