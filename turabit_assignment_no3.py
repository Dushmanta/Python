heads = int(input('please enter heads count:'))
legs = int(input('Please enter legs count:'))
if legs % 2 !=0 or heads ==0 or heads > legs:
    print('Error in input')
else:
    r = int((legs + (-2*heads))/2)
    c = int(heads - r)
    print('Number of rabbits and  chickens are : ','{} and {}'.format(c,r))
