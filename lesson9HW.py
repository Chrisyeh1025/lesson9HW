dict1 = {'A001':'小熊餅乾 , 20元','A002':'冰棒, 25元','A004':'王子麵, 10元','A006':'汽水 , 30元'}
dict2 = {}
print(dict1)
x = input('要查詢哪個商品?')  
if x not in dict1:
    print('抱歉,找不到此商品')
    print('您可以新增資料')
    i = input('商品名稱?')
    y = input('商品價格?')
    dict2[i] = y
    dict1.update(dict2)
    print(dict1)
    print(dict2)
else:     
    print(dict1[x])
