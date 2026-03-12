
def stress_test():
    print("Starting heavy calculation...")
    result = sum(i**2 for i in range(10**7))
    return result
