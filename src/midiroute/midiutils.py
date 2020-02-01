"""MIDI utilities."""
import mido


def list_midi_output_ports() -> None:
    """Print the available MIDI output ports."""
    print("Midi output ports:")
    print("\n".join(sorted(mido.get_output_names())))


def list_midi_input_ports() -> None:
    """Print the available MIDI input ports."""
    print("Midi input ports:")
    print("\n".join(sorted(mido.get_input_names())))
