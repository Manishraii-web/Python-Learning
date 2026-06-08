# 4. Recursive Learning Rate Decay Calculator
# In machine learning, the learning rate is reduced after each iteration.
# Write a recursive function that calculates the learning rate after n iterations using:
# new_rate = current_rate × 0.9
# Requirements:
# ● Use recursion only.
# ● Accept initial learning rate and iteration count as arguments.
# ● Return the final learning rate.

def learning_rate_decay(current_rate, iterations):
    if iterations == 0:
        return current_rate

    return learning_rate_decay(current_rate * 0.9, iterations - 1)

initial_rate = float(input("Enter initial learning rate: "))
n = int(input("Enter number of iterations: "))

final_rate = learning_rate_decay(initial_rate, n)

print("Final learning rate:", final_rate)