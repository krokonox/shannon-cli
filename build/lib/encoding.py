import math

def shannon_encoding(prob):
    """
    Calculates the Shannon encoding for a set of symbol probabilities.
    """
    # Parse the symbol probabilities from the input string
    symbol_probs = {}
    for item in prob.split(" "):
        symbol, prob = item.split(':')
        symbol_probs[symbol] = float(prob)

    # Check that the probabilities sum to 1
    if abs(sum(symbol_probs.values()) - 1) > 1e-6:
        raise ValueError('Symbol probabilities must sum to 1')

    # Calculate the information content of each symbol
    symbol_info = {symbol: math.log2(1/p)
                   for symbol, p in symbol_probs.items()}

    # Calculate the optimal number of bits to use for each symbol
    symbol_bits = {symbol: math.ceil(info)
                   for symbol, info in symbol_info.items()}

    # Generate the Shannon encoding
    encoding = {}
    for symbol in symbol_probs:
        code = ''
        for i in range(symbol_bits[symbol]):
            code += '1' if (len(code) == 0 or code[-1] == '0') else '0'
        encoding[symbol] = code

    # Print the encoding
    encoding_string = ""
    for symbol, code in encoding.items():
        encoding_string += (f'{symbol}: {code}')

    return encoding_string