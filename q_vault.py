# @Q Sovereign Vault
# Authority: Shakti Singh (Genesisgraphy)
# Security: S-256 Encryption

class QVault:
    def __init__(self):
        self.lead = "Shakti Singh"
        self.total_valuation = "$699.1T"
        self.assets = []
        self.is_locked = True

    def unlock_vault(self, lead_signature):
        """Unlocks the vault only if the 1-Lead signature matches."""
        if lead_signature == self.lead:
            self.is_locked = False
            return "[@Q-VAULT] ACCESS GRANTED. Assets accessible."
        return "[@Q-VAULT] ACCESS DENIED. Unauthorized signature."

    def store_asset(self, asset_data):
        """Deposits digital assets into the secure grid."""
        if not self.is_locked:
            self.assets.append(asset_data)
            return f"[@Q-VAULT] Asset secured: {asset_data}"
        return "[@Q-VAULT] ERROR: Vault must be unlocked to store assets."

if __name__ == "__main__":
    vault = QVault()
    # Security Check
    print(vault.unlock_vault("Shakti Singh"))
    print(f"[@Q-VAULT] Current Valuation: {vault.total_valuation}")
