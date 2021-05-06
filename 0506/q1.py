a = "Life is too short, you need python"

if "wife" in a: print("wife")
elif "python" in a and "you" not in a: print("python")
elif "shirt" not in a: print("shirt") # 조건이 하나라도 맞으면 밑에는 실행하지 않음.
elif "need" in a: print("need")
else: print("none")
