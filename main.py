"""1. [1p] Citirea unei liste de numere întregi. Citirile repetate suprascriu listele precedente. 2. [2p] Afișarea tuturor numerelor negative nenule din listă (de ex. -1, -56).
3. [2p] Afișarea celui mai mic număr care are ultima cifră egală cu o cifră citită de la tastatură. Exemplu: [1, 6, 34, 68, 40, 48, 20] și cifra 8 -> 48
4. [2p] Afișarea tuturor numerelor din listă care sunt superprime. Un număr este superprim dacă este  strict pozitiv și toate prefixele sale sunt prime. De exemplu, 173 nu este superprim deoarece 1 nu  este prim, iar 239 este superprim deoarece 2, 23 și 239 sunt toate prime.
5. [3p] Afișarea listei obținute din lista inițială în care numerele pozitive și nenule au fost înlocuite cu  CMMDC-ul lor și numerele negative au cifrele în ordine inversă.
Exemplu: [-76, 12, 24, -13, 144] → [-67, 12, 12, -31, 12] (pentru că CMMDC dintre 12, 24 și 144  este 12).
"""


def get_all_negatives(lst):
    '''
    Returns the list of all negative elements from given list.
    :param lst: Input list of integers.
    :return: all negative elements from given list as list
    '''
    result = []
    for element in lst:
        if element < 0:
            result.append(element)
    return result


def test_get_all_negatives():
    assert get_all_negatives([1, 2, 3]) == []
    assert get_all_negatives([]) == []
    assert get_all_negatives([-1, 2, -3]) == [-1, -3]
    assert get_all_negatives([-2, -3, -4]) == [-2, -3, -4]


def get_smallest_with_given_last_digit(lst, digit):
    '''
    Returns the smallest integer with given last digit .
    :param lst: List of integers.
    :param digit: Digit to check against.
    :return: Smallest integer with given last digist.
    '''
    smallest = None
    for element in lst:
        to_check = abs(element)
        if to_check % 10 == digit and (smallest is None or element < smallest):
            smallest = element
    return smallest


def test_get_smallest_with_given_last_digit():
    assert get_smallest_with_given_last_digit([1, 6, 34, 68, 40, 48, 20], 8) == 48
    assert get_smallest_with_given_last_digit([1, 2, 3, 4, 5, 6], 3) == 3
    assert get_smallest_with_given_last_digit([777, 7, 77], 7) == 7
    assert get_smallest_with_given_last_digit([-777, 7, 77], 7) == -777


def is_prime(number):
    '''
    Check if a given number is prime
    :param number: Number to test.
    :return: True if number is prime, False otherwise.
    '''
    if number < 2:
        return False
    if number != 2 and number % 2 == 0:
        return False
    for factor in range(3, number // 2 + 1, 2):
        if number % factor == 0:
            return False
    return True


def test_is_prime():
    assert is_prime(-2) is False
    assert is_prime(1) is False
    assert is_prime(2) is True
    assert is_prime(3) is True
    assert is_prime(4) is False
    assert is_prime(5) is True
    assert is_prime(9) is False
    assert is_prime(11) is True
    assert is_prime(19) is True
    assert is_prime(20) is False


def is_super_prime(number):
    '''
    Tests if a number is a 'superprime'. A number is a 'superprime' if all its prefixes are primes, including the given number.
    :param number: Input number to be checked if it's 'superprime'.
    :return: True if the number it's 'superprime', false otherwise.
    '''
    clone = number
    while number > 0:
        if not is_prime(number):
            return False
        number //= 10
    if clone <= 0:
        return False
    else:
        return True


def test_is_super_prime():
    assert is_super_prime(12) is False
    assert is_super_prime(-5) is False
    assert is_super_prime(2) is True
    assert is_super_prime(233) is True
    assert is_super_prime(37) is True
    assert is_super_prime(373) is True
    assert is_super_prime(3731) is False


def get_all_super_primes(lst):
    '''
    Returns all elements from the list that are super primes. A number is a 'superprime' if all its prefixes are primes, including the given number.
    :param lst: Input list of integers.
    :return: All elements from the list that are super primes as a list.
    '''
    result = []
    for element in lst:
        if is_super_prime(element):
            result.append(element)
    return result


def test_get_all_super_primes():
    assert get_all_super_primes([2, 3, 5, 7]) == [2, 3, 5, 7]
    assert get_all_super_primes([1, 4, 6, 7, 239, 147]) == [7, 239]
    assert get_all_super_primes([]) == []
    assert get_all_super_primes([17]) == []


def get_biggest_common_factor(first, second):
    '''
    Returns the biggest common factor for given integers.
    :param first: First integer.
    :param second: Second integer.
    :return: Biggest common factor between 'first' and 'second'.
    '''
    if first == 0:
        return second
    elif second == 0:
        return first
    while first != second:
        if first > second:
            first -= second
        else:
            second -= first
    return first


def test_get_biggest_common_factor():
    assert get_biggest_common_factor(4, 4) == 4
    assert get_biggest_common_factor(3, 7) == 1
    assert get_biggest_common_factor(12, 24) == 12
    assert get_biggest_common_factor(24, 36) == 12


def get_biggest_common_factor_of_all_positives(lst):
    '''
    Return the biggest common factor for all elements in list.
    :param lst: Input list of integers.
    :return: Biggest common factor for all elements in list.
    '''
    biggest_common_factor = None
    for element in lst:
        if element > 0:
            if biggest_common_factor is None:
                biggest_common_factor = element
            else:
                biggest_common_factor = get_biggest_common_factor(biggest_common_factor, element)
    return biggest_common_factor


def test_get_biggest_common_factor_of_all():
    assert get_biggest_common_factor_of_all_positives([3, 6, 12]) == 3
    assert get_biggest_common_factor_of_all_positives([12, 3, 6]) == 3
    assert get_biggest_common_factor_of_all_positives([3]) == 3
    assert get_biggest_common_factor_of_all_positives([12, 6]) == 6
    assert get_biggest_common_factor_of_all_positives([-1, 12, 6]) == 6
    assert get_biggest_common_factor_of_all_positives([-1, 12, -6]) == 12
    assert get_biggest_common_factor_of_all_positives([12, 19, 81]) == 1


def get_mirror(nr):
    '''
    Returns the mirror of this number, i.e. the number with digits in reverse order.
    :param nr: Input number.
    :return: The mirror of this number.
    '''
    if nr == 0:
        return 0
    mirror = int(str(abs(nr))[::-1])
    sgn = nr // abs(nr)
    return sgn * mirror


def test_get_mirror():
    assert get_mirror(2) == 2
    assert get_mirror(23) == 32
    assert get_mirror(-123) == -321
    assert get_mirror(0) == 0
    assert get_mirror(-67) == -76


def replace_positives_with_biggest_common_factor_and_negatives_with_mirror(lst):
    '''
   Return a list where positives are replaced by their biggest common factor and negatives by their mirror.
   :param lst: Input list of integers
   :return: A list where positives are replaced by their biggest common factor and negatives by their mirror.
   '''
    biggest_common_factor = get_biggest_common_factor_of_all_positives(lst)
    result = []
    for element in lst:
        to_add = 0
        if element > 0:
            to_add = biggest_common_factor
        elif element < 0:
            to_add = get_mirror(element)
        result.append(to_add)
    return result


def test_replace_positives_with_biggest_common_factor_and_negatives_with_mirror():
    assert replace_positives_with_biggest_common_factor_and_negatives_with_mirror([-76, 12, 24, -13, 144]) == [-67, 12,
                                                                                                               12, -31,
                                                                                                               12]
    assert replace_positives_with_biggest_common_factor_and_negatives_with_mirror([12, 24]) == [12, 12]
    assert replace_positives_with_biggest_common_factor_and_negatives_with_mirror([1, 3, 5, -8]) == [1, 1, 1, -8]
    assert replace_positives_with_biggest_common_factor_and_negatives_with_mirror([-9, 0, -8]) == [-9, 0, -8]


def read_input_elements():
    elements = []
    no_elements = int(input('Number of elements='))
    for index in range(0, no_elements):
        el = int(input(f'el[{index + 1}]='))
        elements.append(el)
    return elements


def test_all():
    test_is_prime()
    test_is_super_prime()
    test_get_all_negatives()
    test_get_smallest_with_given_last_digit()
    test_get_all_super_primes()
    test_get_biggest_common_factor()
    test_get_biggest_common_factor_of_all()
    test_get_mirror()
    test_replace_positives_with_biggest_common_factor_and_negatives_with_mirror()


def last_digit_option(lst):
    digit = int(input('Give last digit:'))
    print(f"Smallest number with given last digit is: {get_smallest_with_given_last_digit(lst, digit)}")


def show_options():
    print("""
    1.Citeste lista de la tastatura
    2.Afișarea tuturor numerelor negative nenule din listă
    3.Afiseaza cel mai mic numar care are ultima cifră egală cu o cifră citită de la tastatură.
    4.Afișarea tuturor numerelor din listă care sunt superprime
    5.Afișarea listei obținute din lista inițială în care numerele pozitive și nenule au fost înlocuite cu  CMMDC-ul lor și numerele negative au cifrele în ordine inversă
    6.Exit menu""")


def interactive_menu():
    lst_data = []
    while True:
        show_options()
        option = input("Your option is:")
        if option == '1':
            lst_data = read_input_elements()[:]
            print(f'Input list is {lst_data}')
        elif option == '2':
            print(f'Negatives from list are:{get_all_negatives(lst_data)}')
        elif option == '3':
            last_digit_option(lst_data)
        elif option == "4":
            print(f'All super primes are {get_all_super_primes(lst_data)}')
        elif option == "5":
            print(
                f'Result after replace is {replace_positives_with_biggest_common_factor_and_negatives_with_mirror(lst_data)}')
        elif option == "6":
            break
        else:
            print("Unknown option, try again.")
    print("Exiting the menu.")


test_all()
interactive_menu()
