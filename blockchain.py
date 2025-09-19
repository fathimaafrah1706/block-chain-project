import hashlib
import datetime

# Function to calculate hash of a block
def calculate_hash(block):
    block_string = str(block["index"]) + block["timestamp"] + block["data"] + block["previous_hash"]
    return hashlib.sha256(block_string.encode()).hexdigest()

# Function to check if blockchain is valid
def is_chain_valid(chain):
    for i in range(1, len(chain)):
        current_block = chain[i]
        previous_block = chain[i-1]

        # Check if current block's hash is correct
        if current_block["hash"] != calculate_hash(current_block):
            return False

        # Check if current block's previous_hash matches previous block's hash
        if current_block["previous_hash"] != previous_block["hash"]:
            return False

    return True

# Create blockchain
blockchain = []

# Genesis block
genesis_block = {
    "index": 0,
    "timestamp": str(datetime.datetime.now()),
    "data": "Student 1",
    "previous_hash": "0",
    "hash": ""
}
genesis_block["hash"] = calculate_hash(genesis_block)
blockchain.append(genesis_block)

# Second block
second_block = {
    "index": 1,
    "timestamp": str(datetime.datetime.now()),
    "data": "Student 2",
    "previous_hash": blockchain[-1]["hash"],
    "hash": ""
}
second_block["hash"] = calculate_hash(second_block)
blockchain.append(second_block)

# Print blockchain
for block in blockchain:
    print(block)

# Check blockchain validity (should be True)
print("\nBlockchain valid?", is_chain_valid(blockchain))

# Tamper with the second block
blockchain[1]["data"] = "Hacker Changed Student 2"

# Check blockchain validity again (should be False)
print("Blockchain valid after tampering?", is_chain_valid(blockchain))
