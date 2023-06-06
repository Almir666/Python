def quest(quest: str, answers: list[str]):
    print(quest)
    try_count = 1
    while True:
        answer = input("Что это? ")
        if answer in answers:
            print("Правильно!")
            break
        print("Не правильно")
        try_count += 1
    return try_count