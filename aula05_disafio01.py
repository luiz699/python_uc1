SENHA_CORRETA="1234" 

idade=int(input("informe a sua idade : "))
senha=input("informe a senha").lower()


if (idade>=18)and (SENHA_CORRETA==senha) :
    print ("!!!! acesso liberado !!!")
       
else:   
    print("acesso negado . senha !!!")


