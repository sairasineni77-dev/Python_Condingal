# Function Parameter
def greet(name, message='Hi'):

 return f"{message} {name}"

greeting = greet('John', "Hello")

print(greeting)




str_1 = """ Python is a high-level, interpreted programming language known for its simplicity, readability, and versatility. Created by Guido van Rossum and first released in 1991, Python's design philosophy emphasizes code readability with the notable use of significant whitespace.

Why is Python so Popular? """




def total_calc(bill_amount,tip_perc):
 total = bill_amount*(1 + 0.01*tip_perc)
 total = round(total,2)
 print(f"Please pay ${total}")


total_calc(150,20)