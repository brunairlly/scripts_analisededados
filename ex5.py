
# coding: utf-8

# In[ ]:


def removeRepetidas(lista):
    lis = []
    for i in lista:
        if i not in lis:
            lis.append(i)
    lis.sort()
    return lis

lista = ['Big Data','Analise de Dados','Big Data', 'Python', 'Python', 'NoSQL']

lista = removeRepetidas(lista)
print (lista)

