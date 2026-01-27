# 🗓️ Day 2: Entering the Kingdom of Data Types

🧙‍♂️ Python Magic: The Variable Chronicles

Welcome to this beginner-friendly guide to understanding Variables in Python! This README serves as a quick-start cheat sheet for new wizards of code.

---

## 🧙‍♂️ What Are Variables?
Variables are like **labeled treasure chests**. You can put anything inside them — a number, a word, a list, or even a spell (function) — and give them a name so you can find them later.

In Python, a variable is created the moment you first assign a value to it.

## 📜 The Golden Rules of Naming Variables

### ✅ Do's:
* **Start with a letter or underscore**
  * `name = "Py"` ✅
  * `_secret = 123` ✅
* **Use letters, numbers, and underscores**
  * `player_score = 100` ✅
  * `item_count_2 = 5` ✅
* **Make names descriptive and clear**
  * `user_age = 25` ✅
  * `total_price = 99.99` ✅
* **Use snake_case for readability**
  * `my_favorite_color = "blue"` ✅

### ❌ Don'ts:
* **Don’t start with a number** (`1st_try` ❌)
* **Don’t use spaces or special characters** (`my variable` ❌ or `price@item` ❌)
* **Don’t use Python keywords** (`class`, `if`, `for`, `while` ❌)
* **Avoid confusing letters** like `l`, `O`, and `I`.

---

## 🎭 The Four Guardians of Variable Types

1. **The Keeper of Numbers** 🔢
   * `int`: Whole numbers (e.g., `age = 21`)
   * `float`: Decimals (e.g., `temp = 36.6`)

2. **The Scribe of Text** 📜
   * `str`: Text inside quotes (e.g., `greeting = "Hello!"`)

3. **The Judge of Truth** ⚖️
   * `bool`: Only `True` or `False` (e.g., `is_active = True`)

4. **The Collector of Many** 🗂
   * `list`: Ordered items `["apple", "banana"]`
   * `dict`: Key-value pairs `{"name": "Py", "level": 5}`

---

## 🧪 Practice Lab
Save this code to a file named `variables.py` and run it:

```python
# 🏷️ Step 1: Create your first variable
magic_word = "Abracadabra"

# 🧮 Step 2: Store numbers
wizard_level = 5
spell_power = 78.9

# 🔁 Step 3: Change a variable’s value
wizard_level = 6  # You leveled up!

# 🧾 Step 4: Use variables together
total_power = wizard_level * spell_power

# 🖨️ Step 5: See what’s inside
print("Wizard Level:", wizard_level)
print("Total Power:", total_power)

```
# 🏰 The Kingdom of Data Types

In the land of Pythonia, every piece of information belongs to a specific **Guild**. Each guild has its own unique magic, strengths, and limitations.

---

## 1. The Guild of Numeria (The Mathematicians)
Numerians handle everything that can be calculated, counted, or measured.

* **Integers (`int`):** The **"Whole Knights."** They represent solid, unbreakable numbers. No decimals allowed.
  * *Use for:* Counting gold coins, number of enemies, or player levels.
  * *Example:* `10`, `-5`, `1000`
* **Floats (`float`):** The **"Measurers."** They carry a decimal point to handle precise details.
  * *Use for:* Weight of a potion, distance to a castle, or percentage of health.
  * *Example:* `98.6`, `1.0`, `-0.005`



---

## 2. The Scribes of Textos (The Storytellers)
The Scribes manage the language and communication of the kingdom.

* **Strings (`str`):** The **"Scroll Keepers."** Anything wrapped in quotes is a string. They can hold letters, numbers, and symbols, but they are treated as text.
  * *Power:* You can join them together (Concatenation). `"Fire" + "ball"` becomes `"Fireball"`.
  * *Example:* `"Hello, Traveler!"`, `'12345'`, `"True"`

---

## 3. The Order of Truth (The Judges)
The Judges see the world without any shades of gray. They are the foundation of all logic.

* **Booleans (`bool`):** There are only two members in this guild: **True** and **False**.
  * *Use for:* Checking if a gate is locked, if a player is alive, or if a quest is finished.
  * *Example:* `True`, `False`



---

## 4. The Grand Archivists (The Collectors)
When information becomes too heavy for one person, the Archivists provide powerful containers.

* **Lists (`list`):** The **"Market Baskets."** An ordered collection that is **changeable**. You can add or remove items at any time.
  * *Syntax:* Uses square brackets `[]`.
  * *Example:* `["Sword", "Shield", "Potion"]`
* **Tuples (`tuple`):** The **"Stone Tablets."** An ordered collection that is **immutable** (cannot be changed once created).
  * *Syntax:* Uses parentheses `()`.
  * *Example:* `(latitude, longitude)`
* **Dictionaries (`dict`):** The **"Library Index."** A collection that maps a **Key** to a **Value**.
  * *Syntax:* Uses curly braces `{}`.
  * *Example:* `{"Name": "Zara", "Level": 10}`



---

## 🧪 The Alchemist's Lab
How do you know which guild a piece of data belongs to? You use the `type()` spell!

```python
print(type(42))           # <class 'int'>
print(type(3.14))         # <class 'float'>
print(type("Magic"))      # <class 'str'>
print(type(True))         # <class 'bool'>
print(type([1, 2, 3]))    # <class 'list'>
```

