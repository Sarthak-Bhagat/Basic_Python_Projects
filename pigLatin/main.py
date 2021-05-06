def main(S:str) -> str:
    S = S.split()
    S1 = ""
    for i in S:
        S1 += f" {i[1:]}-{i[0]}ay"

    return S1

if __name__ == "__main__":
    inp = input("Enter a String\n")
    print(main(inp))
