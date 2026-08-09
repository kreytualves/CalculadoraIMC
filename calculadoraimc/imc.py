peso = float(input('Qual é o seu peso: (Kg) '))
altura = float(input('Qual a sua altura: (m) '))
imc = peso/(altura**2)

print('\nO seu IMC é {:.1f}'.format(imc))
if imc < 18.5:
    print('Você está abaixo do peso ideal!')
elif imc >=18.5 and imc <25:
    print('Parabéns peso ideal!')
elif imc >=25 and imc <30:
    print('Sobrepeso!')
elif imc >=30 and imc <40:
    print('Obesidade!')
else:
    print('Obesidade morbida!!!')