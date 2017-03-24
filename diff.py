social = raw_input('enter marks for social: ')
science = raw_input('enter marks for science: ')
math = raw_input('enter marks for math: ')
english = raw_input('enter marks for english: ')
nepali = raw_input('enter marks for nepali: ')

total = float(social) + float(science) + float(math) + float(english) + float(nepali)
print'total marks,total'
percentage = (total/ 500 ) *100
print('total {}' .format(total) )
print('percentage= {:.2f} %' .format(percentage))

