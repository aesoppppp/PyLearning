import random

quotes = []
quotes.append('시작이 반이다.')
quotes.append('가는말이 고와야 오는말이 곱다.')
quotes.append('어물전 망신은 꼴두기가 시킨다.')
quotes.append('사람은 사랑할때 누구나 시인이 된다.')
quotes.append('지렁이도 밟으면 꿈틀댄다.')

daily_quote = random.choice(quotes)
print('##########################')
print('#       오늘의 속담        #')
print('##########################')

print(daily_quote)
