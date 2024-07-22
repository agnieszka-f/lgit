print("Moja lista zakupów:")
shoppingList = {
  "Piekarnia" : ['Chleb', 'Pączek', 'Bułki'],
  "Warzywniak" : ['Marchew', 'Seler', 'Rukola']
}
count = 0;
for shop, products in shoppingList.items():
  print(f"Idę do {shop.upper()} i kupuję tam następujące rzeczy: {[p.upper() for p in products]}")
  count = count + len(products)

print(f"W sumie kupuję {count} produktów.")