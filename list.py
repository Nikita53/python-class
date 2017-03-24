names = ['john doe', 'jane doe', 'johnny turk']
names[0] = 'foo bar'
print 'names now:', names
names.append('Molly Mormon')
names.append('joe bloogs')
print 'names finally:', names
print 'last name in the list: %s' %names[-1]
joined_names = '\n'.join(names)
print '\nlist of names:'
print joined_names
