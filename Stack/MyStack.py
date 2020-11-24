class MyStack:
    def __init__(self):
        self.data=[]

    def push(self,x):
        """
        将数据压入栈中
        :param x:需要插入的元素
        :return:
        """
        self.data.append(x)

    def pop(self):
        """
        从栈中弹出元素
        :return:弹出的元素
        """
        if not self.empty():
            ret,self.data=self.data[-1],self.data[:-1]
            return ret
        return None

    def empty(self):

        """
        判断栈是否为空
        :return:栈空：true，非空：false
        """
        return len(self.data)==0

    def size(self):
        """
        获取栈中元素的数量
        :return:
        """
        return len(self.data)

    def peek(self):
        """
        返回最后一个插入的元素
        :return:最后一个插入的元素
        """

        if not self.empty():
            return self.data[-1]
        return None
    
    