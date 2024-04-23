# instance attribute vs class attribute.
# every object has its own namespace/dictionary.
# classes also have its own namespace/dictionary.
# class attributes are common attributes for all its instance.
# Class dictionary is readonly, whereas instance dictionary is mutable.


class BankAccount:
    apr = 1.2


print(BankAccount.__dict__['apr'])

acc_1 = BankAccount()
acc_2 = BankAccount()
print(acc_1 is not acc_2)

# coming from class its class, as the instance dictionary does not have that
print(acc_1.__dict__, acc_2.__dict__)  # empty

print(acc_1.apr, acc_2.apr)
acc_1.apr = 3.0
print(acc_1.__dict__, acc_2.__dict__)
acc_2.apr = 4.0
print(acc_1.apr, acc_2.apr, BankAccount.apr)
acc_1.type = 'saving'
print(acc_1.__dict__, acc_2.__dict__)
BankAccount.type = 'saving'
print(acc_1.__dict__, acc_2.__dict__)
print(acc_1.type, acc_2.type)
