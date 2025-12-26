# @Q Stealth Lock Protocol
# Lead: Shakti Singh (Genesisgraphy)
# Function: AES-256 Repository Encryption

import os
from cryptography.fernet import Fernet

class QStealthLock:
    def __init__(self):
        self.key_file = "genesis.key"
        self.target_extensions = [".py"]
        self.exclude_files = ["q_stealth_lock.py", "genesis.key"]

    def generate_master_key(self):
        """Generates the unique 1-Lead key. DO NOT LOSE THIS."""
        if not os.path.exists(self.key_file):
            key = Fernet.generate_key()
            with open(self.key_file, "wb") as f:
                f.write(key)
            print(f"[@Q-STEALTH] Master Key Generated: {self.key_file}")

    def encrypt_repository(self):
        """Locks all @Q equations into encrypted blobs."""
        with open(self.key_file, "rb") as f:
            key = f.read()
        fernet = Fernet(key)

        for file in os.listdir("."):
            if any(file.endswith(ext) for ext in self.target_extensions) and file not in self.exclude_files:
                with open(file, "rb") as f:
                    original_data = f.read()
                
                encrypted_data = fernet.encrypt(original_data)
                
                # Rename to generic blob to hide identity
                new_name = file.replace(".py", ".q_blob")
                with open(new_name, "wb") as f:
                    f.write(encrypted_data)
                
                os.remove(file) # Remove the original source code
                print(f"[@Q-STEALTH] Locked: {file} -> {new_name}")

if __name__ == "__main__":
    lock = QStealthLock()
    lock.generate_master_key()
    lock.encrypt_repository()
    print("[@Q-STEALTH] SYSTEM IS NOW IN STEALTH MODE. SOURCE CODE HIDDEN.")
