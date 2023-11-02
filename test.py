a = ["sot"]
a *= 3
print(a)
FPS = 30
print((5 / FPS))

hasBounced = False

dic = {1: [34, 45, 60], 2: (50, 60, 30), 3:hasBounced}
print(dic)
print(dic.get(1))
print(dic.values())
print(dic)

game = "game"

dic_2 = {1: 34, 45: 60, 2: [50, 60, 30], 4: hasBounced}
dic_3 = {1: [game, False, False, (0.5, 0.5)]}

print(dic_2)
hasBounced = True
dic_2.update({4: hasBounced})
print("Dic après chgmnt hasBounced : ", dic)

if dic_2.get(4):
    print("coucou")

variables_temp = dic_3.get(1)
print("Variables temps : ", variables_temp)
temp = (variables_temp[3][0]*-1, 0.5)
variables_temp[3] = temp
print("Variables modifiées : ", variables_temp)
new_dic_3 = dic_3.update({1: variables_temp})

print("Mise à jour dic_3 : ", dic_3)