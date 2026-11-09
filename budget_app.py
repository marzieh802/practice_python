def budget_manager(amount):
    budget = amount

    def manager(action, money=0):
        nonlocal budget
        if action == "add":
            budget += money
            print(f"add: {money},budget: {budget}")
        elif action == "spend":
            budget -= money
            print(f"spend: {money},budget: {budget}")
        elif action == "get":
            print(f"the budget is : {budget}")
        else:
            print("invalid action")
    return manager


my_budget = budget_manager(1000)
my_budget("get")
my_budget("add", 1000)
my_budget("spend", 500)
my_budget("get")
