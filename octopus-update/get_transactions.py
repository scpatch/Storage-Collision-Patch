import requests

def get_transactions(contract_address):
    api_endpoint = "http://api.etherscan.io/api"
    params = {
        'module': 'account',
        'action': 'txlist',
        'address': contract_address,
        'sort': 'asc',
        'apikey': 'YourApiKeyToken'
    }
    response = requests.get(api_endpoint, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        return {'status': 'Failed', 'message': 'Could not fetch transactions'}

def analyze_transactions(transactions):
    for tx in transactions.get('result', []):
        if tx['input'] == '0x' or len(tx['input']) <= 10:
            tx_type = 'Normal Transaction'
        else:
            tx_type = 'Function Call'
            print(tx)
        print(f"Transaction Hash: {tx['hash']} | Type: {tx_type}")

contract_address = "0x435940c749b012f53885a1f56dea68a1eb8e05d7"
transactions = get_transactions(contract_address)
analyze_transactions(transactions)
