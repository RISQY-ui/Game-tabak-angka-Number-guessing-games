# Number Guessing Game - Complete English Version

```python
import random

secret_number = random.randint(1, 100)

print("=== NUMBER GUESSING GAME (1 - 100) ===")

while True:
    guess = int(input("Guess the number: "))

    if guess < secret_number:
        print("The number is too small! Try again.\n")

    elif guess > secret_number:
        print("The number is too big! Try again.\n")

    else:
        print("🎉 Player Wins! Success!")
        print("Your guess is correct!\nThe number was", secret_number)
        break
```

---

## 📝 Line-by-Line Translation

| Indonesian | English | Explanation |
|-----------|---------|-------------|
| `import random` | `import random` | Import random module (same) |
| `angka_rahasia` | `secret_number` | The secret number variable |
| `random.randint(1, 100)` | `random.randint(1, 100)` | Generate random number (same) |
| `print("=== GAME TEBAK ANGKA (1 - 100) ===")` | `print("=== NUMBER GUESSING GAME (1 - 100) ===")` | Game title |
| `while True:` | `while True:` | Infinite loop (same) |
| `tebakan` | `guess` | User's guess variable |
| `int(input("Tebak angkanya: "))` | `int(input("Guess the number: "))` | Get user input |
| `tebakan < angka_rahasia` | `guess < secret_number` | Comparison (same concept) |
| `"Angka Kekecilan! Coba lagi.\n"` | `"The number is too small! Try again.\n"` | Message if too small |
| `tebakan > angka_rahasia` | `guess > secret_number` | Comparison (same concept) |
| `"Angka Kebesaran! Coba lagi.\n"` | `"The number is too big! Try again.\n"` | Message if too big |
| `else:` | `else:` | If guess is correct (same) |
| `"🎉 Pemain Menang! Berhasil"` | `"🎉 Player Wins! Success!"` | Win message |
| `"Tebakan kamu tepat!"` | `"Your guess is correct!"` | Correct guess message |
| `"angkanya emang"` | `"The number was"` | Reveal the number |
| `break` | `break` | Exit loop (same) |

---

## 🎮 How to Run

```bash
# Save as game.py
python game.py

# Or
python3 game.py
```

---

## 📊 Example Output

```
=== NUMBER GUESSING GAME (1 - 100) ===
Guess the number: 50
The number is too big! Try again.

Guess the number: 25
The number is too small! Try again.

Guess the number: 37
The number is too small! Try again.

Guess the number: 42
🎉 Player Wins! Success!
Your guess is correct!
The number was 42
```

---

## ✅ Concept Remains the Same

✔ Same logic
✔ Same game flow
✔ Same variables (just renamed to English)
✔ Same output format
✔ Only text/messages are translated

**Done!** 🚀
