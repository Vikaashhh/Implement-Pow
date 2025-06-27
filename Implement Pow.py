class Solution:
    def power(self, b: float, e: int) -> float:
        # Base case: agar exponent 0 ho to result hamesha 1 hota hai
        if e == 0:
            return 1.0

        # Negative exponent ke liye: b^-e = 1 / (b^e)
        if e < 0:
            b = 1 / b
            e = -e

        result = 1.0

        # Exponentiation by squaring
        while e > 0:
            # Agar e odd hai to result me b ko multiply karo
            if e % 2 == 1:
                result *= b
            # Square the base
            b *= b
            # Half the exponent
            e //= 2

        return result
