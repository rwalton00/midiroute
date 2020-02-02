"""Command line interface module."""

import asyncio

from typing import Any

import click
import tabulate

from midiroute import midiutils


@click.group()
def cli() -> None:
    """CLI entry-point."""
    pass


@cli.command()
@click.option("--input-port", "-i")
@click.option("--output-ports", "-o")
@click.option("--monitor", "-m", is_flag=True)
def run(input_port: str, output_ports: Any, monitor: bool) -> None:
    """'run' command handler."""
    output_ports = output_ports.split(",")
    asyncio.run(midiutils.stream(input_port, output_ports, monitor))


@cli.command()
def list_ports() -> None:
    """'list-ports' command handler."""
    inports = midiutils.list_input_port_names()
    outports = midiutils.list_output_port_names()
    print(tabulate.tabulate(list(zip(inports, outports)), headers=["Input", "Output"]))
