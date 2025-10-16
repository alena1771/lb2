# main.py
def greet(name):
    print(f"Привет, {name}!")

if __name__ == "__main__":
    greet("Алёна")
    git add .
git commit -m "Initial commit: Добавила основную структуру проекта."
git tag v0.1
echo "# Добавляем дополнительные файлы" >> file.txt
git add .
git commit -m "Добавлен вспомогательный файл."
git tag v0.2

