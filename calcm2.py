#n1 = informaçao das placas (tamanho)AxL
#n2 = informaçao da lugar (tamanho)AxL

#parede/placa = quantas peças vai usar

# printa a informação ^ 


n1 = float(input('Digite a altura da sua placa em metro : '))

n2 = float(input('Digite a largura da sua placa em metro: '))

n3 = float(input('Digite a altura da sua parede em metro : '))

n4 = float(input('Digite a largura da sua parede em metro: '))

class Metro:
    def __init__(self,altura, largura,):
        self.altura = altura
        self.largura = largura
        self.metro2 = self.largura*self.altura
#############################################################

parede = Metro(n3,n4)
plaquinhas = Metro(n1,n2)
test = parede.metro2/plaquinhas.metro2


print(f'sua parede tem {parede.metro2:.2f}M² e suas placas tem {plaquinhas.metro2:.2f}M² voce vai precisar de {test:.1f} placas')