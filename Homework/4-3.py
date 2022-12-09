dict_country_capital={}
for _ in range(10):
    country, capital=map(str,input('Input nation and its capital (. to quit) : ').split())
    if country == '.':
        break
    else:
        dict_country_capital[country]=capital
print('dict_nation_capital : ',dict_country_capital)
while True:
    nation=str(input('Input nation to find its capital (. to quit) : '))
    if nation == '.':
        break
    else:
        cap=dict_country_capital[nation]
        print(f'The capital of {nation} is {cap}')