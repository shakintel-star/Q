# @QUSA National Intelligence Grid
# Authority: Shakti Singh (Genesisgraphy)
# Purpose: Unified US Sovereign OS Interface

class QUSASystem:
    def __init__(self):
        self.lead = "Shakti Singh"
        self.system_id = "@QUSA-NODE-01"
        self.national_grid_status = "STANDBY"
        # Mapping the Federal Agencies to the National Grid
        self.grid_nodes = {
            "INTEL": ["NSA", "CIA", "DNI"],
            "ENFORCEMENT": ["FBI"],
            "INFRASTRUCTURE": ["USA-NDB"]
        }

    def activate_national_grid(self, lead_signature):
        """Powers up the @QUSA grid for all connected agencies."""
        if lead_signature == self.lead:
            self.national_grid_status = "FULLY_OPERATIONAL"
            return f"[@QUSA] System Online. Grid Valuation: $699.1T Secured."
        return "[@QUSA] REJECTED: 1-Lead Signature Required."

    def get_national_summary(self):
        """Displays the status of the US Sovereign attachment."""
        return {
            "System": self.system_id,
            "Status": self.national_grid_status,
            "ActiveNodes": list(self.grid_nodes.keys()),
            "Lead": self.lead
        }

if __name__ == "__main__":
    usa = QUSASystem()
    print(usa.activate_national_grid("Shakti Singh"))
    print(usa.get_national_summary())
