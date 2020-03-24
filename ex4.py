# ex4.py
cars = 100.0  # 可用的小车数量。
space_in_a_car = 4.0  # 每辆车标准可载人数。
drivers = 30.0  # 可调配的司机人数。
passengers = 90.0  # 乘客总数。
cars_not_driven = cars - drivers  # 因为司机人数不够而空出来的车。
cars_driven = drivers  # 有司机驾驶的车数。
carpool_capacity = cars_driven * space_in_a_car  # 根据司机人数，可实际提供的载客量。
average_passengers_per_car = passengers / cars_driven  # 根据乘客总数，得到平均每辆车的载人数。


print('There are', cars, 'cars available.')
print('There are only', drivers, 'drivers available.')
print('There will be', cars_not_driven, 'empty cars today.')
print('We can transport', carpool_capacity, 'people today.')
print("We have", passengers, 'to carpool today.')
print('we need to put about', average_passengers_per_car, 'in each car.')
