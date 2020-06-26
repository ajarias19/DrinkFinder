import requests 
import json 
import random
# from pages.views import request.POST('Ingredient')

Ingredient = 'S'
r = requests.get(f'https://www.thecocktaildb.com/api/json/v1/1/filter.php?i={Ingredient}')
print(r.text)

parsed = r.json()
print(json.dumps(parsed, indent=4, sort_keys=True))


drinkNum = random.randint(0,len(parsed["drinks"])-1)
# print(drinkNum)

Drinkid=parsed["drinks"][drinkNum]["idDrink"]
# Drinkid=178318
Det = requests.get(f'https://www.thecocktaildb.com/api/json/v1/1/lookup.php?i={Drinkid}')
Details = Det.json()
print(json.dumps(Details, indent=4, sort_keys=True))

#Name
drinkName = Details["drinks"][0]["strDrink"]
#Thumbnail
drinkThumb = Details["drinks"][0]["strDrinkThumb"]
#Ingredients
drinkIng1= Details["drinks"][0]["strIngredient1"]
drinkIng2= Details["drinks"][0]["strIngredient2"]
drinkIng3= Details["drinks"][0]["strIngredient3"]
drinkIng4= Details["drinks"][0]["strIngredient4"]
drinkIng5= Details["drinks"][0]["strIngredient5"]
drinkIng6= Details["drinks"][0]["strIngredient6"]
drinkIng7= Details["drinks"][0]["strIngredient7"]
drinkIng8= Details["drinks"][0]["strIngredient8"]
drinkIng9= Details["drinks"][0]["strIngredient9"]
drinkIng10= Details["drinks"][0]["strIngredient10"]
drinkIng11= Details["drinks"][0]["strIngredient11"]
drinkIng12= Details["drinks"][0]["strIngredient12"]
drinkIng13= Details["drinks"][0]["strIngredient13"]
drinkIng14= Details["drinks"][0]["strIngredient14"]
drinkIng15= Details["drinks"][0]["strIngredient15"]
#Instructions
drinkInstr= Details["drinks"][0]["strInstructions"]
#Measurements
ingMeas1= Details["drinks"][0]["strMeasure1"]
ingMeas2= Details["drinks"][0]["strMeasure2"]
ingMeas3= Details["drinks"][0]["strMeasure3"]
ingMeas4= Details["drinks"][0]["strMeasure4"]
ingMeas5= Details["drinks"][0]["strMeasure5"]
ingMeas6= Details["drinks"][0]["strMeasure6"]
ingMeas7= Details["drinks"][0]["strMeasure7"]
ingMeas8= Details["drinks"][0]["strMeasure8"]
ingMeas9= Details["drinks"][0]["strMeasure9"]
ingMeas10= Details["drinks"][0]["strMeasure10"]
ingMeas11= Details["drinks"][0]["strMeasure11"]
ingMeas12= Details["drinks"][0]["strMeasure12"]
ingMeas13= Details["drinks"][0]["strMeasure13"]
ingMeas14= Details["drinks"][0]["strMeasure14"]
ingMeas15= Details["drinks"][0]["strMeasure15"]

print(drinkName)
print(drinkThumb)
if drinkIng1 == type(None)():
    print('- ')
else:
    if ingMeas1 == type(None)():
        print(drinkIng1)
    else:
        print('-' +ingMeas1 + drinkIng1)



if drinkIng2 == type(None)():
    print('- ')
else:
    if ingMeas3 == type(None)():
        print(drinkIng3)
    else:
        print('-' +ingMeas2 + drinkIng2)


if drinkIng3 == type(None)():
    print('- ')
else:
    if ingMeas3 == type(None)():
        print(drinkIng3)
    else:
        print('-' +ingMeas3 + drinkIng3)



if drinkIng4 == type(None)():
    print('- ')
else:
    if ingMeas4 == type(None)():
        print(drinkIng4)
    else:
        print('-' +ingMeas4 + drinkIng4)



if drinkIng5 == type(None)():
    print('- ')
else:
    if ingMeas5 == type(None)():
        print(drinkIng5)
    else:
        print('-' +ingMeas5 + drinkIng5)



if drinkIng6 == type(None)():
    print('- ')
else:
    if ingMeas6 == type(None)():
        print(drinkIng6)
    else:
        print('-' +ingMeas6 + drinkIng6)



if drinkIng7 == type(None)():
    print('- ')
else:
    if ingMeas7 == type(None)():
        print(drinkIng7)
    else:
        print('-' +ingMeas7 + drinkIng7)



if drinkIng8 == type(None)():
    print('- ')
else:
    if ingMeas8 == type(None)():
        print(drinkIng8)
    else:
        print('-' +ingMeas8 + drinkIng8)



if drinkIng9 == type(None)():
    print('- ')
else:
    if ingMeas9 == type(None)():
        print(drinkIng9)
    else:
        print('-' +ingMeas9 + drinkIng9)



if drinkIng10 == type(None)():
    print('- ')
else:
    if ingMeas10 == type(None)():
        print(drinkIng10)
    else:
        print('-' +ingMeas10 + drinkIng10)


if drinkIng11 == type(None)():
    print('- ')
else:
    if ingMeas11 == type(None)():
        print(drinkIng11)
    else:
        print('-' +ingMeas11 + drinkIng11)
        

if drinkIng12 == type(None)():
    print('- ')
else:
    if ingMeas12 == type(None)():
        print(drinkIng12)
    else:
        print('-' +ingMeas12 + drinkIng12)


if drinkIng13 == type(None)():
    print('- ')
else:
    if ingMeas13 == type(None)():
        print(drinkIng13)
    else:
        print('-' +ingMeas13 + drinkIng13)


if drinkIng14 == type(None)():
    print('- ')
else:
    if ingMeas14 == type(None)():
        print(drinkIng14)
    else:
        print('-' +ingMeas14 + drinkIng14)


if drinkIng15 == type(None)():
    print('- ')
else:
    if ingMeas15 == type(None)():
        print(drinkIng15)
    else:
        print('-' +ingMeas15 + drinkIng15)





# print(ingMeas1 + drinkIng1)
# print(ingMeas2 + drinkIng2)
# print(ingMeas3 + drinkIng3)
# print(ingMeas4 + drinkIng4)
print(drinkInstr)



