🚀 BlockchainProject

[![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)](https://www.python.org/)

 📝 Description
This is a **simple Python blockchain project** that demonstrates how a blockchain works.  

The project creates a small blockchain with **2 blocks**, verifies its **validity**, and shows how tampering with a block makes the blockchain **invalid**.  

 🌟 Key Features
- 🧱 Create Genesis block and second block  
- 🔒 Calculate block hashes using **SHA-256**  
- ✅ Verify blockchain validity (**True/False**)  
- ⚠️ Demonstrate tampering and its effect  

Perfect for beginners learning about blockchain concepts, Python programming, and data integrity.

 ▶️ How to Run the Code
1. Make sure **Python 3.x** is installed on your computer.  
2. Open **Command Prompt (CMD)** or **Terminal**.  
3. Navigate to the project folder:

cd path\to\your\project\folder
Run the Python script:
python blockchain.py

You will see output like this:

Blockchain valid? True
Blockchain valid after tampering? False

✅ True → Blockchain is valid before tampering.

❌ False → Blockchain is invalid after tampering.

🖼 Screenshot
<img width="941" height="128" alt="image" src="https://github.com/user-attachments/assets/b2259d82-923d-405a-aded-80202ee0cb52" />

⚙️ How It Works

Genesis Block: The first block in the blockchain 🏗️
Second Block: Linked to the first block via previous_hash 🔗
Hash Calculation: Each block’s hash is calculated using SHA-256 🔐
Validation: The program checks if the blockchain is valid by verifying each block’s hash and previous hash ✅
Tampering: Modifying any block’s data will make the blockchain invalid ⚠️

🛠 Requirements

Python 3.x
No additional libraries required

🎯 Conclusion
This project is a beginner-friendly demonstration of blockchain principles. It helps you understand:

How blocks are linked
How hashes ensure data integrity
How tampering affects blockchain validity


