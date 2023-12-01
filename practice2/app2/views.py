from django.shortcuts import render

# Create your views here.

def index(request):
    meals = [
        {
            "strMealThumb": "https://www.themealdb.com/images/media/meals/ryppsv1511815505.jpg",
            "strMeal": "BeaverTails",
            "idMeal": "Lorem, ipsum dolor sit amet consectetur adipisicing elit. Ipsa vero voluptate tempora sequi. Illo reprehenderit necessitatibus ullam natus reiciendis error."
        },
        {
            "strMealThumb": "https://www.themealdb.com/images/media/meals/1550441882.jpg",
            "strMeal": "Breakfast Potatoes",
            "idMeal": "Lorem, ipsum dolor sit amet consectetur adipisicing elit. Ipsa vero voluptate tempora sequi. Illo reprehenderit necessitatibus ullam natus reiciendis error."
        },
        {
            "strMealThumb": "https://www.themealdb.com/images/media/meals/wpputp1511812960.jpg",
            "strMeal": "Canadian Butter Tarts",
            "idMeal": "Lorem, ipsum dolor sit amet consectetur adipisicing elit. Ipsa vero voluptate tempora sequi. Illo reprehenderit necessitatibus ullam natus reiciendis error."
        },
        {
            "strMealThumb": "https://www.themealdb.com/images/media/meals/uttupv1511815050.jpg",
            "strMeal": "Montreal Smoked Meat",
            "idMeal": "Lorem, ipsum dolor sit amet consectetur adipisicing elit. Ipsa vero voluptate tempora sequi. Illo reprehenderit necessitatibus ullam natus reiciendis error."
        },
        {
            "strMealThumb": "https://www.themealdb.com/images/media/meals/vwuprt1511813703.jpg",
            "strMeal": "Nanaimo Bars",
            "idMeal": "Lorem, ipsum dolor sit amet consectetur adipisicing elit. Ipsa vero voluptate tempora sequi. Illo reprehenderit necessitatibus ullam natus reiciendis error."
        },
        {
            "strMealThumb": "https://www.themealdb.com/images/media/meals/yyrrxr1511816289.jpg",
            "strMeal": "Pate Chinois",
            "idMeal": "Lorem, ipsum dolor sit amet consectetur adipisicing elit. Ipsa vero voluptate tempora sequi. Illo reprehenderit necessitatibus ullam natus reiciendis error."
        },
        {
            "strMealThumb": "https://www.themealdb.com/images/media/meals/yqqqwu1511816912.jpg",
            "strMeal": "Pouding chomeur",
            "idMeal": "Lorem, ipsum dolor sit amet consectetur adipisicing elit. Ipsa vero voluptate tempora sequi. Illo reprehenderit necessitatibus ullam natus reiciendis error."
        },
        {
            "strMealThumb": "https://www.themealdb.com/images/media/meals/uuyrrx1487327597.jpg",
            "strMeal": "Poutine",
            "idMeal": "Lorem, ipsum dolor sit amet consectetur adipisicing elit. Ipsa vero voluptate tempora sequi. Illo reprehenderit necessitatibus ullam natus reiciendis error."
        },
        {
            "strMealThumb": "https://www.themealdb.com/images/media/meals/ruwpww1511817242.jpg",
            "strMeal": "Rappie Pie",
            "idMeal": "Lorem, ipsum dolor sit amet consectetur adipisicing elit. Ipsa vero voluptate tempora sequi. Illo reprehenderit necessitatibus ullam natus reiciendis error."
        },
        {
            "strMealThumb": "https://www.themealdb.com/images/media/meals/xxtsvx1511814083.jpg",
            "strMeal": "Split Pea Soup",
            "idMeal": "Lorem, ipsum dolor sit amet consectetur adipisicing elit. Ipsa vero voluptate tempora sequi. Illo reprehenderit necessitatibus ullam natus reiciendis error."
        }
    ]

    return render(request, 'app2/index.html', {'meals': meals})