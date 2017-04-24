import skidl
from skircuits.programmable.max10 import max10

@skidl.subcircuit
def pupa_form_factor(port):
    pass

@skidl.subcircuit
def pupa_circuit(port):
    fpga = max10('10m02sce144')
    fpgacct = skidl.subcircuit(fpga.circuit)
    fpgacct(port)

if __name__ == '__main__':
    port = skidl.Net()
    pupa_circuit(port)
    circuit = skidl.subcircuit(pupa_circuit)
    skidl.ERC()
    skidl.generate_netlist()
