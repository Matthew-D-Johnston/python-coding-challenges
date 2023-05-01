def profit(sales):
  total_cost = sales["cost_price"] * sales["inventory"]
  total_sales = sales["sell_price"] * sales["inventory"]

  return round(total_sales - total_cost)

print(profit({
  "cost_price": 32.67,
  "sell_price": 45.00,
  "inventory": 1200
}))

print(profit({
  "cost_price": 225.89,
  "sell_price": 550.00,
  "inventory": 100
}))

print(profit({
  "cost_price": 2.77,
  "sell_price": 7.95,
  "inventory": 8500
}))