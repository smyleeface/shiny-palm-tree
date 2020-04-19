from datetime import datetime

today = datetime.today()

# It is Month DD, YYYY HH:MM:SS
print(today.strftime('It is %B %d, %Y %H:%m:%S'))

# It is Mth DD, YYY HH:MM:SS
print(today.strftime('It is %b %d, %Y %H:%m:%S'))

# It is Month DD, YYY HH:MM:SSAM
print(today.strftime('It is %B %d, %Y %I:%m:%S%p'))

