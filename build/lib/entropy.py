import math

def shannon_entropy(probs):
    """
    Calculates Shannon entropy for a list of probabilities.
    """
    entropy = 0
    for p in probs:
        if p > 0:
            entropy -= p * math.log2(p)
    return entropy
