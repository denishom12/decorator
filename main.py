import csv


class Memento():
    privat_cost: int

    def __init__(self, cost):
        self.privat_cost = cost

    def getCost(self):
        return self.privat_cost


class Originator():
    memento: Memento

    def getMemento(self, memento: Memento):
        pass

    def setMemento(self, memento: Memento):
        pass


class Product(Originator):
    privat_cost: int
    name: str
    sale: int
    index: int

    def __init__(self, name):
        self.name = name
        self.privat_cost = 10000

    def getCost(self, cost):
        self.privat_cost = cost

    def setCost(self):
        return self.privat_cost

    def getSales(self, sale):
        otv = int(self.privat_cost)
        org = sale * otv
        otv = otv - (org/100)
        self.privat_cost = otv

    def delSales(self, sale):
        self.privat_cost = self.privat_cost + ((sale * self.privat_cost)/100)

    def onlySales(self,sale):
        self.sale = sale

    def printCost(self):
        print("Стоимость, включая скидки: ", self.privat_cost)

    def setMemento(self, memento: Memento):
        self.privat_cost = memento.getCost()

    def getMemento(self):
        return Memento(self.privat_cost)


class ConcreteProduct(Product):
    name: str
    privat_cost: int
    sale: int
    index: int

    def puton(self):
        return self.name


class Decorator(Product):
    product: Product
    sale: int

    def __init__(self, product: Product, cost, name):
        self.product = product
        self.privat_cost = cost
        self.name = name

    def clothes(self):
        return self.product

    def puton(self):
        return self.product.puton()


class ConcreteDecorator(Decorator):
    sale = 30

    def puton(self):
        return f"30% sale ({self.product.puton()})"


class ConcreteDecorator1(Decorator):
    sale = 5

    def puton(self):
        return f"5% sale({self.product.puton()})"


class ConcreteDecorator2(Decorator):
    sale = 10

    def puton(self):
        return f"10% sale({self.product.puton()})"


class ConcreteDecorator4(Decorator):
    sale = 0

    def puton(self):
        return f"0% sale({self.product.puton()})"


class Saler():
    __memento: Memento

    def saveState(self, originator: Originator):
        self.__memento = originator.getMemento()
        print("Сохранить скидку")

    def loadState(self, originator: Originator):
        originator.setMemento(self.__memento)
        print("Загрузить скидку")


def client(product: Product):
    print(f"Добавляем все скидки: {product.puton()}")


class DataBase():
    pproduct: Product
    articl: str
    dect: Decorator
    saler: Saler

    def __init__(self, product: Product, dect: Decorator, saler: Saler, _articl):
        self.pproduct = product
        self.dect = dect
        self.saler = saler
        self.articl = _articl

    def id(self):
        return self.articl

    def name(self):
        return self.pproduct.name

    def sale(self):
        return str(self.pproduct.privat_cost)

    def cost(self):
        print("WEAREHERE")
        self.saler.loadState(self.dect)
        return str(self.pproduct.privat_cost)

    def onsale(self):
        return str(self.pproduct.sale)

    def values(self):
        return self.id(), self.name(), self.sale(), self.cost(), self.onsale()


def print_pretty_table(data, cell_sep=' | ', header_separator=True):
    rows = len(data)
    cols = len(data[0])

    col_width = []
    for col in range(cols):
        columns = [data[row][col] for row in range(rows)]
        col_width.append(len(max(columns, key=len)))

    separator = "-+-".join('-' * n for n in col_width)

    for i, row in enumerate(range(rows)):
        if i == 1 and header_separator:
            print(separator)

        result = []
        for col in range(cols):
            item = data[row][col].rjust(col_width[col])
            result.append(item)

        print(cell_sep.join(result))


def interface():
    groups = []
    dates =[]
    i = 0
    k = 0

    simples=[]
    sales=[]
    salers=[]
    decs =[]
    costers=[]
    shops =[0]*100
    table_datas=[]
    table_datas.append(['Артикул', 'Наименование товара', 'Стоимость', 'Стоимость без скидок', 'Скидка в %'])

    while (True):
        print("-----MENU-----")
        print("1. просмотр базы товаров\n"
              "2. добавить товар\n"
              "3. удалить товар\n"
              "4. выбрать товар\n")
        flag = int(input())
        if(flag ==1):
            i = 0
            with open('text.csv', newline='') as file:
                f = list(csv.reader(file))
                for el in f:
                    print("K", k)
                    print("i", i)
                    nm = el[1]
                    simples.append(ConcreteProduct(nm))
                    simples[i].index = i
                    cst = el[3]
                    simples[i].getCost(cst)
                    sales.append(0)
                    salers.append(Saler())
                    costers.append(simples[i].setCost())
                    decs.append(ConcreteDecorator4(simples[i], costers[i], simples[i].name))
                    salers[i].saveState(decs[i])
                    sales[i] = 0
                    art = el[0]
                    dates.append(DataBase(decs[i], decs[i], salers[i], art))
                    table_datas.append(dates[i].values())
                    i = i+1
            k = i
            i = 0
            table_datas = f
            print_pretty_table(table_datas)
            print("KKK", k)

        if(flag == 2):
            print("KK", k)
            print("Name")
            nm = input()
            simples.append(ConcreteProduct(nm))

            simples[k].index = k
            print("Cost")
            cst = input()
            simples[k].getCost(cst)
            sales.append(0)
            salers.append(Saler())
            costers.append(simples[k].setCost())
            decs.append(ConcreteDecorator4(simples[k], costers[k], simples[k].name))
            salers[k].saveState(decs[k])
            sales[k] = 0

            art = str(k)
            dates.append(DataBase(decs[k], decs[k], salers[k], art))
            table_datas.append(dates[k].values())
            print_pretty_table(table_datas)
            k = k+1
        if(flag ==4):
            i = 0
            print("Введите артикул товара")
            flag1 = int(input())
            for x in range(100):
                print(simples[x].index)
                if(simples[x].index == flag1):
                    print("Изменить скидку? ")
                    flag2 = int(input())
                    if(flag2 == 1):

                        print("5 10 30")
                        flag3 = int(input())
                        if(flag3 == 30):
                            indx = simples[x].index

                            sale = int(shops[indx])

                            salers.append(Saler())
                            costers.append(simples[indx].setCost())
                            decs.append(ConcreteDecorator(decs[indx], costers[-1], simples[indx].name))
                            salers[indx].saveState(decs[indx])
                            decs[-1].printCost()

                            sale = sale + decs[-1].sale
                            print("SALE", sales[-1])
                            shops[indx] = sale

                            decs[-1].onlySales(sale)
                            decs[-1].getSales(sale)

                            dates[indx] = DataBase(decs[-1], decs[-1], salers[indx], str(indx))
                            table_datas[indx] = dates[indx].values()
                            print_pretty_table(table_datas)
                            break

                        if (flag3 == 10):
                            indx = simples[x].index

                            sale = int(shops[indx])
                            salers.append(Saler())
                            costers.append(simples[indx].setCost())
                            decs.append(ConcreteDecorator2(decs[indx], costers[-1], simples[indx].name))
                            salers[-1].saveState(decs[-1])
                            decs[-1].printCost()

                            sale = sale + decs[-1].sale

                            shops[indx] = sale

                            decs[-1].onlySales(sale)
                            decs[-1].getSales(sale)

                            dates[indx] = DataBase(decs[-1], decs[-1], salers[indx], str(indx))
                            table_datas[indx] = dates[indx].values()
                            print_pretty_table(table_datas)
                            break

                        if (flag3 == 5):
                            indx = simples[x].index

                            sale = int(shops[indx])
                            salers.append(Saler())
                            costers.append(simples[indx].setCost())
                            decs.append(ConcreteDecorator1(decs[indx], costers[-1], simples[indx].name))
                            salers[-1].saveState(decs[-1])
                            decs[-1].printCost()

                            sale = sale + decs[-1].sale

                            shops[indx] = sale

                            decs[-1].onlySales(sale)
                            decs[-1].getSales(sale)

                            dates[indx] = DataBase(decs[-1], decs[-1], salers[indx], str(indx))
                            table_datas[indx] = dates[indx].values()
                            print_pretty_table(table_datas)
                            break

        if(flag == 5):
            print("Сохранить все в базу")
            with open('text.csv', 'w', newline='') as file:
                csv.writer(file).writerows(table_datas)


interface()