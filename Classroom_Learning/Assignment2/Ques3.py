# 3. Model Training Epoch Simulator
# Write a Python program that simulates model training for a given number of epochs.
# Requirements:
# ● Create a function train_model(epochs).
# ● Use a for loop to display:
# Epoch 1 completed
# Epoch 2 completed
# ...
# ● Print "Training Finished" after the loop.

def train_model(epochs):
    for epoch in range(1, epochs + 1):
        print(f"Epoch {epoch} completed")

    print("Training Finished")

epochs = int(input("Enter number of epochs: "))

train_model(epochs)