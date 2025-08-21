def CompanyInfo(_id):
   CompanyStatements = dict(admin123=dict(revenue=15977.95, sales=3915.11, forecast=1993351051.99)) #closure???
   try:
      if not CompanyStatements.get(_id): raise Exception(f"Sorry, {_id}, but you are NOT authorized to view sensitive company statments!!!");
      return f"Hello, {_id}... here are your companyStatements: \n{CompanyStatements}."
   except Exception as EXC:
      return EXC

print(CompanyInfo('admin123fdsfdsa'));
print("=========");
print(CompanyInfo('admin123'));