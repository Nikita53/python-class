intercept = raw_input('enter equation of line in the form of y = mx+c')

# 'y' , 'mx+c'
rhs = intercept.split('=')[1]

# 'mx' , "c"
parts = rhs.split('+')

#part out the value of m & c
m = parts[0].replace('x','').split
c = parts[1].strip()

#print them out 
print('slope of line: {}' .format(m))
print('Y-intercept: {}' .format(c))