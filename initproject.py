print("Lista zakupów")
shopping_list = ["chleb", "paczek", "bulki", "marchew", "seler", "rukola"]
shopping_dict = {
    "piekarnia" : ["chleb", "paczek", "bulki"],
    "warzywniak" : ["marchew", "seler", "rukola"]
}
for shop in shopping_dict:
    items = [item.capitalize() for item in shopping_dict[shop]]
    print(f"Idę do {shop.capitalize()}, kupuję tam: {', '.join(items)}.")