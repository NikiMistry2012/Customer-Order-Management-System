import re

def validate_name(name):
    name = str(name).strip()
    if len(name) < 2 or not re.fullmatch(r"[A-Za-z .'-]+", name):
        raise ValueError("Name must be at least 2 letters (letters/spaces only).")
    return name.title()


def validate_phone(phone):
    phone = str(phone).strip()
    if not re.fullmatch(r"\d{10}", phone):
        raise ValueError("Phone must be exactly 10 digits.")
    return phone


def validate_email(email):
    email = str(email).strip()
    if email and not re.fullmatch(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", email):
        raise ValueError("Invalid email format.")
    return email

def validate_order_id(order_id):
    order_id = str(order_id).strip().upper()

    if not re.fullmatch(r"O\d{3}", order_id):
        raise ValueError("Order ID must be like O001, O002, etc.")

    return order_id


def validate_customer_id(customer_id):
    customer_id = str(customer_id).strip().upper()

    if not re.fullmatch(r"C\d{3}", customer_id):
        raise ValueError("Customer ID must be like C001, C002, etc.")

    return customer_id


def validate_product(product):
    product = str(product).strip()

    if len(product) < 2:
        raise ValueError("Product name must contain at least 2 characters.")

    return product.title()


def validate_quantity(quantity):
    try:
        quantity = int(quantity)
    except ValueError:
        raise ValueError("Quantity must be a whole number.")

    if quantity <= 0:
        raise ValueError("Quantity must be greater than 0.")

    return quantity


def validate_price(price):
    try:
        price = float(price)
    except ValueError:
        raise ValueError("Price must be a number.")

    if price <= 0:
        raise ValueError("Price must be greater than 0.")

    return price


def validate_status(status):
    status = str(status).strip().title()

    valid_status = [
        "Pending",
        "Processing",
        "Shipped",
        "Delivered",
        "Cancelled"
    ]

    if status not in valid_status:
        raise ValueError(
            "Invalid status. Use Pending, Processing, Shipped, Delivered or Cancelled."
        )
    return status
