from pyevmasm import instruction_tables, disassemble_hex, disassemble_all, assemble_hex

def disassmble_bytecode(bin_file):
    bytecode = ''
    with open(bin_file, 'r') as f:
        bytecode = f.read()
    
    disassembly = disassemble_hex(bytecode)

    with open(bin_file.split('.')[0] + '.bytecode', 'w') as f:
        f.write(disassembly)


def assemble(bytecode_file):
    with open(bytecode_file, 'r') as f:
        bytecode = f.read()
        print(bytecode)
        patched_bin = assemble_hex(bytecode)
        print(patched_bin)
        with open('patch/patched_proxy.bin', 'w') as f:
            f.write(patched_bin)

DEMO_PATH = 'patch/proxy.bin'
disassmble_bytecode(DEMO_PATH)
assemble('patch/proxy.bytecode')