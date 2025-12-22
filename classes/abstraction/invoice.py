from abc import ABC, abstractmethod;

class Invoice(ABC):
   '''
   An abstract class inheriting from ABC. total method must be included. companyDetails does not need to be included.
   '''
   @staticmethod
   def companyDetails(revenue, **kwargs):
      '''
      companyDetails is NOT an abstractmethod, so you do NOT need to include this in the class that will be inheriting from Invoice.
      '''
      return {**kwargs, "revenue": revenue};

   @abstractmethod #This is the abstract method.
   def total(self): pass

class Company(Invoice):
   def __init__(self, revenue, *items) -> None:
      super().__init__()
      self.items = items;
      self._revenue = revenue;

   @property
   def revenue(self):
      return self._revenue;
   
   @revenue.setter
   def revenue(self, other):
      self._revenue = other;
   
   def total(self):
      totalForEach = list(map(lambda x: round(x.get("each") * x.get("qty"), 3), self.items));

      return sum(totalForEach)

ABC_Packing = Company(579935, dict(item="shoes", each=105.99, qty=5), dict(item="potato chips", each=3.75, qty=31), dict(item="sparking water", each=7.99, qty=51));

ABC_Packing.revenue = 199797019

details = ABC_Packing.companyDetails(ABC_Packing.revenue, name="ABC Packing", CEO="Jamie Smith");

print("TOTAL:", ABC_Packing.total());
print("COMPANY DETAILS:", details);