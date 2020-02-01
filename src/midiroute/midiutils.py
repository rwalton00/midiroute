import mido


def list_midi_output_ports():
    print("Midi output ports:")
    print("\n".join(sorted(mido.get_output_names())))


def list_midi_input_ports():
    print("Midi input ports:")
    print("\n".join(sorted(mido.get_input_names())))
