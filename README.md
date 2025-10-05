# Projeto  individual 2 - MaxMin Select 📝

Implementação do algoritmo de seleção simultânea do maior e do menor elementos utilizando a abordagem de divisão e conquista.

**CURSO:** ENGENHARIA DE SOFTWARE  
**DISCIPLINA:** FUNDAMENTOS DE PROJETO E ANÁLISE DE ALGORITMOS  
**PROFESSOR:** João Paulo Carneiro Aramuni

---

### 🎯 Objetivo do Projeto

Desenvolver um programa em Python que implemente o algoritmo **MaxMin Select**. O objetivo é encontrar, de forma simultânea e eficiente, o maior e o menor elemento de uma sequência de números, aplicando a técnica de **divisão e conquista** para reduzir o número total de comparações.

---

### ⚙️ Lógica do Algoritmo Implementado

O algoritmo foi implementado de forma recursiva no arquivo `main.py`, seguindo a estratégia de divisão e conquista. A lógica principal se baseia nos seguintes passos:

-   **Dividir**: O problema de encontrar o mínimo e o máximo em uma lista de `n` elementos é quebrado em dois subproblemas de tamanho `n/2`. Isso é feito recursivamente até que os subproblemas sejam pequenos o suficiente para serem resolvidos diretamente.

-   **Conquistar**: A solução dos subproblemas é encontrada nos casos base da recursão:
    1.  Se a sub-lista contém apenas **um elemento**, ele é ao mesmo tempo o valor mínimo e máximo.
    2.  Se a sub-lista contém **dois elementos**, uma única comparação define qual é o mínimo e qual é o máximo.

-   **Combinar**: Os resultados (pares de `min` e `max`) retornados pelas chamadas recursivas das duas metades são combinados para encontrar a solução final. Isso requer apenas duas comparações adicionais: uma para encontrar o mínimo global e outra para o máximo global.

---

### 🚀 Como Executar o Projeto

Para executar o projeto localmente, basta seguir os passos abaixo.

1.  **Clone o repositório:**
    ```bash
    # Substitua [seu-usuario] pelo seu nome de usuário do GitHub
    git clone [https://github.com/](https://github.com/)[seu-usuario]/trabalho_individual_2_FPAA.git
    ```

2.  **Navegue até o diretório do projeto:**
    ```bash
    cd trabalho_individual_2_FPAA
    ```

3.  **Execute o script Python:**
    O programa não possui dependências externas.
    ```bash
    python3 main.py
    ```
    O terminal exibirá as sequências de teste e os valores mínimo e máximo encontrados para cada uma delas.

---

### 📈 Relatório Técnico de Análise

#### Análise de Complexidade por Contagem de Operações

A análise foca no número de comparações, que é a operação dominante.

-   A relação de recorrência para o número de comparações $T(n)$ é:
    $$ T(n) = 2T(n/2) + 2 $$
    -   $2T(n/2)$: Duas chamadas recursivas para subproblemas de metade do tamanho.
    -   $+ 2$: Duas comparações na etapa de combinação para encontrar o mínimo e o máximo finais.

-   A resolução dessa recorrência mostra que o número total de comparações é aproximadamente $1.5n - 2$.
-   Isso resulta em uma complexidade de tempo linear, **$O(n)$**.

#### Análise de Complexidade pelo Teorema Mestre

Aplicamos o Teorema Mestre à recorrência $T(n)=2T(n/2)+O(1)$ , onde $T(n)=a \cdot T(n/b)+f(n)$.

1.  **Identificação dos parâmetros**:
    -   $a = 2$ (número de subproblemas).
    -   $b = 2$ (fator de redução do tamanho da entrada).
    -   $f(n) = O(1)$ (custo constante do trabalho de combinação).

2.  **Cálculo de $\log_b a$**:
    -   $p = \log_b a = \log_2 2 = 1$.

3.  **Enquadramento no Teorema Mestre**:
    -   Comparamos $f(n) = O(1)$ com $n^{\log_b a} = n^1$.
    -   Como $f(n) = O(n^{1-\epsilon})$ para $\epsilon = 1$, a recorrência se enquadra no **Caso 1** do teorema.

4.  **Solução Assintótica**:
    -   Pelo Caso 1, a solução é $T(n) = \Theta(n^{\log_b a})$.
    -   Portanto, $T(n) = \Theta(n^1) = \Theta(n)$.

Ambos os métodos confirmam que a complexidade de tempo do algoritmo é **$O(n)$**.

---

### 🖼️ (Ponto Extra) Diagrama Visual da Recursão

Para ilustrar o funcionamento do algoritmo, foi criado um diagrama que demonstra visualmente o processo de divisão e conquista. O diagrama está localizado na pasta `assets/`.

![Diagrama Visual da Recursão](assets/diagramaMaxMin.png)

O diagrama detalha:
1.  Como a lista original é dividida recursivamente em subproblemas menores.
2.  Como os resultados (pares de mínimo e máximo) são combinados em cada nível da recursão.
3.  Os níveis da árvore de recursão e o número de comparações em cada etapa.
