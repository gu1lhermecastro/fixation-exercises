length = float(input('Informe o comprimento da cozinha: '))
width = float(input('Informe a largura da cozinha: '))
height = float(input('Informe a altura da cozinha: '))

area = (((2 * length) + (2 * width)) * height)
print(area)

boxTiles = float(input('Informe quantos metros quadrados possui cada caixa: '))


totalBox = (area/boxTiles)

print('Serão necessárias', totalBox, 'para cobrir a cozinha.')
