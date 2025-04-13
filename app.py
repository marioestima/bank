bank = []

def dep():
    value = int(input('insira o valor de deposito: '))
    bank.append(value)

def levantamento():
    lev_value = int(input('insira um valor para levantamento: '))
    if len(bank) <= 0:
      print('sorry but you account is empty! :(')
    for value in range(len(bank)):
       atual_value =  bank[value] - lev_value
       print('valor atual', atual_value)

def user_account():
    total = 0

    if len(bank) != 0:
        total = sum(bank)
        print('o total na sua conta é de: ', total)
    else: 
        print('o saldo na sua é vazio', str(total))
            
while True:
    print('==============================')
    print('|    simple bank system     | ')
    print('==============================')
    print('Escolha uma Opção')
    print('')
    print('')
    print('1-depositar')
    print('2-levantar')
    print('3-saldo na conta')
    print('4-sair')
   
    option = int(input('>'))


    if option == 1:
        dep() 
    elif option == 2:
        levantamento()
    elif option == 3:
        user_account()
    else:
       print('saindo....')   
       break  
         

   

    
