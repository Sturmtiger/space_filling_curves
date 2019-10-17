import turtle


def hilbert_curve(iter_amount):
    theta = 90
    order_set = 'X'
    rules = {
        'X': '+YF-XFX-FY+',
        'Y': '-XF+YFY+FX-'
    }

    for _ in range(iter_amount):
        order = str()
        for i in order_set:
            if i == 'X':
                order += rules['X']
            elif i == 'Y':
                order += rules['Y']
            else:
                order += i

        order_set = order

    for i in order_set:
        if i == 'F':
            turtle.forward(10)
        elif i == '+':
            turtle.left(theta)
        elif i == '-':
            turtle.right(theta)

    turtle.done()


if __name__ == '__main__':
    hilbert_curve(int(input('Enter order number: ')))
