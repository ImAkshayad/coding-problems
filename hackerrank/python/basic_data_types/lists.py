if __name__ == '__main__':
    N = int(input())
    my_list = []
    for i in range(N):
        user_command = input()
        if user_command.startswith("insert"):
            parameters = user_command.split(" ")
            my_list.insert(int(parameters[1]),int(parameters[2]))
        elif user_command.startswith("print"):
            print(my_list)
        elif user_command.startswith("remove"):
            parameters = user_command.split(" ")
            my_list.remove(int(parameters[1]))
        elif user_command.startswith("append"):
            parameters = user_command.split(" ")
            my_list.append(int(parameters[1]))
        elif user_command.startswith("sort"):
            my_list.sort()
        elif user_command.startswith("pop"):
            my_list.pop()
        elif user_command.startswith("reverse"):  
            my_list.reverse()  
        else:
            print("Invalid input")
