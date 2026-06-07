# 2. AI Dataset Label Counter
# A dataset contains labels represented by numbers:
# [1, 0, 1, 1, 0, 1, 0, 0, 1, 1]
# Create a function that counts the number of positive labels (1) using a loop.
# Requirements:
# ● Use a function with arguments.
# ● Use a loop inside the function.
# ● Return the count.
# ● Display the percentage of positive labels.

def count_positive_labels(labels):
    count = 0

    for label in labels:
        if label == 1:
            count += 1

    return count

dataset = [1, 0, 1, 1, 0, 1, 0, 0, 1, 1]

positive_count = count_positive_labels(dataset)

percentage = (positive_count / len(dataset)) * 100

print("Number of positive labels:", positive_count)
print("Percentage of positive labels:", percentage, "%")