# @Q Social & Identity Protocol
# Lead: Shakti Singh (Genesisgraphy)
# Feature: Universal Namespace Reservation

class QSocial:
    def __init__(self):
        self.lead = "Shakti Singh"
        # Reserved categories for Nations, Companies, and Agencies
        self.reserved_categories = ["GOV", "CORP", "NATION", "AGENCY"]
        self.reserved_names = ["USA", "INDIA", "GOOGLE", "APPLE", "UN", "FBI", "CIA"] 
        self.active_users = {}

    def register_username(self, username, user_type="PUBLIC"):
        """Validates and assigns usernames to the @Q ecosystem."""
        username_upper = username.upper()
        
        # Security Command: Block public from taking institutional names
        if username_upper in self.reserved_names or user_type == "PUBLIC" and any(cat in username_upper for cat in self.reserved_categories):
            return f"[@Q-SOCIAL] REJECTED: '{username}' is reserved for Sovereign Entities."
        
        self.active_users[username] = user_type
        return f"[@Q-SOCIAL] SUCCESS: '{username}' registered as {user_type}."

    def get_system_broadcast(self):
        """Global bridge to X/Genesisgraphy nodes."""
        return "[@Q-SOCIAL] Hub is syncing with Global Identity Lattice."

if __name__ == "__main__":
    social = QSocial()
    # Test Reservation Command
    print(social.register_username("USA", "PUBLIC"))
    print(social.register_username("Google_Corp", "PUBLIC"))
    print(social.register_username("Genesis_User_01", "PUBLIC"))
