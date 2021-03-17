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
    click.echo("%.2f" % terco_sup)
    click.echo("%.2f" % meio)
    click.echo("%.2f" % terco_inf)


if __name__ == "__main__":
    cli()
