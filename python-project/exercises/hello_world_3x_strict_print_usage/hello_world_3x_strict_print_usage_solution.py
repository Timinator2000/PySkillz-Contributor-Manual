# Only two of the suggested solutions make only 1 call to print:

# 2️⃣ Multi-Line String
message = '''

Hello, World!
Hello, World!
Hello, World!

'''.strip()

def hello_world_3x_strict_print_usage() -> None:
    print(message)


# 5️⃣ Joining a List
def hello_world_3x_strict_print_usage_alt() -> None:
    print("\n".join(["Hello, World!"] * 3))
