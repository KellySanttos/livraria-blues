print("Bem-vindo à livraria Blues\n")

books = ["O pequeno princípe", "A Cabana", "Deus não está morto", "A coragem de ser imperfeito"]

choice = input("Deseja ver os livros disponíveis? (sim/não): ")

if choice == "sim":
    print("\nAqui está a lista:\n ")

    for index,book in enumerate(books):
        print("{} - {}.".format(index+1,book))
    print("---------------------------------------------------------")

    option = (int(input("Qual livro você deseja? ")))

    if option == 1:
        print("-----------------------------------")
        print("Livro escolhido: {}.".format(books[option-1]))

    elif option == 2:
        print("-------------------------------")
        print("Livro escolhido: {}.".format(books[option-1]))

    elif option == 3:
        print("-------------------------------")
        print("Livro escolhido: {}.".format(books[option-1]))

    elif option == 4:
        print("-------------------------------")
        print("Livro escolhido: {}.".format(books[option-1]))

    else:
        print("Opção Inválida! Tente novamente.")

else:
    print("\nOk. O que você deseja? ")
