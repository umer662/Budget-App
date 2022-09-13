class Category:
  # initialize objects based on different budget categories
  def __init__(self, name):
    # initializing the name of category
    self.name = name
    # initializing an instance variable
    self.ledger = []

  # The first arguments of the methods, named self, are references to the instance
  # that calls it. The caller of the method does not explicitly pass the instance
  # into self but leaves it to the Python interpreter to pass it automatically. 
  # For example, given an object plane, Python automatically converts the method
  # call plane.fly() to fly(self=plane).
  def deposit(self, amount, description=""):
    self.ledger.append({"amount": amount, "description": description})

  def withdraw(self, amount, description=""):
    if self.check_funds(amount):
      self.ledger.append({"amount": -amount, "description": description})
      return True
    else:
      return False
  
  def get_balance(self):
    available = 0
    for sum in self.ledger:
      available = available + sum["amount"]
    return available

  def transfer(self, amount, category):
    if self.check_funds(amount):
      self.ledger.append({"amount": -amount, "description": "Transfer to " + category.name})
      category.ledger.append({"amount": amount, "description": "Transfer from " + self.name})
      return True
    else: 
      return False

  def check_funds(self, amount):
    if amount > self.get_balance():
      return False
    else:
      return True
  
  # In Python, the built-in str() and repr() functions both produce a textual
  # representation of an object. The difference between str() and repr() is: 
  # The str() function returns a user-friendly description of an object. 
  # The repr() method returns a developer-friendly string representation of an object.
  def __str__(self):
    title = self.name.center(30, "*")
    items_list = []
    for item in self.ledger:
      val = (item['description'][:23]).ljust(23) + str("{:.2f}".format(item['amount'])).rjust(7)
      items_list.append(val)
    obj_str = title + "\n" + "\n".join(items_list) + "\n" + "Total: " + str(self.get_balance())
    return obj_str
    
def create_spend_chart(categories):
  ctg_items = [x.name for x in categories]
  width = len(ctg_items) * 3 + 5
  pct_chart = "Percentage spent by category\n"
  pct_spent = []
  for category in categories:
    total_credit = 0
    total_debit = 0
    for item in category.ledger:
      if item["amount"] > 0:
        total_credit = total_credit + item["amount"]
      elif item["amount"] < 0:
        total_debit = total_debit + (-item["amount"])
    if total_credit > 0:
      pct_spent.append(round((total_debit/total_credit*100)/10)*10)
  
  for bar_pct in reversed(range(0, 101, 10)):
    pct_chart += (str(bar_pct) + "|").rjust(4) + " "
    for pct in pct_spent:
      if bar_pct <= pct:
        pct_chart += "o".ljust(3, " ")
      else:
        pct_chart += " " * 3  
    pct_chart += "\n"
  pct_chart += ("-" * (width-4)).rjust(width, " ") + "\n"
  
  ctg_length = len(sorted(ctg_items, key=len)[-1])
  for idx in range(ctg_length):
    line = ""
    for ctg in ctg_items:
      try:
        line += ctg[idx]
      except:
        line += " "
      line += "  "
    pct_chart += (line).rjust(width)
    if idx < ctg_length-1:
      pct_chart += "\n"
  return pct_chart
