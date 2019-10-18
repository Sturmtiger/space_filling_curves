import turtle


def koch_curve(iter_amount):
    theta = 90
    order_set = 'F'
    rules = {
        'F': 'F+F-F-F+F'
    }

    for _ in range(iter_amount):
        order = str()
        for i in order_set:
            if i == 'F':
                order += rules['F']
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
    koch_curve(int(input('Enter order number: ')))
