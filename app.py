from modulo import *

if __name__ == "__main__":
    # instancia objeto da subclasse
    h = Filho('','','','',0.0,0.0,'')

    # entrada de dados
    h.nome = input('Informe o nome: ')
    h.email = input('Informe o e-mail: ')
    h.profissao = input('Informe o profissao: ')
    h.olhos = input('Informe a cor olhos: ')
    h.peso = float(input('Informe o peso em kg: ').replace(',','.'))
    h.altura = float(input('Informe a altura em metros: ').replace(',','.'))
    h.cor_cabelo = input('Informe a cor do cabelo: ')

    # saida de dados
    print('\n')
    h.exibir_cartao_visitas()
    h.exibir_fisico()
    print('\n')
    

    