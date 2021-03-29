"""
Scripts do console
"""
from kt_tr import kt_tr
import click


@click.command()
@click.argument("topo")
@click.argument("fundo")
def cli(topo, fundo):
    topo = float(topo)
    fundo = float(fundo)
    range = kt_tr.range(topo, fundo)
    terco = kt_tr.terco(range)
    terco_sup = kt_tr.terco_sup(topo, terco)
    terco_inf = kt_tr.terco_inf(fundo, terco)
    metade = kt_tr.metade(range)
    meio = kt_tr.meio(topo, metade)
    alta = kt_tr.mm_alta(topo, range)
    baixa = kt_tr.mm_baixa(fundo, range)
    click.echo("%.2f" % alta)
    click.echo("%.2f" % terco_sup)
    click.echo("%.2f" % meio)
    click.echo("%.2f" % terco_inf)
    click.echo("%.2f" % baixa)
    return 0


if __name__ == "__main__":
    cli()
