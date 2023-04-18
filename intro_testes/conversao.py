"""
Esse programa faz conversões.
"""

def conversao(temperatura_fahrenheit):

    """
    Método que converte

    >>> conversao(32)
    0.0

    >>> conversao(-40)
    -40.0
    """

    return 5 * ((temperatura_fahrenheit - 32) / 9)