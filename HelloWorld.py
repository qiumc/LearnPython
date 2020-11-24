import re


str="摘要：一、队列的概念 1.基本概念 队列（queue）又被称为队，也是一种保存数据元素的容器。队列时一种特殊的线性表，只允许在表的前端（front）进行删除操作，只允许在表的后端（rear）进行插入操作，进行删除操作的一端叫做对头，进行插入操作的一端称为队尾。"

res=re.match(r'(队列).*',str,re.MULTILINE|re.IGNORECASE)

print(res)