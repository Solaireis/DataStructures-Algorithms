# Name:Eden Will Sng Jin Xuan, Adm:201520M , Tutorial-Grp:IT2553-02
# install the following packages:
# pip install -r requirements.txt


class Record():
    def __init__(self, package, customer, pax, cost):
        self.__package = package
        self.__customer = customer
        self.__pax = pax
        self.__cost = cost

    def get_package(self):
        return self.__package
    
    def set_package(self, package):
        self.__package = package
    
    def get_customer(self):
        return self.__customer
    
    def set_customer(self, customer):
        self.__customer = customer

    def get_pax(self):
        return self.__pax
    
    def set_pax(self, pax):
        self.__pax = pax

    def get_cost(self):
        return self.__cost
    
    def set_cost(self, cost):
        self.__cost = cost


def displayRecord(i, theRecords):
    print("Row:", i+1)
    print("Package:", theRecords[i].get_package())
    print("Customer:", theRecords[i].get_customer())
    print("Number of pax:", theRecords[i].get_pax())
    print("Cost per pax:", theRecords[i].get_cost())
    print("")

def list_records(theRecords):
    sortedRecords = sorted(theRecords, key=lambda x: x.get_cost())
    for i in theRecords:
        print("")
        displayRecord(i, sortedRecords)