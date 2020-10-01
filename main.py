#input
a = [
  {'name':'Star Plus', 'Category':'Entertainment'},
  {'name':'Zee Cinema', 'Category':'Entertainment'},
    {'name':'ABP', 'Category':'news'},
    {'name':'Republic', 'Category':'news'}]

#output
d=[{'Entertainment':'Star Plus'}, {'news':'ABP, Republic'}]
temp=''
temp1=''
out={}

n=len(a)
for i in range(n):
  for x in a[i]:
    if(x=='Category'):
      if(a[i][x]=='news'):
        temp +=  ", " +a[i]['name']
        out['news'] = temp
      elif(a[i][x]=='Entertainment'):
        temp1 +=  ", " +a[i]['name']
        out['Entertainment'] = temp1
      
out['news'] = out['news'].strip(", ")
out['Entertainment'] = out['Entertainment'].strip(", ")

output = [out]
print(output)

# for i in range(3):
#   for x in a[i]:
#     if(x=='Category'):
#       if(a[i][x]=='news'):
#         temp.append( a[i]['name'])
#         out['news'] = temp
#       elif(a[i][x]=='Entertainment'):
#         out['Entertainment'] = a[i]['name']

# print(out)

# print(temp)
# out={}

# for i in range(3):
#   for x in a[i]:
#     if(x=='Category'):
#       if(a[i][x]=='news'):
#         out['news'] = a[i]['name']
#       elif(a[i][x]=='Entertainment'):
#         out['Entertainment'] = a[i]['name']
# print(out)

# print(a[0]['name'])
# print(a[0]['Category'])

# for x in a[0]:
#   if(x=='Category'):
#     if(a[0][x]=='Entertainment'):
#       out['Entertainment'] = a[0]['name']
#       print(out)
# for x in a[2]:
#   if(x=='Category'):
#     if(a[2][x]=='news'):
#       out['news'] = a[2]['name']
#       print(out)
# for x in a[1]:
#   if(x=='Category'):
#     if(a[1][x]=='news'):
#       out['news'] = a[1]['name']
#       print(out)
