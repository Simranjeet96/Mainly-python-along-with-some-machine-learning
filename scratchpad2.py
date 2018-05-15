# Dictionary of dictionaries
europe = { 'spain': { 'capital':'madrid', 'population':46.77 },
           'france': { 'capital':'paris', 'population':66.03 },
           'germany': { 'capital':'berlin', 'population':80.62 },
           'norway': { 'capital':'oslo', 'population':5.084 } }


# Create sub-dictionary data
'''data={}
for i in europe:
    data[i['capital']]=i['population']
'''
for i in europe:
	print(i['capital'])
# Add data to europe under key 'italy'
print(europe['spain']['capital'])
# Print europe
