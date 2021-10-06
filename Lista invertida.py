def main():
    d = list(range(10))
    e = d[::-1]
    print(f'{d}\n{e}')


if __name__ == "__main__":
    main()

# ou

# def main():
#     d = list(range(10))
#     e = []
#     for i in d:
#         e.insert(0, i)
#     print(f'{d}\n{e}')


# if __name__ == "__main__":
#     main()
