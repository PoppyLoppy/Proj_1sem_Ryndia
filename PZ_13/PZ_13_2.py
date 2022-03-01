# Вариант 21.
# Из заданной строки отобразить только цифры. Использовать библиотеку string.

import string

str = 'The Great Pyramid of Khufu at Giza was built about 2700 BC, 755 feet (230 metres) long and 481 feet (147 ' \
      'metres) high.'
new_str = ''

for i in str:
    if i in string.digits:
        new_str += i
print(new_str)
