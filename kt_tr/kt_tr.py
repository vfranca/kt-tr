"""
Arquivo de definições
"""
topo = 0.0
fundo = 0.0


def range(topo, fundo):
    return abs(topo - fundo)


def terco(range):
    return range / 3


def terco_sup(topo, terco):
    return topo - terco


def terco_inf(fundo, terco):
    return fundo + terco


def metade(range):
    return range / 2


def meio(topo, metade):
    return topo - metade


def mm_alta(topo, range):
    return topo + range


def mm_baixa(fundo, range):
    return fundo - range
