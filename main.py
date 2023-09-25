# Topshiriq 1
# 1 1 1 - 1 soat 1 minut 1 sekund
# 2 2 2 - 2 soat 2 minut 2 sekund

h1, m1, s1 = map(int, input().split())
h2, m2, s2 = map(int, input().split())
print(h2*3600 + m2*60 + s2 - h1*3600 - m1*60 - s1)
