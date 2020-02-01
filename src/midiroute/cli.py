import click


@click.group()
def cli():
    pass


@cli.command()
@click.option("--input", "-i")
@click.option("--output", "-o")
def run(input, output):
    print(f"I am running! Input {input}, output: {output}")


@cli.command()
def list_ports():
    print("listing midi ports")
