import time

start_time = time.time()  # მიმდინარე დრო

number = 1  # რიცხვის დასაწყისი

while number <= 100:  # ციკლი გამოიტანს რიცხვებს 1-დან 100-მდე ჩათვლით
    print(number)  # მიმდინარე რიცხვის ბეჭდვა
    number = number + 1  # რიცხვის გაზრდა 1-ით

    # შეამოწმებს არ არის თუ არა 10 წუთი გასული
    if time.time() - start_time >= 600:    
        break




    even_sum = 0
num = 0

print("Even numbers from 0 to 10:")

while num <= 10:
    print(num)
    even_sum += num
    num += 2

print("Sum of even numbers from 0 to 10:", even_sum)