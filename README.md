# estrutura_de_dados_algoritmos
Este repositório tem como objetivo deixar guardado todos os códigos de organização e buscas aprendidos durante o semestre na faculdade

# 1. Binary Search
   - Explique por que a lista deve estar ordenada para que o Binary Search funcione corretamente. Forneça exemplos.
   A lista precisa estar ordenada porque o algoritmo divide a busca em metades, descartando a metade que não pode conter o elemento. Sem ordenação, essa eliminação lógica falha.
Exemplo:
Lista ordenada: [1, 3, 5, 7, 9], buscar 5 → funciona.
Lista não ordenada: [7, 1, 9, 3, 5], buscar 5 → falha.


# 2. Interpolation Search  
   - Identifique casos em que o Interpolation Search é mais eficiente que o Binary Search.
  É mais eficiente que o Binary Search quando os elementos estão distribuídos uniformemente e próximos, porque estima a posição do elemento diretamente, reduzindo o número de comparações.
# 3. Jump Search
   - Compare o tempo de execução do Jump Search com o Binary Search em listas de diferentes tamanhos.
  O Jump Search é geralmente mais lento que o Binary Search em listas grandes devido ao número maior de operações de comparação. Para listas pequenas, a diferença é quase insignificante.

# 4. Exponential Search
   - Analise o desempenho do Exponential Search em listas muito grandes e pequenas.
  É eficiente para listas muito grandes porque rapidamente encontra o intervalo correto com uma complexidade O(log⁡i+log⁡n)O(\log i + \log n)O(logi+logn). Em listas pequenas, o Binary Search é geralmente mais rápido devido à sua simplicidade.

# 5. Shell Sort
   - Explique como a escolha da sequência de intervalos afeta a eficiência do algoritmo.
  A escolha da sequência de intervalos afeta o número de comparações e movimentações. Sequências como a de Knuth (h=3h+1h = 3h + 1h=3h+1) oferecem melhor desempenho em listas grandes, enquanto a sequência original de Shell é mais simples, mas menos eficiente.

# 7. Selection Sort
   - Analise o desempenho do Selection Sort em listas pequenas, médias e grandes.
Desempenho:
Listas pequenas: Desempenho aceitável devido à simplicidade O(n2)O(n^2)O(n2).
Listas médias e grandes: Ineficiente, pois faz muitas comparações e trocas independentemente da ordem inicial.

# 9. Radix Sort
   - Explique como o algoritmo lida com bases diferentes (ex.: base 10 e base 2).
  O algoritmo processa os números por "dígitos" ou "bits".
  Base 10: Ordena pelos dígitos decimais (unidades, dezenas, etc.).
  Base 2: Ordena pelos bits individuais, útil para aplicações em sistemas binários.

# 10. Quick Sort
    - Analise o desempenho do Quick Sort em listas quase ordenadas e completamente desordenadas.
  Listas quase ordenadas: Desempenho pode cair para O(n2)O(n^2)O(n2) com escolha de pivô ruim.
  Listas completamente desordenadas: Geralmente eficiente com O(nlog⁡n)O(n \log n)O(nlogn), especialmente com escolha inteligente de pivô (ex.: mediana).


# 11. Ternary Search
    - Identifique situações em que o Ternary Search seria mais eficiente que o Binary Search.
  É mais eficiente que o Binary Search em situações onde múltiplas buscas consecutivas são realizadas em intervalos grandes, reduzindo o número de comparações. Em listas pequenas, o Binary Search é mais simples e rápido.


# 12. Comparação de Algoritmos de Busca
Tempos de execução em listas de tamanhos 100, 1000 e 10,000 (em milissegundos):
![image](https://github.com/user-attachments/assets/2f524168-2905-4481-936a-3ad6469eb9c5)

Binary Search é consistente para qualquer tamanho.
Interpolation Search é mais eficiente em listas com distribuição uniforme.
Jump Search é mais lento em listas grandes devido ao número de saltos.
Exponential Search se destaca em listas muito grandes, especialmente quando o alvo está nos primeiros intervalos.


# 13. Comparação de Algoritmos de Ordenação
Tempos de execução em uma lista de 1,000 elementos (em milissegundos):

![image](https://github.com/user-attachments/assets/3dc2600e-da07-40a9-bad0-21ceb2d4d373)

Radix Sort é o mais rápido devido à ordenação baseada em dígitos.
Bucket Sort é eficiente para listas uniformemente distribuídas.
Merge Sort e Quick Sort são consistentes e adequados para listas gerais.
Selection Sort é o mais lento, indicado apenas para listas pequenas.


# 15. Busca e Ordenação em Strings
Merge Sort e Quick Sort podem ordenar palavras por ordem alfabética diretamente, pois Python lida com strings lexicograficamente.
Exemplo: Lista ["banana", "apple", "kiwi"] → Ordenada: ["apple", "banana", "kiwi"].
Binary Search funciona para localizar palavras específicas em listas ordenadas.
Exemplo: Palavra "banana" encontrada na posição 1 de ["apple", "banana", "kiwi"].


# 16. Aplicação Prática de Busca
Para encontrar um livro por ISBN, usamos Binary Search em uma lista ordenada.
Exemplo: Lista ordenada de ISBNs [123, 456, 789], busca por 456 retorna índice 1.
Busca e Ordenação em Dados Reais
Bucket Sort ordena as notas de 0 a 100 em buckets de intervalo fixo.
Exemplo: Notas [90, 75, 88, 92] → Ordenadas: [75, 88, 90, 92].
Interpolation Search encontra uma nota específica. Exemplo: Busca por 88 retorna índice 1.


# 18. Ordenação Estável e Instável
Estáveis: Merge Sort, Radix Sort, Bucket Sort (mantêm a ordem relativa dos elementos iguais).
Exemplo: Ordenar [("A", 2), ("B", 2)] por valor mantém "A" antes de "B".
Instáveis: Quick Sort, Selection Sort (podem alterar a ordem relativa).


