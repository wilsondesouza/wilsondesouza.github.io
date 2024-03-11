# Programa feito com a intenção de calcular e  descobrir o dano causado por cada personagem de Don't Starve Together

# Feito por Wilson Júnior.
from time import sleep as s
import Dicionários
import os

class Calculadora():
    print ('"Jogatina dos Putos" apresenta...')
    s(1)
    print ('Calculadora de Dano - Dont Starve Together')
    s(1)

# Método construtor #
    def __init__(self):
        self.personagem_jogado= ""
        self.arma_usada= ""
        self.municao = ""
        self.dano_personagem = 1
        self.dano_arma = 1
        self.buff = 1

    # Limpar Tela #
    def cls(self):
        os.system('cls' if os.name=='nt' else 'clear')


# Usuário informará seu personagem, o programa realizará a busca no dicionário "multiplicador" e passará para a próxima parte
    def personagem(self):  
        s(1)
        self.personagem_jogado = input('Com qual personagem do capeta você está jogando?''\n').replace(' ', '').title()
        if self.personagem_jogado in Dicionários.multiplicador:
            s(1)
            print(f'Sério que você escolheu {self.personagem_jogado}? Espero que saiba o que está fazendo.')
            if self.personagem_jogado == 'Wolfgang':
                s(1)
                print('O dia tem que tá pago pro Wolfão aumentar seu dano')
            elif self.personagem_jogado == 'Wx-78':
                s(1)
                print('O dano do robozinho vai ser o mesmo com ou sem o chip de Eletricidade')    
        else:
            s(1)
            print('Coloque um personagem jogável')
            while self.personagem_jogado not in Dicionários.multiplicador:
                tentativa = input('Quer tentar de novo?''\n').replace(' ', '').title()
                if tentativa == 'Sim':
                    calculadora.personagem()
                    break
                else:
                    s(1)
                    print('Ok. Tchau')
                    quit()

# O usuário informará sua arma, o programa buscará no dicionário "weapon" e passará para a próxima parte
    def arma(self):
        self.arma_usada = input('Qual arma você está usando?''\n').strip().title()
        if self.arma_usada in Dicionários.weapon:
            s(1)
            print(f'Logo a {self.arma_usada}? Tinha arma melhor não?')
            if self.arma_usada == 'Battle Spear' and self.personagem_jogado == 'Wigfrid':
                s(1)
                print('"All the wörlds a stage. För me!" ')
            elif self.arma_usada == 'Dark Sword' and self.personagem_jogado == 'Maxwell':
                s(1)
                print('"Freedom suits me."')
            elif self.arma_usada == 'Ham Bat' and self.personagem_jogado == 'Wolfgang':
                s(1)
                print('"I am mighty! No one is mightier!"')
            elif self.arma_usada == 'Slingshot':
                s(1)
                if self.personagem_jogado != 'Walter':
                    s(1)
                    print(f'Peraí.....{self.personagem_jogado} não consegue equipar a {self.arma_usada}. Só o Waltinho consegue usar ela')
                    while self.personagem_jogado != 'Walter':
                        calculadora.arma()
                        break 
                else:
                    s(1)
                    print('"A Pinetree Pioneer is always prepared!"')
        else:        
            s(1)
            print('Essa arma não existe ou eu não a conheço. Tente alguma outra')
            while self.arma_usada not in Dicionários.weapon:
                tentativa = input('Quer tentar de novo?''\n').replace(' ', '').title()
                if tentativa == "Sim":
                    calculadora.arma()
                    break
                else:
                    print('Ok. Tchau')
                    s(1)
                    quit()

# O programa usará os valores correspondentes às strings informadas pelo usuário para fazer uma simples operação de multiplicação
    def dano(self):
        for key in Dicionários.multiplicador.keys():
            if key.startswith(self.personagem_jogado):
                self.dano_personagem = (Dicionários.multiplicador[key])  
                if self.personagem_jogado == 'Wolfgang':
                    variação = input('Wolfão foi pra academia?"S/N"''\n').replace(' ', '').title()
                    s(1)
                    if variação == 'N':
                        self.dano_personagem = (Dicionários.multiplicador['Wolfgang'][0])
                    elif variação == 'S':
                        self.dano_personagem = (Dicionários.multiplicador['Wolfgang'][1])
        for key in Dicionários.weapon.keys():
            if key.startswith(self.arma_usada):
                self.dano_arma = (Dicionários.weapon[key])
                if self.arma_usada == 'Slingshot':
                    self.munição = input('Qual munição você usará?("Pedra", "Ouro" ou "Mármore")''\n').replace(' ', '').title()
                    s(1)
                    if self.munição == 'Pedra':
                        self.dano_arma = (Dicionários.weapon['Slingshot'][0])
                    elif self.munição == 'Ouro':
                        self.dano_arma = (Dicionários.weapon['Slingshot'][1])
                    elif self.munição == 'Mármore':
                        self.dano_arma = (Dicionários.weapon['Slingshot'][2])
        self.dano_base = self.dano_personagem * self.dano_arma
        s(1)
        #progress bar
        print (f'Seu dano base é {self.dano_base}.')
    
# Após essa operação, finalmente o programa será capaz de apontar quanto de dano o personagem causará com um ou mais buffs.
    def buffs(self):
        print('Existem dois buffs de comida que podem complementar o dano causado: Volt Goat Chaud-Froid e Chili Flakes')
        s(1)
        pergunta_buff = input('Qual buff você quer ver aplicado sobre o seu dano? ("volt", "chili" ou "ambos")?''\n').replace(' ', '').title()
        #progress bar
        if pergunta_buff == 'Volt':
            variação = input('O monstro estará seco ou "Wet"?"(1,2)"''\n').replace(' ', '')
            s(1)
            match variação:
                case '1':
                    volt = self.dano_base * 1.5
                    self.buff = volt
                    print(f'Seu dano com a Volt Goat Chaud-Froid é {self.buff:.2f}')
                case '2':
                    volt2 = self.dano_base * 2.5
                    self.buff = volt2
                    print(f'Seu dano com a Volt Goat Chaud-Froid  se o mob estiver "Wet" será {self.buff:.2f}')
            s(1)
        elif pergunta_buff == 'Chili':
            chili = self.dano_base * 1.2
            self.buff = chili
            s(1)
            print(f'Seu dano com o buff da Chili Flakes passa a ser de {self.buff:.2f}.')
        elif pergunta_buff == 'Ambos':
            variação = input('O monstro estará seco ou "Wet"?"(1,2)"''\n').replace(' ', '')
            s(1)
            match variação:
                case '1':
                    ambos = (self.dano_base * 1.5) * 1.2
                    self.buff = ambos
                    print(f'Seu dano com os dois buffs será de {self.buff:.2f}')
                case '2':
                    ambos2 = self.dano_base * 3.0
                    self.buff = ambos2
                    print(f'Seu dano com os dois buffs será de {self.buff:.2f} se o mob estiver "Wet"')
            s(1)  
        s(1)
        tentativa = input('Quer testar outro buff?''\n').replace(' ', '').title()
        if tentativa== 'Sim':
            s(1) 
            print('Entendido')
            calculadora.buffs()

# Nesta função, o usuário poderá descobrir quantos hits eles precisará acertar para derrotar cada um dos boss monster do game
    def bosses(self):
        boss_usuario = input('Qual boss você irá enfrentar?''\n').strip().title()
        boss = boss_usuario
        while boss_usuario in Dicionários.chefes:
            s(1)
            print (f'{boss_usuario}? Boa sorte!') 
            for key in Dicionários.chefes.keys():
                if key.startswith(boss_usuario):
                    boss = (Dicionários.chefes[key])
                    s(1)
                    if boss_usuario == 'Celestial Champion':
                        variação = input (f'Qual fase do {boss_usuario} você irá enfrentar? "(1,2,3)"''\n').replace(' ', '')      
                        match variação:
                            case '1':
                                boss = (Dicionários.chefes['Celestial Champion'][0])
                                hit_boss = boss
                                hit_boss = hit_boss / self.buff
                                s(1)                    
                            case '2':
                                boss = (Dicionários.chefes['Celestial Champion'][1])
                                hit_boss = boss
                                hit_boss = hit_boss / self.buff
                                s(1)
                            case '3':
                                boss = (Dicionários.chefes['Celestial Champion'][2])
                                hit_boss = boss
                                hit_boss = hit_boss / self.buff
                                s(1)
                    if boss_usuario == 'Klaus':
                        variação = input (f'Qual fase do {boss_usuario} você irá enfrentar? "(1,2)"''\n').replace(' ', '') 
                        match variação:
                            case '1':
                                boss = (Dicionários.chefes['Klaus'][0])
                                hit_boss = boss
                                hit_boss = hit_boss / self.buff
                                s(1)                        
                            case '2':
                                boss = (Dicionários.chefes['Klaus'][1])
                                hit_boss = boss
                                hit_boss = hit_boss / self.buff
                                s(1)
                    if boss_usuario == 'Klaus Enraged':
                        variação = input (f'Qual fase do {boss_usuario} você irá enfrentar? "(1,2)"''\n').replace(' ', '') 
                        match variação:
                            case '1':
                                boss = (Dicionários.chefes['Klaus Enraged'][0])
                                hit_boss = boss
                                hit_boss = hit_boss / self.buff
                                s(1)                    
                            case '2':
                                boss = (Dicionários.chefes['Klaus Enraged'][1])
                                hit_boss = boss
                                hit_boss = hit_boss / self.buff
                                s(1)                          
                    if boss_usuario == 'Reanimated Skeleton':
                        variação = input (f'Qual fase do {boss_usuario} você irá enfrentar? "(1,2,3)"''\n').replace(' ', '')      
                        match variação:
                            case '1':
                                boss = (Dicionários.chefes['Reanimated Skeleton'][0])
                                hit_boss = boss
                                hit_boss = hit_boss / self.buff
                                s(1)                   
                            case '2':
                                boss = (Dicionários.chefes['Reanimated Skeleton'][1])
                                hit_boss = boss
                                hit_boss = hit_boss / self.buff
                                s(1)
                            case '3':
                                boss = (Dicionários.chefes['Reanimated Skeleton'][2])
                                hit_boss = boss
                                hit_boss = hit_boss / self.buff
                                s(1)    
                    if boss_usuario == 'Toadstool':
                        variação = input (f'Qual fase do {boss_usuario} você irá enfrentar? "(1,2)"''\n').replace(' ', '') 
                        match variação:
                            case '1':
                                boss = (Dicionários.chefes['Toadstool'][0])
                                hit_boss = boss
                                hit_boss = hit_boss / self.buff
                                s(1)                       
                            case '2':
                                boss = (Dicionários.chefes['Toadstool'][1])
                                hit_boss = boss
                                hit_boss = hit_boss / self.buff
                                s(1)      
                    if boss_usuario == 'Treeguard':
                        variação = input (f'Qual fase do {boss_usuario} você irá enfrentar? "(1,2,3)"''\n').replace(' ', '')      
                        match variação:
                            case '1':
                                boss = (Dicionários.chefes['Treeguard'][0])
                                hit_boss = boss
                                hit_boss = hit_boss / self.buff
                                s(1)                         
                            case '2':
                                boss = (Dicionários.chefes['Treeguard'][1])
                                hit_boss = boss
                                hit_boss = hit_boss / self.buff
                                s(1)
                            case '3':
                                boss = (Dicionários.chefes['Treeguard'][2])
                                hit_boss = boss
                                hit_boss = hit_boss / self.buff
                                s(1)
                    if boss_usuario == 'Shadow Pieces':
                        variação = input (f'Qual fase do {boss_usuario} você irá enfrentar? "(1,2,3)"''\n').replace(' ', '') 
                        match variação:
                            case '1':
                                boss = (Dicionários.chefes['Shadow Pieces'][0])
                                hit_boss = boss
                                boss2 = (Dicionários.chefes['Shadow Pieces'][3])
                                hit_boss2 = boss2
                                boss3 = (Dicionários.chefes['Shadow Pieces'][6])
                                hit_boss3 = boss3
                                hit_boss = hit_boss / self.buff
                                hit_boss2 = hit_boss2 / self.buff
                                hit_boss3 = hit_boss3 / self.buff
                                s(1)                         
                            case '2':
                                boss = (Dicionários.chefes['Shadow Pieces'][1])
                                hit_boss = boss
                                boss2 = (Dicionários.chefes['Shadow Pieces'][4])
                                hit_boss2 = boss2
                                boss3 = (Dicionários.chefes['Shadow Pieces'][7])
                                hit_boss3 = boss3
                                hit_boss = hit_boss / self.buff
                                hit_boss2 = hit_boss2 / self.buff
                                hit_boss3 = hit_boss3 / self.buff
                                s(1)        
                            case '3':
                                boss = (Dicionários.chefes['Shadow Pieces'][2])
                                hit_boss = boss
                                boss2 = (Dicionários.chefes['Shadow Pieces'][5])
                                hit_boss2 = boss2
                                boss3 = (Dicionários.chefes['Shadow Pieces'][8])
                                hit_boss3 = boss3
                                hit_boss = hit_boss / self.buff
                                hit_boss2 = hit_boss2 / self.buff
                                hit_boss3 = hit_boss3 / self.buff
                                s(1)
                        print (f'Você precisará acertar {hit_boss:.2f} para derrotar o Shadow Knight, {hit_boss2:.2f} para derrotar o Shadow Bishop e {hit_boss:.2f} para derrotar o Shadow Rook.')
                    hit_boss = boss
                    hit_boss = hit_boss / self.buff
                    s(1)
                    if boss_usuario != 'Shadow Pieces':
                        print (f'Você precisará acertar {hit_boss:.2f} para derrotar {boss_usuario}')
                    tentativa_boss = input('Quer escolher outro boss?''\n').replace(' ', '').title()    
                    if tentativa_boss == 'Sim':
                        calculadora.bosses()
                    else:
                        calculadora.novamente()
        while boss_usuario not in Dicionários.chefes:
            s(1)
            tentativa_boss = input('Esse boss não existe. Quer tentar de novo?''\n').replace(' ', '').title()
            if tentativa_boss == 'Sim':
                calculadora.bosses()
            else:
                calculadora.novamente()

# O usuário será questinado se deseja reiniciar a calculadora. Se sim, o programa retornará ao início.
    def novamente(self):
        while True:
            s(1)
            tentativa = input('Quer reiniciar a calculadora?''\n').replace(' ', '').title()
            if tentativa == 'Sim':
                print ('Ok. Vamos lá!')
                s(2)
                calculadora.cls()
                main()
            else:
                print('Ok. Obrigado por usar a calculadora de dano da "Jogatina dos Putos"!')
                s(1)
                quit()      
# Fim do programa. Houve um singelo agredecimento seguido do encerramento.  

# Instâncias da classe e objetos #
calculadora = Calculadora()
def main():
    calculadora.personagem()
    calculadora.arma()
    calculadora.dano()
    s(2)
    calculadora.cls()
    calculadora.buffs()
    calculadora.bosses()

if __name__ == "__main__":
    main()
# Instâncias da classe e objetos #