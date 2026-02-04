users = [
    {"id": 1, "total": 100, "coupon":"P50"},
    {"id": 2, "total": 50, "coupon":"P30"},
    {"id": 3, "total": 80, "coupon":"P10"},
]

discounts = {
    "P50" : (0.5, 0),   # 0.5 is the percentage and 0 is the fixed
    "P30" : (0.3, 0),
    "P10" : (0.1, 0),

}

for user in users:
    percent, fixed = discounts.get(user["coupon"], (0,0))
    discount = user["total"] * percent + fixed
    print(f"{user["id"]} paid {user["total"]} and got discount for next visit for rupess {discount}")