import os
import time

# 1. Create a dummy package/folder
folder_name = "temp_heavy_module"
if not os.path.exists(folder_name):
    os.makedirs(folder_name)

# 2. Write a "heavy" function into a separate file
# This triggers the compiler to create a .pyc file in __pycache__
with open(f"{folder_name}/heavy_logic.py", "w") as f:
    f.write("""
def stress_test():
    print("Starting heavy calculation...")
    result = sum(i**2 for i in range(10**7))
    return result
""")

# 3. Import the newly created module
# This is the exact moment __pycache__ is born!
from temp_heavy_module import heavy_logic

if __name__ == "__main__":
    start = time.time()
    val = heavy_logic.stress_test()
    end = time.time()
    print(f"Result: {val}")
    print(f"Time taken: {end - start:.2f} seconds")
    print("\nCheck your folder... Do you see '__pycache__'? 😉")