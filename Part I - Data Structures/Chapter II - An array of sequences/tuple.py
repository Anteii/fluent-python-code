def is_fixed(o: object) -> bool:
    try:
        hash(o)
    except TypeError:
        return False
    return True

mt = (1, 2, [3, 4])
it = (1, "asdf", 5.1, ())
 
print("Tuple with mutable values:", is_fixed(mt))
print("Tuple with immutable values:", is_fixed(it))