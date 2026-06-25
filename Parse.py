# Step 1: Open file, read and print it
# with open("Pokemon.csv", "r") opens the file and tells Python it's in "read" mode
with open("Pokemon.csv", "r") as file:
    # raw_data = file.read()
    # print(raw_data)
    # instead of using file.read(), we can use the Python function readlines() to
    # automatically separate each line
    lines = file.readlines()

    for line in lines[1:]:      # lines[1:] tells Python to start at the second thing in the list and go to the end
        # .strip() to remove the newline character \n from each line
        clean_line = line.strip()
        print()

        # we need to split the line up whenever there's a comma. To do this,
        # we just use the .split() function.
        data = clean_line.split(',')

        # in data,
        # index 0: Number
        # index 1: Name
        # index 2: Type(s)
        # index 3: Description
        # index 4: Evolutions

        number = data[0].strip()
        name = data[1].strip()
        type = data[2].strip()
        description = data[3].strip()
        evolutions = data[4].strip().split(" ")

        '''
        1.  Bulbasaur
            Type(s)
            Description:
            Bulbasaur -> Ivysaur -> Venusaur
            

        2. Ivysaur ...
        '''

        # f strings: easier way to format strings with variables
        # example_f_string = f"{number}.  {name}"

        print(f"{number}.   {name}")
        print(f"    {type}")
        print(f"    {description}")
        if len(evolutions) > 1:
            for i in range(len(evolutions)):
                print(evolutions[i])
                if i < len(evolutions) - 1:
                    print(" -> ")

        print()