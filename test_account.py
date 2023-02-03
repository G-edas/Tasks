import unittest
from account import BankAccount 


class test_account(unittest.TestCase):
    

    def test_successful_deposit(self):
        bank_account = BankAccount('Gedas', 0)
        bank_account.deposit(20)
        self.assertEqual(bank_account.balance, 20)
         
    def test_successful_withdraw(self):
        bank_account = BankAccount('Gedas', 120)
        bank_account.withdraw(120)
        self.assertEqual(bank_account.balance, 0)
        
    def test_failed_withdraw(self):
        bank_account = BankAccount('Gedas', 120)
        self.assertEqual(bank_account.withdraw(121), "Not enough amout of money in bank account.")

if __name__ == '__main__':
    unittest.main()