import fake_math as div_fk
import true_math as div_tr

fake_divide = div_fk.divide
true_divide = div_tr.divide

result1 = fake_divide(69, 3)
result2 = fake_divide(3, 0)
result3 = true_divide(49, 7)
result4 = true_divide(15, 0)

print(result1)
print(result2)
print(result3)
print(result4)



