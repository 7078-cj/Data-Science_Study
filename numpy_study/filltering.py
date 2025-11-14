import numpy as np

ages = np.array([[21, 17, 19, 20, 16, 30, 18, 65], 
                 [39, 22, 15, 99, 18, 19, 20, 21]])

teenagers = ages[ages < 18]

print(teenagers)
#[17 16 15]

adults =  ages[ (ages >= 18) & (ages < 65)]
#[21 19 20 30 18 39 22 18 19 20 21]

print(adults)

seniors = ages[ages >= 65]
#[65 99]
print(seniors)

evens = ages[ ages % 2 == 0]
print(evens)
#[20 16 30 18 22 18 20]

# preserving the dims

#(condition, array, fill) fill is to preserve the shape of the array
a = np.where( ages >= 18, ages, 0)
print(a)
#[[21  0 19 20  0 30 18 65]
#[39 22  0 99 18 19 20 21]]