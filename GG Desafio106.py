#Estratégia 1

def projeto():
    from time import sleep
    val = 0
    while True:  #########
        print(f'''\033[;30;43m{'~'*27}  
  {'SISTEMA DE AJUDA PyHELP'}  
{'~'*27}\033[m''')
        val = input('Função ou Biblioteca > ').strip().lower()  #########
        if val == 'fim':  #########
            break  #########
        print(f"""\033[0;30;44m{'~'*(36+len(val))} 
  Acessando o manual do comando '{val}'   
{'~'*(36+len(val))} \033[m""")
        sleep(2.5) 
        print(f'''\033[7m
        {help(val)}
              \033[m''')
        sleep(2.5)
    print(f'''\033[;30;41m{'~'*13}
  ATÉ LOGO!  
{'~'*13}\033[m''')


#Projeto Principal
projeto()
