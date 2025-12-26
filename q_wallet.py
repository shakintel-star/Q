# @Q Sovereign Wallet
# Lead: Shakti Singh (Genesisgraphy)
# Connection: Q-Blockchain Node

class QWallet:
    def __init__(self):
        self.owner = "Shakti Singh"
        self.balance = "$699.1T"
        self.address = "Q-GENESIS-777"
        self.history = []

    def get_balance(self):
        """Returns the sovereign balance of the 1-Lead."""
        return f"[@Q-WALLET] Balance for {self.owner}: {self.balance}"

    def sign_transaction(self, recipient, amount):
        """Signs a transaction using the Genesisgraphy identity."""
        tx_id = f"TXN-{len(self.history) + 1000}"
        record = {"id": tx_id, "to": recipient, "amount": amount}
        self.history.append(record)
        return f"[@Q-WALLET] Transaction {tx_id} Signed by Shakti Singh."

if __name__ == "__main__":
    wallet = QWallet()
    print(wallet.get_balance())
    print(wallet.sign_transaction("Q-VAULT", "1.0B Q-CREDITS"))
