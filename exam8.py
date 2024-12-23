def bankrank(filename):
    output_data = "Rich-rank,Amount,Name,Customer-ID\n"
    try:
    fread = open(filename,"r")
    headings = fread.readline().split(",")
    except FileNotFoundError: #fine if error is not mentioned
        print("Unable to open or read the file. Check filename or path and permissions to the file.")
    return

    try:
        name_idx = headings.index("Name")
        id_idx = headings.index("Customer_ID")
        deposits_idx = headings.index("deposits")
    except ValueError: #fine if error is not mentioned
        return

    i = 1
    comp = []
    for line in fread:
        list = []
        money = line[deposits_idx].split('-')
        total = 0
        for item in money:
            total+=float(item)
        list.append(total)
        string =line[name_idx] + "," + line[id_idx] + "\n"
        list.append(string)
        comp.append(list)
    fread.close()
    list2 = sorted(comp, key=lambda comp: (-comp[0]))
    for thing in list2:
        output_data+=thing[0] + thing[1]
    try:
        fwrite = open("ranked.txt","w")
        fwrite.write(output_data)
        fwrite.close
    except:
        print("unable to create the file for writing")
    return
