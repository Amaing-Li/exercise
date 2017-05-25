def is_ip(ip):
    numbers = ip.split(".")
    for num in numbers:
        try:
            num = int(num)
            if 1 <= num <= 255:
                continue
            else:
                return False
        except ValueError as err:
            print(err)
    return True