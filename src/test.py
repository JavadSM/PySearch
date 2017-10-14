with open("database.dhp", "r") as f:
    searchlines = f.readlines()

''' OLD VERSION
    while count != results:
        try:
            base = comp(io_data)
        except ValueError:
            print("No more results")
            break
        io_data = [x for x in io_data if x != base]
        sline = int(base) - 1
        print(database[sline], "On line:", base)
        count += 1
    '''
