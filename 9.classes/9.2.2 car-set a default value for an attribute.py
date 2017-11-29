#9.2.2 setting a default value for an attribute 为属性指定默认值
class Car():
    def __init__(self,make,model,year):
        """初始化描述汽车的属性"""
        self.make=make
        self.model=model
        self.year=year
        self.odometer_reading=0
    def get_descriptive_name(self):
        """返回整洁的描述性信息"""
        long_name=str(self.year)+' '+self.make+' '+self.model
        return long_name.title()
    def read_odometer(self):
        """打印一条指出汽车里程的消息"""
        print("This car has "+str(self.odometer_reading)+" miles on it.")
my_new_car=Car('audi','a4','2016')
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()
# 调用__init__()创建新实例时，以属性的形式存储make model year,并创建一个初始值为0的属性odometer_reading
