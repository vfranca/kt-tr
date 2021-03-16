import sys


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


if __name__ == "__main__":
    if len(sys.argv) > 2:
        topo = float(sys.argv[1])
        fundo = float(sys.argv[2])
    range = range(topo, fundo)
    terco = terco(range)
    terco_sup = terco_sup(topo, terco)
    terco_inf = terco_inf(fundo, terco)
    metade = metade(range)
    meio = meio(topo, metade)

    print("%.2f" % terco_sup)
    print("%.2f" % meio)
    print("%.2f" % terco_inf)
