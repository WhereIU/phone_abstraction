from phone import Phone

iphone_15 = Phone(
    brand="Apple",
    model="iPhone 15 Pro",
    price=1299.99,
    color="Titanium Natural",
    storage_gb=256,
    is_in_stock=True
)

samsung_a54 = Phone(
    brand="Samsung",
    model="Galaxy A54",
    price=449.99,
    color="Awesome Black",
    storage_gb=128,
    is_in_stock=True
)

google_pixel = Phone(
    brand="Google",
    model="Pixel 8 Pro",
    price=999.00,
    color="Porcelain",
    storage_gb=256,
    is_in_stock=False
)


xiaomi_phone = Phone(
    brand="Xiaomi",
    model="13 Ultra",
    price=1199.50,
    color="Green",
    storage_gb=512,
    is_in_stock=True
)

# simple tests each phone
phones = (iphone_15, samsung_a54, google_pixel, xiaomi_phone)
functions = (
    lambda phone: print(phone.get_full_name()),
    lambda phone: phone.apply_discount(30),
    lambda phone: print(phone.check_availability()),
    lambda phone: print(phone),
)
for phone in phones:
    for function in functions:
        function(phone)
        