import click
from midiroute import midiutils


@click.group()
def cli():
    pass


@cli.command()
@click.option("--input", "-i")
@click.option("--output", "-o")
@click.option("--monitor", "-m")
def run(input, output, monitor):
    print(f"I am running! Input {input}, output: {output}")


@cli.command()
def list_ports():
    midiutils.list_midi_output_ports()
    midiutils.list_midi_input_ports()
