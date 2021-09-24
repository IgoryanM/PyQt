"""
1. Написать функцию host_ping(), в которой с помощью утилиты ping
будет проверяться доступность сетевых узлов.
Аргументом функции является список, в котором каждый сетевой узел
должен быть представлен именем хоста или ip-адресом.
В функции необходимо перебирать ip-адреса и проверять
их доступность с выводом соответствующего сообщения
(«Узел доступен», «Узел недоступен»). При этом ip-адрес
сетевого узла должен создаваться с помощью функции ip_address().
"""

from ipaddress import ip_address
from subprocess import Popen, PIPE


def host_ping(ip_list, timeout=500, requests=1):
    result = {'Доступные узлы': "", 'Недоступные узлы': ""}

    for addr in ip_list:
        try:
            addr = ip_address(addr)
        except ValueError:
            pass
        proc = Popen(f"ping {addr} -w {timeout} -n {requests}", stdout=PIPE)
        proc.wait()

        if proc.returncode == 0:
            result['Доступные узлы'] += f"{str(addr)}\n"
            res_string = f'{addr} - Узел доступен'
        else:
            result['Недоступные узлы'] += f"{str(addr)}\n"
            res_string = f'{addr} - Узел недоступен'
        print(res_string)
    return result


if __name__ == '__main__':
    list_ip = ['yandex.ru', '2.2.1.2', '192.168.0.100', '192.168.0.101', '194.58.104.230']
    host_ping(list_ip)
