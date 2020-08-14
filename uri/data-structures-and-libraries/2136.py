"""
	author: Alice Francener
	problem: Friends of Habay
	url: https://www.urionlinejudge.com.br/judge/en/problems/view/2136
"""

inscricao = input()
nome, escolha = inscricao.split()

vencedor = {
    "nome": nome,
    "nome_tam": len(nome)
}

inscritos_yes = []
inscritos_no = []

while(inscricao != 'FIM'):
    nome, escolha = inscricao.split()

    if (escolha == 'YES'):
        if nome not in inscritos_yes:
            inscritos_yes.append(nome)

            if(len(nome) > vencedor["nome_tam"]):
                vencedor["nome"] = nome
                vencedor["nome_tam"] = len(nome)
    else:
        if nome not in inscritos_no:
            inscritos_no.append(nome)
    inscricao = input()

inscritos_yes = sorted(inscritos_yes)
inscritos_no = sorted(inscritos_no)

print(*inscritos_yes, sep='\n')
print(*inscritos_no, sep='\n')
print('\nAmigo do Habay:\n{}'.format(vencedor["nome"]))
