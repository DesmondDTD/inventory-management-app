import requests
import json

BASE_URL = "http://127.0.0.1:5000"

def register():
    email = input("Enter email: ")
    password = input("Enter password: ")
    response = requests.post(f"{BASE_URL}/register", json={"email": email, "password": password})
    print("\nResponse:", response.json())

def login():
    email = input("Enter email: ")
    password = input("Enter password: ")
    response = requests.post(f"{BASE_URL}/login", json={"email": email, "password": password})
    print("\nResponse:", response.json())

def add_item():
    name = input("Enter item name: ")
    quantity = input("Enter quantity: ")
    response = requests.post(f"{BASE_URL}/add_item", json={"name": name, "quantity": int(quantity)})
    print("\nResponse:", response.json())

def search_item():
    query = input("Enter item name to search: ")
    response = requests.get(f"{BASE_URL}/search", params={"query": query})
    print("\nSearch Results:", response.json())

def sort_items():
    key = input("Sort by (name/quantity): ")
    order = input("Order (asc/desc): ")
    response = requests.get(f"{BASE_URL}/sort", params={"key": key, "order": order})
    print("\nSorted Inventory:", response.json())

def menu():
    while True:
        print("\n=== Inventory Management CLI ===")
        print("1. Register")
        print("2. Login")
        print("3. Add Item")
        print("4. Search Item")
        print("5. Sort Inventory")
        print("6. Exit")

        choice = input("Select an option: ")

        if choice == "1":
            register()
        elif choice == "2":
            login()
        elif choice == "3":
            add_item()
        elif choice == "4":
            search_item()
        elif choice == "5":
            sort_items()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    menu()
