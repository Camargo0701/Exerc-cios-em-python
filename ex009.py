import math
ang= float(input('Digite o ângulo que você deseja: '))
seno= math.sin(math.radians(ang))
cos= math.cos(math.radians(ang))
tg= math.tan(math.radians(ang))
print('O ângulo do seno {} vale {:.2f}'.format(ang, seno))
print('O ângulo do cosseno {} vale {:.2f}'.format(ang, cos))
print('O ângulo tangente {} vale {:.2f}'.format(ang, tg))