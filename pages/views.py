from django.shortcuts import render, redirect
from django.http import HttpResponse

def index(request):
    return render(request, 'pages/index.html')

def about(request):
    return render(request, 'pages/results.html')

def search(request):
    print(request.method)
    if request.method == "POST":
        
        Ingredient = request.POST["Ingredient"]
        r = requests.get(f'https://www.thecocktaildb.com/api/json/v1/1/filter.php?i={Ingredient}')
        if r.text == "":
            return render(request, 'pages/index.html', context={"Error": "Error! Please enter a different ingredient"})

        parsed = r.json()
        # print(json.dumps(parsed, indent=4, sort_keys=True))


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

        #Instructions
        drinkInstr= Details["drinks"][0]["strInstructions"]

        ingredientsList2=[]
        for n in range (1,15,1):
            ingredientsList2.append({
                "ing": Details["drinks"][0]["strIngredient"+str(n)],
                'measure': Details["drinks"][0]["strMeasure"+str(n)]
            })

        context= {
        'drinkName': drinkName,
        'drinkThumb': drinkThumb,
        'ingredientsList': ingredientsList2,
        'drinkInstr': drinkInstr,
        'query': Ingredient,
        }
        print('test1')
        print(json.dumps(context))
        return render(request, 'Pages/results.html', context)
    else: 
        return redirect('/')

import requests 
import json 
import random

# def vodka(request):

#     Ingredient = 'Vodka'
#     r = requests.get(f'https://www.thecocktaildb.com/api/json/v1/1/filter.php?i={Ingredient}')

#     parsed = r.json()
#     # print(json.dumps(parsed, indent=4, sort_keys=True))


#     drinkNum = random.randint(0,len(parsed["drinks"])-1)
#     # print(drinkNum)

#     Drinkid=parsed["drinks"][drinkNum]["idDrink"]
#     # Drinkid=178318
#     Det = requests.get(f'https://www.thecocktaildb.com/api/json/v1/1/lookup.php?i={Drinkid}')
#     Details = Det.json()
#     print(json.dumps(Details, indent=4, sort_keys=True))

#     #Name
#     drinkName = Details["drinks"][0]["strDrink"]
#     #Thumbnail
#     drinkThumb = Details["drinks"][0]["strDrinkThumb"]

#     #Instructions
#     drinkInstr= Details["drinks"][0]["strInstructions"]

#     ingredientsList2=[]
#     for n in range (1,15,1):
#         ingredientsList2.append({
#             "ing": Details["drinks"][0]["strIngredient"+str(n)],
#             'measure': Details["drinks"][0]["strMeasure"+str(n)]
#         })

#     context= {
#     'drinkName': drinkName,
#     'drinkThumb': drinkThumb,
#     'ingredientsList': ingredientsList2,
#     'drinkInstr': drinkInstr,
#     }
#     print('test1')
#     print(json.dumps(context))
#     return render(request, 'Pages/results.html', context)