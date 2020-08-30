"""
Dunder Name e Dunder Main =>> siginifica Doble Under __. Em Python são utilizados dundler para criar funções,
atributos, propriedades e etc utilizando Double Under para não gerar conflitos com nomes desses elementos
na programação. Para conhecer alguns Dunder iniciais digite => dir(). Quando o módulo principal é
executado diretamente a variável __name__ recebe o valor __main__. Quando o módulo é importado a
variável __name__ recebe o nome do próprio módulo sem a extensão, por exemplo __name__ lab58c_testando_dunder1

    NOTA: recomenda-se o uso de dunder quando o programa for feito para ser executado diretamente

    Dunder Name =>> __name__
    Dunder Main =>> __main__

    Na linguagem C, temos um programa da seguinte forma:
        int main() {
            return o
        }

    Na linguagem Java, temos um programa da seguinte forma:
        public static void main(String[] args) {

        }

    ATENÇÃO:    em Python, se executarmos um módulo Python diretamente na linha de comando, internamente
                o Python atribuirá à variável __name__ o valor __main__ indicando que este módulo é o
                módulo de execução principal.

    EXEMPLO:     Importando uma função de um módulo criado em aulas passadas
                    from lab58b_funcoes_com_parametros import soma_impares

                    print(f'Chamando a função soma_impares -> {soma_impares([1, 4, 8, 12, 15, 20])}')

"""
# Testando com os novos módulos criados

import lab58c_testando_dunder1
import lab58d_testando_dunder2

print(f'Usando lab58c_testando_dunder1 -> {lab58c_testando_dunder1.funcao1()}')
print(f'Usando lab58d_testando_dunder2 -> {lab58d_testando_dunder2.funcao2()}')
