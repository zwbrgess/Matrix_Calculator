import os

def matrix_print(matrix):
    for row in matrix:
        print("")
        for element in row:
            print(element, end=" ")

def matrix_add_boolean(A, B):
    final = []
    for row in range(len(A)):
        final.append([])
        for element in range(len(A[row])):
            if A[row][element] == 0 and B[row][element] == 0:
                final[row].append(0)        
            else:
                final[row].append(1)
    return final

def matrix_multiply_boolean(A, B):
    final = []
    for lst in A:
        final.append([])

    # turning B's lists from matrix rows to matrix columns
    B_copy = B
    B = []
    for ele in B_copy[0]:
        B.append([])
    for i in range(len(B_copy[0])):
        for lst in B_copy:
            B[i].append(lst[i])

    # iterate through each list
    for x in range(len(A)):
        for y in range(len(B)):
            sum = 0
            for z in range(len(A[x])):
                A_ele = A[x][z]
                B_ele = B[y][z]
                product = A_ele * B_ele
                sum += product
            if sum >= 1:
                final[x].append(1)
            else:
                final[x].append(0)
    return final

def matrix_power(A, n):
    A_raised = A
    for i in range(n - 1):
        A_raised = matrix_multiply_boolean(A_raised, A)
    return A_raised

def transitive_closure(A):
    iterations = len(A)
    for i in range(2, iterations + 1):
        new_A = matrix_power(A, i)
        A = matrix_add_boolean(A, new_A)
    return A

def get_matrix(i):
    print(f"Start of Matrix #{i}:")
    print(f"\nPlease Enter Matrix #{i} dimensions:")
    x = int(input("x Dimension: "))
    y = int(input("y Dimension: "))

    # matrix initialization
    matrix = []
    print("\nEnter a series of 1s and 0s (", end="")
    for j in range(x - 1):
        print("X ", end="")
    print("X)")
    for i in range(y):
        matrix.append([])
        num_lst = input(f"---> ").split()

        # Length Error & Type Error
        while (len(num_lst) != x):
            print("\nOops! Too many numbers, try again (", end="")
            for j in range(x - 1):
                print("X ", end="")
            print("X)")
            num_lst = input(f"---> ").split()

        for num in num_lst:
            matrix[i].append(int(num))


    '''
    num = "awkdjhad"
    matrix = [[]]
    index = 0
    while True:
        num = input("Enter a Number (1 or 0): ")
        while num != "1" and num != "0" and num != "done" and num != "next":
            num = input("Oops, try again (1 or 0): ")
        if num == "done":
            break
        if num == "next":
            index += 1
            matrix.append([])
            continue
        num = int(num)
        matrix[index].append(num)
    '''
    return matrix, x, y
    


if __name__ == "__main__":
    os.system('cls')
    print("\nWelcome to Zach's Boolean Matrix Calculator!")
    print("Remember! This is a Boolean Calculator, 1s and 0s")
    print("\nBut, first things first, would you like to make your own matrices?")
    foo = input("If so, hit enter, otherwise type 'base1' or 'base2' to test my base cases: ")

    print()
    if foo == "":
        m1, x1, y1 = get_matrix(1)
        print()
        m2, x2, y2 = get_matrix(2)
    elif foo == "base1":
        m1 = [ [0, 1, 1, 0], [0, 0, 1, 1], [1, 0, 0, 0], [1, 1, 0, 1] ]
        x1, y1 = 4, 4
        m2 = [ [1, 0, 0, 0], [1, 1, 0, 1], [0, 1, 1, 0], [0, 0, 1, 1] ]
        x2, y2 = 4, 4
    elif foo == "base2":
        m1 = [ [0, 1, 1], [1, 0, 1] ]
        x1, y1 = 3, 2
        m2 = [ [1, 0], [0, 0], [0, 1] ]
        x1, y1 = 2, 3
    
    os.system('cls')
    print("\nHere are your matrices!")
    matrix_print(m1)
    print()
    matrix_print(m2)


    print("\n\nAlrighty, what would you like to do?")

    while True:
        print("\nOptions:")
        print("Type 'Add' to add the matrices")
        print("Type 'Multiply' to multiply the matrices")
        print("Type 'Power' to raise the first matrix to a power")
        print("Type 'Closure' to view the Transitive Closure of the first matrix")
        print("Type 'Help' for a few rules")
        o = input("\n--> ")
        if o == "Add":
            print("\nMatrix Boolean Addition:")
            matrix_print(matrix_add_boolean(m1, m2))
        elif o == "Multiply":
            print("\nMatrix Boolean Multiplication:")
            matrix_print(matrix_multiply_boolean(m1, m2))
        elif o == "Power":
            n = int(input("Enter the power you would like to raise to: "))
            print(f"\nMatrix Boolean ^{n}:")
            matrix_print(matrix_power(m1, n))
        elif o == "Closure":
            print("\nMatrix Transitive Closure: ")
            matrix_print(transitive_closure(m1))
        elif o == "Exit":
            break
        else:
            print("Oops, thats not an option, try again")
            continue
        print("\n\nFeel free to pick another option, or type 'Exit' to finish")
