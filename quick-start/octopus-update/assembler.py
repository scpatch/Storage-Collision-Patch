from octopus.arch.evm.evm import EVM


def init(filename):
    with open(filename) as fp:
        text = fp.read()
        words = text.split()
        return words


def filter(opcode):
    if opcode == 'KECCAK256':
        return 'SHA3'
    elif opcode == 'PREVRANDAO':
        return 'DIFFICULTY'
    else:
        return opcode


def main(filename):
    opcodes = init(filename)
    evm = EVM()
    table = evm.reverse_table
    offset = 0
    res = '0x'
    while offset < len(opcodes):
        opcode = opcodes[offset]
        opcode = filter(opcode)
        details = table.get(opcode)
        if details is None:
            # opcode not in table
            if '0x' in opcode:
                # if the unknown opcode starts with 0x
                op = opcode.replace('0x', '')
                res += f"{op:0>2}"
                offset += 1
                continue
            else:
                print('Unknown opcode:', opcode)
                return
        op = details[0]
        res += f"{op:02x}"
        operand_size = details[2]
        if operand_size != 0:
            operand_width = operand_size*2
            offset += 1
            operand = opcodes[offset]
            operand = operand.replace('0x', '')
            operand = f"{operand:0>{operand_width}}"
            res += operand
        offset += 1
    return res.lower()


# res = main('/Users/py/github/evm-trace/patch/demo_test06_basic.bytecode')
# with open ('/Users/py/github/evm-trace/patch/patched_demo06_basic.bin', 'w') as f:
#     f.write(res)
# res = main('/Users/py/github/evm-trace/correctness/test.bytecode')
# with open ('/Users/py/github/evm-trace/correctness/test.bin', 'w') as f:
#     f.write(res)
