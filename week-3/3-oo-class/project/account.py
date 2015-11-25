def deposit(account, amount):
    account["balance"] += amount
    return account["balance"]

def withdraw(account, amount):
    account["balance"] -= amount
    return account["balance"]
