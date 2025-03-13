# Exibir cabeçalho da tabela

print(" A | B | A AND B")
print("...|...|...... ")
 
 # gerar todas as condições de A e B 
for A in [0, 1]:
     for B in [0, 1]: 
          Resultado = A or B # operação  AND 
          print(" {A}  | {B} | {Resultado}")