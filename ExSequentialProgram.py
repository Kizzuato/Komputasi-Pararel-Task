n = 5
total = 0
print("Serial Computation")
for i in range(1, n + 1):
    total += i
    print(f"Step {i}: Total = {total}")
    
print(f"Final Serial sum is: {total}")