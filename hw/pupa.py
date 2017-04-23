import skidl
import skircuits

def pupa_form_factor():
    pass

def pupa_circuit():
    fpga = skidl.SubCircuit(skircuits.programmable.max10)

if __name__ == '__main__':
    form_factor = skidl.SubCircuit(pupa_form_factor)
    circuit = skidl.SubCircuit(pupa_circuit)
    skidl.ERC()
    skidl.generate_netlist()
