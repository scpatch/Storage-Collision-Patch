from web3 import HTTPProvider, Web3
from evm_trace import TraceFrame

web3 = Web3(HTTPProvider("http://127.0.0.1:7545"))
txn_hash = "0xbc96825d71471c5750a3875a6baf2891c0ebf0f2d473ff40a9f23133b1eb85c8"
struct_logs = web3.manager.request_blocking("debug_traceTransaction", [txn_hash]).structLogs
# for item in struct_logs:
#     frame = TraceFrame.model_validate(item)
#     print(frame)
with open('log2.txt', 'w') as f:
    for item in struct_logs:
        # print(str(item))
        f.write(str(item))
        frame = TraceFrame.model_validate(item)
        print(str(frame)) 

        # if item['op'] == 'SSTORE':
        #     f.write(str(item) + '\n')

