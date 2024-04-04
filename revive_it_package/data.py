def detectDelimiter(csv_naam):
    csvFile = f"../raw_data/{csv_naam}"

    with open(csvFile, 'r') as myCsvfile:
        header=myCsvfile.readline()
        if header.find(";")!=-1:
            return ";"
        if header.find(",")!=-1:
            return ","
    #default delimiter (MS Office export)
    return ";"
