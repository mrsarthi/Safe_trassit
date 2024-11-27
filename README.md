# Safe_trassit - Secure Transaction System

## Overview

Safe_trassit is a blockchain-based secure transaction system designed to ensure the integrity and privacy of financial transactions. The project uses Python to simulate and secure transactions, leveraging blockchain technology to guarantee immutability and prevent fraud. The system is built with scalability in mind and is aimed at users who want to ensure secure financial transfers in a decentralized and transparent environment.

The project is still in development, with additional features and improvements on the way. New functionality will continue to be added in future releases.

## Current Features

- **Transaction Simulation**: The system generates random transactions between users, ensuring that the total amount in circulation remains balanced.
- **Blockchain Implementation**: Each transaction is added to a blockchain, ensuring its integrity and transparency.
- **SHA-256 Hashing**: Transactions and blocks are hashed using SHA-256 to secure data and prevent tampering.
- **Blockchain Verification**: The blockchain integrity is verified to ensure no tampering or alteration of transaction data.
- **Genesis Block**: The first block in the blockchain is created, marking the beginning of the blockchain ledger.

## Features Coming Soon

The following features are planned for future updates:

1. **User Authentication**: Add user registration, login, and authentication features to ensure only authorized users can create or view transactions.
2. **Multi-Signature Transactions**: Implement multi-signature functionality where multiple parties must sign a transaction before it is validated and added to the blockchain.
3. **Smart Contracts**: Enable smart contracts for automating processes and validating conditions before transactions can occur.
4. **Decentralized Application (DApp)**: Integrate the blockchain system into a decentralized application that allows users to interact with the blockchain through a web interface.
5. **Transaction Fee System**: Introduce a transaction fee mechanism to incentivize miners or validators to process transactions in the blockchain network.
6. **Enhanced Blockchain Verification**: Implement a more advanced consensus algorithm (e.g., Proof of Work, Proof of Stake) to verify blocks and transactions.
7. **Real-time Transaction Monitoring**: Add the ability to monitor transactions in real time, with notifications for successful or failed transactions.
8. **Tokenization**: Introduce a token system that can be used for transactions, representing assets or currencies within the blockchain.
9. **Audit and Reporting**: Provide functionality for auditing transaction history and generating detailed reports on transactions.

## Prerequisites

- Python 3.x
- Libraries: `hashlib`, `json`, `sys`, `random`, `time`

## Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/mrsarthi/Safe_trassit.git
   cd Safe_trassit
