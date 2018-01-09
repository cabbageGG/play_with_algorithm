#-*-coding:utf-8 -*-

'''
python元类理解：
1、python中可以动态创建类对象。
   比如：使用type函数。type(类名，(继承的类名，),{属性字典，可以是变量或函数。})
   MyShinyClass = type('MyShinyClass', (), {})  # 返回一个类对象
2、python的这种使用type函数来创建类的方式，其实就是元类的作用。type就是一个元类。
   也就是说：元类就是用来创建类的“东西”。
3、python创建一个类的过程：（重要）（多度几遍）
    class Foo(Bar):
       pass
   Foo中有__metaclass__这个属性吗？如果是，Python会在内存中通过__metaclass__创建一个名字为Foo的类对象
   （我说的是类对象，请紧跟我的思路）。如果Python没有找到__metaclass__，它会继续在Bar（父类）中寻找__metaclass__属性，
   并尝试做和前面同样的操作。如果Python在任何父类中都找不到__metaclass__，它就会在模块层次中去寻找__metaclass__，
   并尝试做同样的操作。如果还是找不到__metaclass__,Python就会用内置的type来创建这个类对象。

   现在的问题就是，你可以在__metaclass__中放置些什么代码呢？
   答案就是：可以创建一个类的东西。那么什么可以用来创建一个类呢？type，或者任何使用到type或者子类化type的东东都可以。
'''
#自定义元类

#示例1：通过自定义函数来实现
# 元类会自动将你通常传给‘type’的参数作为自己的参数传入
def upper_attr(future_class_name, future_class_parents, future_class_attr):
    '''返回一个类对象，将属性都转为大写形式'''
    #  选择所有不以'__'开头的属性
    attrs = ((name, value) for name, value in future_class_attr.items() if not name.startswith('__'))
    # 将它们转为大写形式
    uppercase_attr = dict((name.upper(), value) for name, value in attrs)
    # 通过'type'来做类对象的创建
    return type(future_class_name, future_class_parents, uppercase_attr)

# __metaclass__ = upper_attr  #  这会作用到这个模块中的所有类

class Foo(object):
    # 我们也可以只在这里定义__metaclass__，这样就只会作用于这个类中
    bar = 'bip'
    __metaclass__ = upper_attr  #自己定义的。

print (hasattr(Foo, 'bar'))
# 输出: False
print (hasattr(Foo, 'BAR'))
# 输出:True
 
f = Foo()
print (f.BAR)
# 输出:'bip'
 


#示例2：通过自定义metaclass来实现
class UpperAttrMetaclass(type):
    def __new__(cls, name, bases, dct):
        attrs = ((name, value) for name, value in dct.items() if not name.startswith('__'))
        uppercase_attr = dict((name.upper(), value) for name, value in attrs)
        uppercase_attr['add1'] = 'add1'
        return super(UpperAttrMetaclass, cls).__new__(cls, name, bases, uppercase_attr)

class Test(object):
    def test(self):
        print 'test'
    __metaclass__ = UpperAttrMetaclass

print (hasattr(Test,'test'))
print (hasattr(Test,'TEST'))
print (hasattr(Test,'add1'))
t = Test()
print (t.add1)     

    