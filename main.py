
def max_min_select(arr, inicio, fim):
    """
    Encontra o maior e o menor elemento em uma sub-lista arr[inicio...fim]
    usando a abordagem de divisão e conquista.

    Parâmetros:
    arr (list): A lista de números.
    inicio (int): O índice inicial da sub-lista.
    fim (int): O índice final da sub-lista.

    Retorna:
    tuple: Uma tupla contendo (menor_elemento, maior_elemento).
    """
    # Caso base 1: Se há apenas um elemento na sub-lista.
    if inicio == fim:
        return arr[inicio], arr[inicio]

    # Caso base 2: Se há dois elementos na sub-lista.
    if fim == inicio + 1:
        if arr[inicio] > arr[fim]:
            return arr[fim], arr[inicio]
        else:
            return arr[inicio], arr[fim]

    # Etapa de Divisão: Encontra o ponto médio para dividir a lista.
    meio = (inicio + fim) // 2

    # Conquista: Chama recursivamente para as duas metades.
    menor_esq, maior_esq = max_min_select(arr, inicio, meio)
    menor_dir, maior_dir = max_min_select(arr, meio + 1, fim)

    # Etapa de Combinação: Combina os resultados das duas metades.
    menor_final = min(menor_esq, menor_dir)
    maior_final = max(maior_esq, maior_dir)

    return menor_final, maior_final

# --- execução principal para teste ---
if __name__ == "__main__":
    print("--- Teste do Algoritmo MaxMin Select ---")
    
    # exemplo para teste
    sequencia = [10, -1, 25, 50, 3, 99, 42, -5, 0, 77]
    
    if not sequencia:
        print("A lista está vazia.")
    else:
        # Chama a função principal passando a lista inteira (da posição 0 ao final)
        menor, maior = max_min_select(sequencia, 0, len(sequencia) - 1)
        
        print(f"\nSequência de números: {sequencia}")
        print(f"Menor elemento encontrado: {menor}")
        print(f"Maior elemento encontrado: {maior}")

    # exemplo de teste adicional
    sequencia_2 = [3, 5, 1, 9, 4, 8]
    if not sequencia_2:
        print("\nA lista 2 está vazia.")
    else:
        menor_2, maior_2 = max_min_select(sequencia_2, 0, len(sequencia_2) - 1)
        print(f"\nSequência de números: {sequencia_2}")
        print(f"Menor elemento encontrado: {menor_2}")
        print(f"Maior elemento encontrado: {maior_2}")