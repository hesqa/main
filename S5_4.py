def update_list(z):
    updated_list = [4 if i == 3 else i for i in z if i != 2]
    return updated_list

if __name__ == "__main__":
    z = [2, 3, 4, 5, 3, 4, 5, 2, 2, 5, 3, 4, 3, 5, 4]
    x = [4, 2, 3, 5, 3, 5, 4, 2, 2, 5, 4, 3, 5, 3, 4]
    c = [5, 4, 3, 3, 4, 3, 3, 5, 5, 3, 3, 3, 3, 4, 4]
    print(update_list(z))

    