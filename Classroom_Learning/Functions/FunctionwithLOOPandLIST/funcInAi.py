def load_data(filepath):
    """Load dataset from file"""
    data = []

    with open(filepath) as f:
        for line in f:
            data.append(line.strip().split(","))

    return data


def normalise(values):
    """Min-Max normalization"""
    mn, mx = min(values), max(values)

    return [(v - mn) / (mx - mn) for v in values]


def accuracy(predictions, labels):
    """Compute classification accuracy"""

    correct = sum(p == l for p, l in zip(predictions, labels))

    return round(correct / len(labels) * 100, 2)


def train_epoch(model, data, lr=0.01):
    """Simulate one training epoch"""

    total_loss = 0

    for x, y in data:
        pred = model(x)

        loss = (pred - y) ** 2

        total_loss += loss

    return total_loss / len(data)


# Compute the pipeline
raw = [23, -1, 45, 89, 67, 24]

# remove negative values
clean = [v for v in raw if v >= 0]

# normalize
normd = normalise(clean)

preds = [1, 0, 1, 1, 0]
labels = [1, 0, 1, 0, 0]

print("Normalized:", [round(n, 3) for n in normd])

print("Accuracy:", accuracy(preds, labels), "%")