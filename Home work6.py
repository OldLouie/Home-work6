my_dict = {'Egor': 1999, 'Veronika': 2000, 'Masha': 1996}
print(my_dict)
print('Existing value:', my_dict['Egor'])
print('Not existing value:', my_dict.get('Elena'))
my_dict.update({'Sasha': 1997,
                'Misha': 1998})
print(my_dict)
my_dict.pop('Veronika')
print(my_dict)

my_set = {1.54, 2, 3.96, 4.58, 'apple'}
print(my_set)
my_set.add((55, 83, 'coconut'))
my_set.remove(3.96) # Или еще один способ через "discard"/ оба рабочих..
#my_set.discard(1.54)
print(my_set)