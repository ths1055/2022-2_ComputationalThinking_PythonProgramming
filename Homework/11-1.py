import myHashMap
if __name__ == "__main__":
    HashMap_Capacity = 7
    print("Creating a HashMap of capacity ({})".format(HashMap_Capacity))
    hsMap = myHashMap.HashMap(capacity=HashMap_Capacity)
    Entries = [("Kim", 19345, "ICE", 4.0), ("Park", 18234, "CS", 4.2), ("Hong", 20456, "EE", 3.9), ("Lee", 20987, "ME", 3.8), ("Yoon", 21654, "ICE", 3.7), ("Moon", 21001, "CHEM", 4.1), ("Hwang", 21123, "CE", 3.7), ("Choi", 19003, "EE", 4.3), ("Yeo", 20234, "ME", 3.8), ("Jeong", 18005, "PH", 4.3)]
    for i in range(len(Entries)):
        entry = Entries[i]
        key = entry[0]
        hsMap._setitem(key, entry)
        print("Entry[{:2}] : {}".format(i, Entries[i]))
    print("Current HashMap Internal Structure:\n", hsMap)
    print("Checking entry searching in HashMap")
    while True:
        key = input("Input student name to search (. to quit) : ")
        if key == '.':
            break
        v = hsMap._getitem(key)
        if v == None:
            print("key ({}) is not found in hashmap !!".format(key))
        else:
            print("key ({}) : Value ({})".format(key, v))