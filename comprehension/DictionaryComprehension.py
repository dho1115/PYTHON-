if __name__ == '__main__':
   salespersonnel = [
      dict(_id="jamie1559", name="Jamie Smith", sales=3951.33, months=3),
      dict(_id="carmen135", name="Carmen Jack", sales=10579.77, months=5),
      dict(_id="aceyj155", name="Acey Johnson", sales=977.35, months=7),
      dict(_id="rickey135", name="Rickey Roberts", sales=9733.15, months=4),
      dict(_id="jojo339", name="Jojo Corrigan", sales=1995.85, months=2),
      dict(_id="kerry1", name="Kerry Cunninghan", sales=11335.7, months=6)
   ];

   def bonusStructure(AvgSalesPerMonth):
      payout = [
         dict(minSales=2995, bonus=1995.00), 
         dict(minSales=1993.99, bonus=1050.00), 
         dict(minSales=1501.99, bonus=975.00), 
         dict(minSales=1003.99, bonus=500.00), 
         dict(minSales=875.99, bonus=75.00),
         dict(minSales=0.00, bonus=0.00)
      ];
      bonus = filter(lambda x: x.get("minSales") < AvgSalesPerMonth, payout)
      return {**list(bonus)[0], 'average': AvgSalesPerMonth}; #used a filter(). Match did not work???

   # Calculate the sales per month and the bonus for each sales person based on the sales per month.

   BonusCalculator = {
      f"{val.get('_id')}"
      : 
      {
         **val, 
         "SalesPerMonth": val.get("sales")/val.get("months"), 
         "bonus": bonusStructure(val.get("sales")/val.get("months")).get("bonus")
      } 
      for val in salespersonnel
   }

   print(BonusCalculator)