"""
Esse programa faz conversões.
"""


def converte_f_para_c(temperatura_fahrenheit):
    """
    Método que converte fahrenheit para celsius

    >>> converte_f_para_c(32)
    0.0

    >>> converte_f_para_c(-40)
    -40.0
    """

    return 5 * ((temperatura_fahrenheit - 32) / 9)


def converte_c_para_f(temperatura_celsius: float):
    """
    Método que converte celsius para fahrenheit

    >>> converte_c_para_f(0)
    32.0

    >>> converte_c_para_f(10)
    50.0
    """

    return (temperatura_celsius * 1.8) + 32
