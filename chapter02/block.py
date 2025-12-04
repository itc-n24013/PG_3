name="Mary"
#password="swordfish" #あえてコメントアウト
print("パスワードを入力してください", end="")
password=input()
if name == "Mary":
    print("Maryさん、こんにちは！")
    if password == "swordfish":
        print("認証しました")
    else:
        print("パスワードが間違ってます")
else:
    print("名前が間違っているようです")