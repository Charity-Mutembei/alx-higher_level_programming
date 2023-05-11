from calculator_1 import add, sub, mul, div

a = 10
b = 5

if __name__ == "__main__":
    # calc_add = add(a, b)
    print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))
    # calc_sub = sub(a, b)
    print("{:d} - {:d} = {:d}".format(a, b, sub(a, b)))
    # calc_mul = mul(a, b)
    print("{:d} * {:d} = {:d}".format(a, b, mul(a, b)))
    # calc_div = div(a, b)
    print("{:d} / {:d} = {:d}".format(a, b, div(a, b)))
