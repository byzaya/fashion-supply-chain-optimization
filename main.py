# импортирование необходимых библиотек
from pulp import *

# инициализация модели
model = LpProblem("Fashion_Supply_Chain_Optimization", LpMinimize)

# объявление переменных
x1 = LpVariable("Production_of_Product_1", 50)
x2 = LpVariable("Production_of_Product_2", 75)
x3 = LpVariable("Production_of_Product_3", 100)
y1 = LpVariable("Storage_of_Product_1", 20)
y2 = LpVariable("Storage_of Product_2", 40)
y3 = LpVariable("Storage_of_Product_3", 60)
z1 = LpVariable("Delivery_of_Product_1_to_Retailer_1", 15)
z2 = LpVariable("Delivery_of_Product_1_to_Retailer 2", 10)
z3 = LpVariable("Delivery_of_Product_2_to_Retailer 1", 30)
z4 = LpVariable("Delivery_of_Product_2_to_Retailer 2", 40)
z5 = LpVariable("Delivery_of_Product_3_to_Retailer 1", 50)
z6 = LpVariable("Delivery_of_Product_3_to_Retailer 2", 75)

# объявление целевой функции
model += 1000 * x1 + 1200 * x2 + 1500 * x3 + 10 * y1 + 8 * y2 + 12 * y3 + 20 * z1 + 22 * z2 + 18 * z3 + 20 * z4 + 25 * z5 + 30 * z6, "Total Cost"

# ограничения на производство
model += x1 <= 100
model += x2 <= 150
model += x3 <= 200

# ограничения на складирование
model += y1 <= 50
model += y2 <= 100
model += y3 <= 150

# ограничения на доставку к ритейлерам
model += z1 + z2 <= 50
model += z3 + z4 <= 100
model += z5 + z6 <= 150

# ограничения на доступность товаров для ритейлеров
model += z1 + z3 + z5 <= x1 + y1
model += z2 + z4 + z6 <= x2 + y2
model += z1 + z2 + z3 + z4 + z5 + z6 <= x3 + y3

# решение задачи линейного программирования
model.solve()

# вывод результатов оптимизации
print("Production of Product 1: ", x1.value())
print("Production of Product 2: ", x2.value())
print("Production of Product 3: ", x3.value())
print("Storage of Product 1: ", y1.value())
print("Storage of Product 2: ", y2.value())
print("Storage of Product 3: ", y3.value())
print("Delivery of Product 1 to Retailer 1: ", z1.value())
print("Delivery of Product 1 to Retailer 2: ", z2.value())
print("Delivery of Product 2 to Retailer 1: ", z3.value())
print("Delivery of Product 2 to Retailer 2: ", z4.value())
print("Delivery of Product 3 to Retailer 1: ", z5.value())
print("Delivery of Product 3 to Retailer 2: ", z6.value())
print("Total Cost: ", value(model.objective))
