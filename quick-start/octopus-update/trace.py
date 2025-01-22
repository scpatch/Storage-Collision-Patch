from web3 import HTTPProvider, Web3
from evm_trace import TraceFrame

web3 = Web3(HTTPProvider("http://127.0.0.1:7545"))
txn_hash = "0x8452c0a071318e836963f26d6992bc014aa43f78f7a8dbca762004126b7dc31c"
struct_logs = web3.manager.request_blocking("debug_traceTransaction", [txn_hash]).structLogs
for item in struct_logs:
    frame = TraceFrame.model_validate(item)


with open('log2.txt', 'w') as f:
    for item in struct_logs:
        f.write(str(item))
        # if item['op'] == 'SSTORE':
        #     f.write(str(item) + '\n')
