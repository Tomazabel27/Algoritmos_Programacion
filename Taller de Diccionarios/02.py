lista=[]
dic= {'Mikel': 3, 'Ane': 8, 'Amaia': 12, 'Unai': 5, 'Jon': 8, 'Ainhoa': 7, 
'Maite': 5}
for num in dic:
    lista.append(dic[num])
listax=set(lista)
listav=list(listax)
print (sorted (listav), reverse=True)