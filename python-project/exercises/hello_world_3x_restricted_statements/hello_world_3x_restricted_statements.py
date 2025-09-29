def hello_world_3x_restricted_statements() -> None:
    pass


# Or try any of the solutions below.

# 1️⃣ Three Direct Print Calls

# def hello_world_3x_restricted_statements() -> None:
#     print("Hello, World!")
#     print("Hello, World!")
#     print("Hello, World!")


# 2️⃣ Multi-Line String

# message = '''

# Hello, World!
# Hello, World!
# Hello, World!

# '''.strip()

# def hello_world_3x_restricted_statements() -> None:
#     print(message)


# 3️⃣ Using a `for` Loop

# def hello_world_3x_restricted_statements() -> None:
#     for _ in range(3):
#         print("Hello, World!")


# 4️⃣ Using a `while` Loop

# def hello_world_3x_restricted_statements() -> None:
#     i = 0
#     while i < 3:
#         print("Hello, World!")
#         i += 1


# 5️⃣ Joining a List

# def hello_world_3x_restricted_statements() -> None:
#     print("\n".join(["Hello, World!"] * 3))


# 6️⃣ One-Liner with String Multiplication

# def hello_world_3x_restricted_statements(): print(("Hello, World!\n" * 3)[:-1])


# 7️⃣ Recursion

# def hello_world_3x_restricted_statements(n=3) -> None:
#     if n > 0:
#         print("Hello, World!")
#         hello_world_3x_restricted_statements(n - 1)

