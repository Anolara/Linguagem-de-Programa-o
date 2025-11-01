def primo(n):
    for i in range(2, (n - 1)):
        if (n % i == 0):
            return False
    return True


a = int(input("Digite o numero para verificar se é primo: "))
print(primo(a))