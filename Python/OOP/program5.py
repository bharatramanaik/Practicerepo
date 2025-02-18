from typing import List, Dict, Tuple, Union


# walrus opreator
if (n := len([1,2,3,4,5])) > 3:
    print(f"length is {n}")


# type definitions
x: int = 334
print(x.bit_length())

nums: List[int] = [1,2,2,3]
dicts: Dict[str, int] = {"abc": 23, "cdf":45}
tuples: Tuple[str, int] = ("bh", 345)
identi: Union[str, int] = "ID23"


# Match operator
def match_status(scode) -> str:  # return type is string
    match scode:
        case 200:
            return "ok"
        case 404:
            return "not found"
        case 500:
            return "server error"
        case _:
            return "other"
        
print(match_status(200))
