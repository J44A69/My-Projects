# Hecho por Jhonnatan Andres

# <<Este proyecto se basa en una clase de python que se puede usar para crear y manipular una cuenta de banco personal>>

# <<Acepta depositos>>
# <<Permite retiros>>
# <<Muestra el balance y detalles de la cuenta>>


class BankAccount(object):
  balance = 0

  # Datos 
  def __init__(self, name):
    self.name = name

# Muestra el balance
  def __repr__(self):
     return "%s's account. Balance: $%.2f" % (self.name, self.balance)

  def show_balance(self):
    print("%s's account. Balance: $%.2f" % (self.name, self.balance))

# Depositos
  def deposit(self, amount):
    if amount <= 0:
      return 'Invalid amount sent!'
    else:
     print("You deposited %s your balance is $%.2f")
     self.balance += amount
     self.show_balance()

# Retiros      
  def withdraw(self, amount):
    if amount > balance:
      return 'you dont have enough balance'
    else:
     print("%s's account. Balance: $%.2f")
     self.balance -= amount
     self.show_balance()

# Llamadas
my_account = BankAccount("Jhonnatan")
print(my_account)