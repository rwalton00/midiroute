<h2 align="center">MIDI Message Routing Tool</h2>

[![Build Status](https://dev.azure.com/rwalton00/midiroute/_apis/build/status/rwalton00.midiroute?branchName=master)](https://dev.azure.com/rwalton00/midiroute/_build/latest?definitionId=1&branchName=master)
<a href="https://github.com/psf/black"><img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg"></a>
<a href="https://pypi.org/project/midiroute/"><img alt="PyPI" src="https://img.shields.io/pypi/v/midiroute"></a>

_midiroute_ is a command line utility for routing MIDI streams between input and output ports on your computer.
_midiroute_ can route an incoming MIDI stream to multiple output ports. The stream can also be monitored in the terminal.

## Installation and usage

### Installation

_midiroute_ can be installed by running `pip install midiroute`. It requires Python 3.7.0+ to
run.

### Usage

To list the available input and output ports on your system:

```
midiroute list-ports
```

Route messages from an input to an output port with monitoring enabled:

```
midiroute run -i "Oxygen 61 0" -o "Microsoft GS Wavetable Synth 0" -m
```

### Command line options

You can list the command line options by running `midiroute --help`:

```
Usage: midiroute [OPTIONS] COMMAND [ARGS]...

  CLI entry-point.

Options:
  --help  Show this message and exit.

Commands:
  list-ports  List available input and output ports.
  run         Run the MIDI router.
```

To get help on a specific command run `midiroute <command> --help`:

```
$ midiroute run --help
Usage: midiroute run [OPTIONS]

  Run the MIDI router.

Options:
  -i, --input-port PORT_NAME    Select the input port.
  -o, --output-ports PORT_NAME  Select one or more output ports in a comma
                                separated list.
  -m, --monitor                 Enable monitoring of MIDI activity on the
                                selected ports.
  --help                        Show this message and exit.
```

## License

MIT

## Contributing to _midiroute_

Contributions to this project are more than welcome!

More details can be found in [CONTRIBUTING](CONTRIBUTING.md).

## Authors

[Rob Walton](mailto:rwalton00@gmail.com)
