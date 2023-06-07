from  random import randint, choice

VOWELS = "aeyuoi"
CONSTAINS = "bcdfghjklmnpqrstvwxz"
def generate_files(extension: str, min_len: int = 6, max_len: int = 30, min_len_byte: int = 256,
                   max_len_byte: int = 4096, count_files: int = 42):
    for _ in range(count_files):
        rnd_string = "".join(choice(VOWELS) if i % 3 == 0 else choice(CONSTAINS)
                             for i in range(randint(min_len, max_len)))
        data = bytes(randint(0, 255) for _ in range(randint(min_len_byte, max_len_byte)))
        with open(f"{rnd_string}.{extension}", "wb") as f:
            f.write(data)