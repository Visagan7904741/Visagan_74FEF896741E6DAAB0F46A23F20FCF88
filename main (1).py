
def isleapyear(year):
  if ( year % 4 == 0 and year % 100 !=0) or year % 400==0:
    return Ture
  else:
    return False
    
year = int(input ("enter a year:"))

if isleapyear (year):
  print ( '{} is a leap yedef isleapyear(year):
  if ( year % 4 == 0 and year % 100 !=0) or year % 400==0:
    return Ture
  else:
    return False
    
year = int(input ("enter a year:"))

if isleapyear (year):
  print ( '{} is a leap year.'.format (year))
else:
  print ('{} is a not a leap year.'. format (year))
  ar.'.format (year))
else:
  print ('{} is a not a leap year.'. format (year))
  