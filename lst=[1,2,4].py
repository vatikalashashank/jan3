# lst=[1,2,4]
# sum=0
# p=1
# for x in lst:
#     sum+=x
#     p*=x
# print(sum)
# print(p)

# lst=['100','222','88']
# # op:[0,8,64]
# for x in lst:
#     prd=1
#     for y in x:
#         prd*=int(y)
#     print(prd)

lst=[100,222,88]
for x in lst:
    prd=1
    for y in str(x):
        prd*=int(y)
    print(prd)