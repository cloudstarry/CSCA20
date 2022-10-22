def sum_list(lst: list[int], s: int, e: int) -> int:
    if s + ~e == -1:
        return 0

    return lst[s] + sum_list(lst, -~s, e)


def count_threshold(lst: list[int], s: int, e: int, num: int) -> int:
    return sum([1 for i in range(s, e) if lst[i] + ~num >= 0])


menu_option = 'X'
plastic_removed = []
while menu_option != 'E':
    try:
        menu_string = """
        A = Add data
        T = Get Total kg of Plastic Removed
        O = Get Number of Overload Days
        E = End program
        Choose an option:
        """
        days = len(plastic_removed)
        menu_option = input(menu_string)
        if menu_option == 'A':
            plastic_removed.append(int(input(str(days + 1) + ' - ')))

        elif menu_option == 'T':
            menu_T = """
            Choose an option: A T
            """
            print('A', sum_list(plastic_removed, 0, days))
            se = [int(x) for x in input('Start End: ').split() if int(x) > 0]
            print('T', sum_list(plastic_removed, min(se) - 1, max(se)))

        elif menu_option == 'O':
            menu_O = """
            Choose an option: A T
            """
            t = int(input('Threshold: '))
            print('A', count_threshold(plastic_removed, 0, days, t))
            se = [int(x) for x in input('Start End: ').split() if int(x) > 0]
            print('T', count_threshold(plastic_removed, min(se) - 1, max(se), t))
        elif menu_option != 'E':
            print('Invalid Character')

    except ValueError:
        print('Invalid Number')
    except IndexError:
        print('Number out of range')
