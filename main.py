

if __name__ == '__main__':
    while True:
        print("-----------------------")
        total_items = int(input("Total items: "))
        stack_size = int(input("Stack size: "))

        stacks = int(total_items / stack_size)
        items = total_items % stack_size

        # Stack String
        if stacks == 1:
            stack_string = str(stacks) + " stack, "
        else:
            stack_string = str(stacks) + " stacks, "

        # Item String
        if items == 1:
            item_string = str(items) + " item"
        else:
            item_string = str(items) + " items"

        # Print stacks and items required
        print(stack_string, item_string)

        if input("Again? (y/n): ") == "n":
            break
