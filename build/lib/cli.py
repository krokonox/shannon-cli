import click
from entropy import shannon_entropy
from encoding import shannon_encoding

@click.command()
@click.argument('probs', nargs=-1, type=float)
def calculate_entropy(probs):
    """
    Calculates Shannon entropy for a list of probabilities.
    """
    entropy = shannon_entropy(probs)
    click.echo(f"Shannon entropy: {entropy:.2f}")


@click.command()
@click.argument('probs', nargs=-1, type=float)
def calculate_shannon_encoding(probs):
    """
    Calculates Shannon encoding for a list of probabilities.
    """
    encoding = shannon_encoding(probs)
    click.echo(f"Shannon entropy: {encoding}")
