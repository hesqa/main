with open("empty.txt", "w") as file:
    pass

with open("data.txt", "w") as file:
    file.write("zxcvbnm12345")

def read_file(file_name):
    try:
        with open(file_name, "r") as file:
            data = file.read()
            if not data:
                raise Exception("Файл пуст")
            else:
                print(data)
    except Exception as e:
        print(e)

read_file("empty.txt")

read_file("data.txt")