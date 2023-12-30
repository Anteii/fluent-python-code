# Simple unpacking
pair = (1.244, 46.6)
first_el, second_el = pair

# Nested unpacking
city = ("name", (1.244, 46.6))
#name, first_el, second_el = city # Error
name, (first_el, second_el) = city

# Grab excess items
city = ("name", (1.244, 46.6), 500_000, 24.1)
name, (first_el, second_el), *_ = city

city = ("name", 0, "region", (1.244, 46.6), 500_000)
name, *_, (first_el, second_el), pop = city

# Unpack field
[record] = [("name", (1.244, 46.6), 500_000, 24.1)]
[[name]] = [("name",)]

(record,) = [("name", (1.244, 46.6), 500_000, 24.1)]
((name,),) = [("name",)]

*_, [long, lat], _ = ("name", 0, "region", (1.244, 46.6), 500_000)
