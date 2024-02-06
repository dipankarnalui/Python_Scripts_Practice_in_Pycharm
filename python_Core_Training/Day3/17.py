class Emp:
     def __init__(self,name, basic):
        self.name = name
        self.basic = basic
     def ctor(self):
        print("ctor in base class")
     def show(self):
         print("show in base class")
class ContractEmp(Emp):
      def __init__(self, name, basic, cname,additional, netpay=0):
          Emp.__init__(self,name,basic)
          self.cname=cname
          self.additional = additional
          self.netpay = netpay
      def ctor(self):
            print("ctor in derived class")
      def find_netpay(self):
          self.netpay = self.basic + self.additional
      def display(self):
          print("Name = ", self.name)
          print("Basic = ", self.basic)
          print("Cname = ", self.cname)
          print("Additional = ",self.additional)
          print("Netpay = ", self.netpay)

c1 = ContractEmp("ravi",15000,"ABC",4500)
c1.display()  # name = ravi
              # basic = 15000
              # cname = ABC
              # addt  = 4500
              # netpay = 0
c1.find_netpay()
c1.display()  # name = ravi
              # basic = 15000
              # cname = ABC
              # addt  = 4500
              # netpay = 19500
