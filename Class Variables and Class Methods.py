class Bank:
    bank_name = "Default Bank"
    
    def __init__(self, branch):
        self.branch = branch
    
    def display_info(self):
        print(f"Bank: {Bank.bank_name}, Branch: {self.branch}")
    
    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name

if __name__ == "__main__":
    bank1 = Bank("Downtown Branch")
    bank2 = Bank("Uptown Branch")
    bank3 = Bank("City Center Branch")
    
    print("Initial bank information:")
    bank1.display_info()
    bank2.display_info()
    bank3.display_info()
    
    print("\nChanging bank name to 'Global Bank'...")
    Bank.change_bank_name("Global Bank")
    
    print("\nBank information after name change:")
    bank1.display_info()
    bank2.display_info()
    bank3.display_info()
    
    print("\nCreating a new branch after name change:")
    bank4 = Bank("New Branch")
    bank4.display_info() 