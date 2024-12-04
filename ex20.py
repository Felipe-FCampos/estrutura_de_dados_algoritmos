def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

def interpolation_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high and arr[low] <= target <= arr[high]:
        pos = low + ((target - arr[low]) * (high - low) // (arr[high] - arr[low]))
        if arr[pos] == target:
            return pos
        elif arr[pos] < target:
            low = pos + 1
        else:
            high = pos - 1
    return -1

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = merge_sort(arr[:mid])
        right = merge_sort(arr[mid:])
        return merge(left, right)
    return arr

def merge(left, right):
    result = []
    while left and right:
        if left[0] < right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    result.extend(left or right)
    return result

def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

def main():
    print("Escolha a ação:")
    print("1. Ordenar lista")
    print("2. Procurar elemento")
    choice = int(input("Digite sua escolha (1/2): "))
    
    if choice == 1:
        print("Escolha o algoritmo de ordenação:")
        print("1. Quick Sort")
        print("2. Merge Sort")
        print("3. Selection Sort")
        sort_choice = int(input("Digite sua escolha (1/2/3): "))
        
        arr = list(map(int, input("Digite os elementos da lista separados por espaço: ").split()))
        
        if sort_choice == 1:
            print("Lista ordenada (Quick Sort):", quick_sort(arr))
        elif sort_choice == 2:
            print("Lista ordenada (Merge Sort):", merge_sort(arr))
        elif sort_choice == 3:
            print("Lista ordenada (Selection Sort):", selection_sort(arr))
        else:
            print("Escolha inválida.")
    
    elif choice == 2:
        print("Escolha o algoritmo de busca:")
        print("1. Binary Search")
        print("2. Interpolation Search")
        search_choice = int(input("Digite sua escolha (1/2): "))
        
        arr = sorted(list(map(int, input("Digite os elementos da lista separados por espaço: ").split())))
        target = int(input("Digite o elemento a ser procurado: "))
        
        if search_choice == 1:
            result = binary_search(arr, target)
            print(f"Elemento {'encontrado na posição ' + str(result) if result != -1 else 'não encontrado'} (Binary Search).")
        elif search_choice == 2:
            result = interpolation_search(arr, target)
            print(f"Elemento {'encontrado na posição ' + str(result) if result != -1 else 'não encontrado'} (Interpolation Search).")
        else:
            print("Escolha inválida.")
    else:
        print("Escolha inválida.")

main()