def load_data(filepath):
    """Load dataset from file"""
    data = []
    with open(filepath) as f:
        for line in f:
            data.append(line.string().split(","))
        return data
    
def normalise(values):
    """Min-Max normalization - standard ML sign"""
    mn,mx = min(values), max(values)
    return [(v -mn)/ (mx-mn) for v in values]
def accuracy(predictions, labels):
    """Compute classification accuracy"""
    correct = sum(p ==1 for p, 1 in zip(predictions,labels))
    return round(correct/ len(labels)* 100,2)