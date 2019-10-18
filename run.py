import curve_patterns
import l_system


if __name__ == '__main__':

    curve_names = list()

    for curve_name in dir(curve_patterns):
        if curve_name.startswith('__'):
            break
        curve_names.append(curve_name)

    print('Choose any curve pattern:')
    for i, curve_name in enumerate(curve_names, 1):
        print(f"{i}. {curve_name.replace('_', ' ')}")

    selected_curve_name = curve_names[int(input('Enter the number: '))-1]
    selected_curve_class = getattr(curve_patterns, selected_curve_name)
    order_number = int(input('Enter the order number for the chosen curve: '))

    curve = l_system.LSystem(selected_curve_class, order_number)
    curve.run()
