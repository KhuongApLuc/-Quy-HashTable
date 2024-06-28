#hàm được gọi lại bởi chính nó
#là 1 dạng vòng lặp nhưng không phải while hay for loop
#nếu không có điều kiện thì có thể lặp vô hạn

import os
os.system('cls')

# def factorial( a ):
#     if a == 1 :
#         return 1
#     return a * factorial(a-1)
# a = int(input())
# print(factorial( a ))

class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

class Binary_search_tree:
    def __init__(self):
        self.root = None
    def __r_contains(self, current_node, value):
        if current_node == None:
            return False
        if value == current_node.value:
            return True
        if value < current_node.value :
            return self.__r_contains(current_node.left, value)  
        if value > current_node.value :
            return self.__r_contains(current_node.right, value) 
        
    def r_contains(self,value):
        return self.__r_contains(self.root, value)

    def __r_insert(self,current_node, value):
        if current_node is None :
            return Node(value)
        if value < current_node.value:
            current_node.left = self.__r_insert(current_node.left,value)  
        if value > current_node.value:
            current_node.right = self.__r_insert(current_node.right,value)  
        return current_node
    def r_insert(self,value):
        if self.root is None :
            self.root = Node(value)
        return self.__r_contains(self.root, value)
    
    def __delete_node(self, current_node,value):
        if current_node is None :
            return None
        if value < current_node.value :
            current_node.left = self.__delete_node(current_node.left,value)
        elif value > current_node.value :
            current_node.right = self.__delete_node(current_node.right,value)
        else:
            if current_node.left is None and current_node.right is None :
                return None
            elif current_node.left is None:
                current_node = current_node.right
            elif current_node.right is None:
                current_node = current_node.left
            else : 
                sub_tree__min = self.min_value(current_node.right)
                current_node.value = sub_tree__min
                current_node.right = self.__delete_node(current_node.right, sub_tree__min)
        return current_node
    
    def delete_node(self,value):
        return self.__delete_node(self.root, value)
    
    def min_value (self, current_node):
        while current_node.left is not None:
            current_node = current_node.left
        return current_node.value
a = Binary_search_tree()
a.r_insert(8)
a.r_insert(4)
a.r_insert(12)
a.r_insert(2)
a.r_insert(1)
a.r_insert(3)
a.r_insert(6)
a.r_insert(5)
a.r_insert(7)
a.r_insert(10)
a.r_insert(9)
a.r_insert(11)
a.r_insert(14)
a.r_insert(13)
a.r_insert(15)
