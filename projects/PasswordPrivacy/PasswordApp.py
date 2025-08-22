'''
*** IMPORTANT!!! ***
IF YOU DECIDE TO CLONE THIS REPO AND RUN THIS FILE (PasswordApp.py), IT MAY NOT WORK...

UNLESS YOU:

1. Create a .env in your IDE (inside your terminal, type the following: touch .env), or just manually create it on the left hand side of your IDE.
2. Once the .env is created, add the following:

mypassword="admin123"
company_revenue=39151.99
sales=1955.77
expected_growth=19993193195.99
company_info="We are expected to grow by 975% by... sometime."

3. Then, when you run Python PasswordApp.py, it should work.

This program is to simulate hiding sensitve data (passwords, api keys, fake sensitive company information like above, etc...) and then accessing this via .env library.

I deliberately left this out of my github repo (.gitignore) because, well... technically, that is what you are supposed to do!

If I were to use Netlify (https://www.netlify.com/) or Vercel (https://vercel.com/) or some other deployment platform to run this (well, maybe not Netlify since I THINK it only allows frontend applications and not Python or other backend), there would be a place for me to store all my .env keys.
'''
from dotenv import load_dotenv;
import os;

load_dotenv();

def GetCompanyFinances(myvariable):
   variable = os.getenv('mypassword', 'Please_Read_Comment');
   finances = os.getenv('company_revenue', 'Please_Read_Comment');
   sales = os.getenv('sales');
   expected_growth=os.getenv('expected_growth');
   company_info=os.getenv("company_info");
   return f"{myvariable} has been validated.\nHere is your sensitive company data:\n{dict(revenue=finances, current_sales=sales, expected_growth=expected_growth, important_messages=company_info)}" if myvariable == variable else f"{myvariable} is not the right password!!!";

# RIGHT PASSWORD SIMULATION!!!
print(GetCompanyFinances('admin123')); # Of course, in a real life simulation, I would (hopefully) NEVER put the actual password ('admin123') in the argument field. This is just a SIMULATION!!!

# WRONG PASSWORD SIMULATION!!!
print(GetCompanyFinances("I_AM_TRYING_TO_GET_SENSIVE_DATA")); # 'I_AM_TRYING_TO_GET_SENSIVE_DATA' is NOT the right password.
