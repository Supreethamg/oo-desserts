"""Dessert classes."""


class Cupcake:
    """A cupcake."""
    cache ={}
    def __init__(self,name,flavor,price):
      self.name = name
      self.flavor = flavor
      self.price = price
      self.qty = 0
      self.cache[self.name] = self


    def add_stock(self,amount):
      self.qty =self.qty + amount


    def sell(self,amount):
      if self.qty > 0:
       self.qty = self.qty - amount
       if self.qty < 0:
         self.qty = 0
      else:
        print('Sorry, these cupcakes are sold out')

    @staticmethod
    def scale_recipe(ingredients,amount):
      ing = []
      for ingredient in ingredients:
        ing.append((ingredient[0], ingredient[1] *amount))
      return ing

    @classmethod
    def get(cls,name):
      if name in cls.cache:
        return cls.cache.get(name)
      else:
        print("Sorry, that cupcake doesn't exist")
        


    def __repr__(self):
        """Human-readable printout for debugging."""

        return f'<Cupcake name="{self.name}" qty={self.qty}>'




class Brownie(Cupcake):

  def __init__(self,name,price):
    super().__init__(self,name,"chocolate",price)




if __name__ == '__main__':
    import doctest

    result = doctest.testfile('doctests.py',
                              report=False,
                              optionflags=(
                                  doctest.REPORT_ONLY_FIRST_FAILURE
                              ))
    doctest.master.summarize(1)
    if result.failed == 0:
        print('ALL TESTS PASSED')
