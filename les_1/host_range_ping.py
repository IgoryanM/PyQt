"""
2. Написать функцию host_range_ping() для перебора ip-адресов из заданного диапазона.
Меняться должен только последний октет каждого адреса.
По результатам проверки должно выводиться соответствующее сообщение.
"""

from ipaddress import ip_address
from host_ping import host_ping


def host_range_ping():
    while True:
        first_ip = input('Введите первый адрес: ')
        try:
            las_oct = int(first_ip.split('.')[3])
            first_ip = ip_address(first_ip)
            break
        except Exception as e:
            print(e)

    while True:
        end_ip = input('Сколько адресов проверить?: ')
        if not end_ip.isnumeric():
            print('Необходимо ввести число!')
        else:
            if (las_oct + int(end_ip)) > 254:
                print(f"Можем менять только последний октет, т.е. "
                      f"максимальное число хостов для проверки: {254 - las_oct}")
            else:
                break

    host_list = [str(first_ip + x) for x in range(int(end_ip))]

    return host_ping(host_list)


if __name__ == "__main__":
    host_range_ping()
