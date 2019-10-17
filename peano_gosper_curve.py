import turtle


def peano_gosper_curve(iter_amount):
    theta = 60
    order_set = 'X'
    rules = {
        'X': 'X+YF++YF-FX--FXFX-YF+,',
        'Y': '-FX+YFYF++YF+FX--FX-Y'
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
    peano_gosper_curve(int(input('Enter order number: ')))
