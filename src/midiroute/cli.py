"""Command line interface module."""
import click
from midiroute import midiutils


@click.group()
def cli() -> None:
    """CLI entry-point."""
    pass


@cli.command()
@click.option("--input", "-i")
@click.option("--output", "-o")
@click.option("--monitor", "-m")
def run(input: str, output: str, monitor: str) -> None:
    """'run' command handler."""
    print(f"I am running! Input {input}, output: {output}")


@cli.command()
@click.option("--filter-opt", "-f")
def list_ports(filter_opt: str) -> None:
    """'list-ports' command handler."""
    if "out" not in filter_opt:
        midiutils.list_midi_output_ports()
    if "in" not in filter_opt:
        midiutils.list_midi_input_ports()
