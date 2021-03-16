from kt_tr import kt_tr
import sys


def cli():
    if len(sys.argv) > 2:
        topo = float(sys.argv[1])
        fundo = float(sys.argv[2])
    range = kt_tr.range(topo, fundo)
    terco = kt_tr.terco(range)
    terco_sup = kt_tr.terco_sup(topo, terco)
    terco_inf = kt_tr.terco_inf(fundo, terco)
    metade = kt_tr.metade(range)
    meio = kt_tr.meio(topo, metade)

    print("%.2f" % terco_sup)
    print("%.2f" % meio)
    print("%.2f" % terco_inf)
