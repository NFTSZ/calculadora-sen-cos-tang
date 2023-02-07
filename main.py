from math import sin, cos, tan, radians

ang = float(input('Digite um ângulo qualquer: '))
print('O seno desse ângulo é {:.2f}, o cosseno {:.2f} e a tangente {:.2f}.'
      .format(sin(radians(ang)), cos(radians(ang)), tan(radians(ang))))
