"""
GIL => Python Global Interpreter Lock

    O QUE É ISSO?   - O GIL é um mutex (ou lock) que permite que apenas uma thread tome conta do interpretador Pyhton
                    - Isso significa que somente uma thread pode estar em um estado de execução em qualquer
                    instante de tempo
                    - O impacto do GIL não é comumente visível para desenvolvedores que executam programas
                    single-thread, mas pode ser uma dor de cabeça para programadores que precisam de tempo
                    de resposta em códigos multi-thread
                    - Desde de que o GIL permite apenas uma thread a ser executada, mesmo em computadores
                    multi-threads com arquitetura que permite utilizar mais de uma CPU ou core, o GIL tem
                    ganhado reputação como um recurso "indecente" do Python
                    - Neste laboratório vamos aprender como o GIL afeta a performance do seu programa Python
                    e também como podemos mitigar o impacto no nosso código.
                    - Python utiliza refernce counting para gerenciamento de memória
                    - Isso significa que para cada objeto criado Python mantém uma variável de contangem de
                    referência que guarda quantas referências apontam para o objeto. Quando o contador de
                    referências chega a zero, a memória ocupada é liberada
                    - Para melhor entender o reference counting (quantas instânicas/variáveis apontam para
                    um memso objeto), abra um terminal Python e digite o código a seguir:
                        > > > import sys
                        > > > a = []
                        > > > b = a
                        > > > sys.getrefcount(a)
                    -> deverá retornar 3 (três referencias ao mesmo objeto, sendo: a -> 1, b -> 2 e getrefcount() -> 3
                    - O problema é que essa forma de gerenciamento de memória utilizando reference couting precisa
                    de proteção para um funômeno chamado "race conditions" (quando duas ou mais threads
                    disputam o mesmo recurso), onde duas threads aumentam ou diminuem seu valor simultaneamente
                    - Se isso acontecer, poderá causar problemas de memória que nunca é liberada, ou ainda pior,
                    liberação incorreta de memória enquanto ainda existe referência para o objeto
                    - E isso pode causar crashs ou outros bugs esquisitos no seu programa Python
                    - Este reference counting pode ser mantido seguro adicionando 'locks' (quando você define um lock,
                    siginfica que você irá usar o recurso naquele momento) em toda estrutura de dados que são
                    compartilhadas via threads. Desta forma eles não são mofificados de forma inconsistente
                    - O problema é que adicionar 'locks' em cada objeto ou grupo de objetos significa que múltiplos
                    locks irão existir, e isso irá causar outro problema - Deadlocks (deadlocks só podem existir se
                    existe mais de um lock). Outro efeito colateral seria decaimento da performance causada pela
                    repetida aquisição e liberação dos locks
                    - O GIL aplica na regra de execução de qualquer código Python o single lock previnindo qualquer
                    deadlock, o que por outro lado tranforma qualquer código Python em single-thread
                    - Vale mencionar que o GIL apesar de ser usado também em outras linguagens de programação, como
                    o Ruby, não é a única solução
                    - Algumas lingugens evitam o uso do GIL para gerenciamento de memória em thread utilizando
                    abordagens diferentes do refernce counting que o Python utiliza
                    - Por exemplo, uma das aboradagens que outras linguagens utilizam é o compilador JIT -
                    Just in Time, como o JAVA
                    - Dos exemplos pudemos observr que mesmo utilizando multi-thread o tempo de finalização embora
                    melhor ainda pode ser muito otimizado
                    - A utilização do GIL prejudica a real utilização de multi-cores nas máquinas, o que torna os
                    projetos Python lentos em alguns casos, pois são tratados com threads únicos
                    Por outro lado, o GIL torna as aplicações single-threads muito performáticas, e a grande
                    maioria das aplicações não precisam do recurso de muti-threads
                    - Como lidar com o GIL?
                    - Caso você tenha problemas com o GIL, você pode utilizar multi-processing ao invés
                    de multithreading
                    - Utilizando processos ao invés de threads cada processo Python ganha seu próprio interprestador
                    Python e espaço em memória. Desta forma o GIL não será problema e sim parte da solução
                    - Que fique claro que multi-processing são mais pesados que multi-threading
                    - Ou seja, lembre-se que para cada processo, teremos uma ambiente Python próprio
                    - Interpretadores alternativos Python
                    - Conforme mencionado antes, python possui múltiplas implementações dentre as principais:
                        - CPython -> C
                        - Jython -> Java
                        - IronPython -> C#
                        - Pypy -> escrito em Python
                    - O GIL só existe na implementação original (CPython). Então se seu programa estiver rodando
                    em outra implementação, você não terá o problema que o GIL traz.
                    - Para aprofundar seus estudos em Python consulte o site: https://edabit.com

"""
# Como exemplo, vamos ver o impacto em programas Python multi-thead
# Para isso, vamos abrir um novo lab para este teste
