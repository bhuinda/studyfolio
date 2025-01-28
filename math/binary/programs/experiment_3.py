import sympy

def prime_factorization(n):
    # Check if the number is prime
    if sympy.isprime(n):
        return f"The number {n} is prime."
    else:
        # If it's not prime, get the prime factors
        factors = sympy.factorint(n)
        return f"The prime factorization of {n} is: {factors}"

# The large number
large_number = 64981894480961462577763634484511978224024849567652872834876704053749370159051445366279159426604828098301112122501621822068760910559347651308433540035418116275199093504834057074335003198802893740037259106111483600855280707034304853464486993440633488710148001049588419873358215578371610885376299349236988289645125801050742222390548814409606169633455439361911141607597582291683427008810424558033733041918047788469881392415452051400238802400459420210775873704730178451519837648120424255019424671608324893025313470391940042373386469375

# Call the function
result = prime_factorization(large_number)
print(result)
