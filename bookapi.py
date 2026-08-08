import requests as req
from dotenv import load_dotenv
import os

load_dotenv()

BASE_URL = os.getenv("BASE_URL")

# We are using a Book API


response = req.get(BASE_URL)
print(response.status_code)

# Now we will see the list of books

books_url = f"{BASE_URL}/books"

r = req.get(books_url)
print(r.status_code)
print(f"List of Books\n{r.json()}")

# In order to search one book, we will use id

""" 
Optional query parameters:
type: fiction or non-fiction
limit: a number between 1 and 20.
"""

id = 1
book_url =  f"{BASE_URL}/books/{id}"
params = {"type" : "fiction", "limit" : 2}

r = req.get(book_url, params=params)
print(r.status_code)
print(f"Book with id {id}\n{r.json()}")

# We want to place an order of book (HINT: Adding data)

order_url = f"{BASE_URL}/orders"
playload = {
    "bookId" : 2,
    "customerName" : "Rehaan"
}

r = req.post(BASE_URL)
print(f"At first order status code: {r.status_code}\nMeans Unauthorized error. We first have to add our Credentials")

# Unauthorised Error: We can't order book until we veirfy ourself(provide our credentials) to book store

verify_url = f"{BASE_URL}/api-clients"
user_detail ={
   "clientName": "Rehaan",
   "clientEmail": "rehaan@example.com"
}

r = req.post(verify_url, json=user_detail)
print(f"Verification Status: {r.status_code}")
print(f"Result of Verification\n{r.json()}")

# We got the access token from verify json result "ACCESS_TOKEN"

# It's time to order a book

order_url = f"{BASE_URL}/orders"
order_detail = {
    "bookId" : 2,
    "customerName" : "Rehaan"
}

ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")

r = req.post(order_url, json=order_detail, headers={"Authorization" : f"Bearer {ACCESS_TOKEN}"})
print(f"Order Status: {r.status_code}") # If 404 book out of stock
print(f"Order Status: {r.json()}") 

# Giving another order

order_detail = {
    "bookId" : 1,
    "customerName" : "Rehaan"
}

r = req.post(order_url, json=order_detail, headers={"Authorization" : f"Bearer {ACCESS_TOKEN}"})
print(f"Order Status: {r.status_code}") 
print(f"Order Status: {r.json()}") # Book is successfully Ordered

# Its time to check order list

r = req.get(order_url ,headers={"Authorization" : f"Bearer {ACCESS_TOKEN}"})
print(f"Order List\n{r.json()}")

# Suppose some client want to change his name in order

order_id = "ysUWEBBynAKMEqKVoWU1Y" # Person with that order id

update_order_url = f"{BASE_URL}/orders/{order_id}"

r = req.patch(update_order_url, json={"customerName" : "Mufassa"}, headers={"Authorization" : f"Bearer {ACCESS_TOKEN}"})
print(f"Update status: {r.status_code}")

# Now we will see the updated order list

r = req.get(order_url ,headers={"Authorization" : f"Bearer {ACCESS_TOKEN}"})
print(f"Order List\n{r.json()}")

# Some person cancelled his order so we want to remove it from order list

order_id = "dwOEPgyVq4StyU80ZfOR4"
update_order_url = f"{BASE_URL}/orders/{order_id}"

r = req.delete(update_order_url, headers={"Authorization" : f"Bearer {ACCESS_TOKEN}"})
print(f"Delete status: {r.status_code}")

# Check order list after Deletion

r = req.get(order_url, headers={"Authorization" : f"Bearer {ACCESS_TOKEN}"})
print(f"Order List\n{r.json()}")
