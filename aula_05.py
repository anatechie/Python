def verificar_voto(idade):
    if idade < 0:
        return "Não nasceu."
    else:
        if idade in [16,17]:
            return "Voto opcional."
        else:
            if idade < 16:
                return "Não vota."
            else:
                if idade == 37:
                    return "Não vota e recebe um prêmio!"
                else:
                     if idade >= 61:
                          return "Voto opcional."
                     else:
                         if idade == 74:
                             return "Vota e recebe um prêmio!"
                         else:
                             return "Voto Obrigatorio!"
    
idade = int(input("Digite a idade do cidadão:"))
resultado = verificar_voto(idade)
print(f"A idade informada foi (idade). Resultado: {resultado}")
