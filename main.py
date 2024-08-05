immutable_var = (1, 2, "string", True, False)
print(immutable_var)
# immutable_var[3] = False
# Данные в кортеже неизменяемы
mutable_list = [1, 2, "string", True, False]
print(mutable_list)
mutable_list[3] = False
print(mutable_list)