import csv
from web3 import Web3

# Connect to a Geth node
w3 = Web3(Web3.HTTPProvider('http://localhost:8545'))  # Update with your Geth node's URL

if w3.isConnected():
    print("Connected to Geth node")
else:
    print("Not connected to Geth node. Check your node's URL.")

# Get the latest block number
latest_block_number = w3.eth.blockNumber

# Create a CSV file to store all transactions
csv_filename = 'all_transactions.csv'
with open(csv_filename, 'w', newline='') as csv_file:
    fieldnames = ['Block Number', 'Transaction Index', 'Hash', 'From', 'To', 'Value', 'Gas Price', 'Gas', 'Input Data', 'V', 'R', 'S']
    csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    
    csv_writer.writeheader()

    # Iterate through all blocks and transactions
    for block_number in range(latest_block_number + 1):
        block = w3.eth.getBlock(block_number, full_transactions=True)
        transactions = block.transactions
        
        for tx_hash in transactions:
            tx = w3.eth.getTransaction(tx_hash)
            csv_writer.writerow({
                'Block Number': block_number,
                'Transaction Index': tx['transactionIndex'],
                'Hash': tx['hash'].hex(),
                'From': tx['from'],
                'To': tx['to'],
                'Value': tx['value'],
                'Gas Price': tx['gasPrice'],
                'Gas': tx['gas'],
                'Input Data': tx['input'],
                'V': tx['v'],
                'R': tx['r'],
                'S': tx['s']
            })

print(f"All transactions have been saved to {csv_filename}")
