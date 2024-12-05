from flask import Flask

app = Flask(__name__)

weather = {
    "astana": -10.3,
    "almaty": -6.7,
    "vienna": -2.5,
}

todos = [
    "Brush teeth",
    "Wash dishes",
    "Buy groceries",
]

@app.route("/")
def welcome():
    return "Это моё первое API"

@app.route("/name")
def second():
    return "моё первое"

@app.route("/city/<city_name>")
def weather_by_city(city_name):

    if city_name in weather:
        return f"Текущая погода в {city_name}: {weather[city_name]}"
    else:
        return f"не найден {city_name}"

@app.route("/todos")
def todos_list():
    return f"Список: {todos}"

@app.route("/todos/new/<title>")
def add_todo(title):
    todos.append(title)
    return f"Добавлен '{title}' Текущий: {todos}"

@app.route("/todos/remove/<int:index>")
def remove_todos(index):
    
    if 0 <= index < len(todos):
        removed_todo = todos.pop(index)
        return f"Удален: {removed_todo}. Текущий список задач: {todos}"
    else:
        return f"Задание с индексом {index} не найдено"

@app.route("/todos/edit/<int:index>/<new_title>")
def edit_todo(index, new_title):
    
    if 0 <= index < len(todos):
        todos[index] = new_title
        return f"Задача с индексом {index} обновлена на '{new_title}'. Текущий список задач: {todos}"
    else:
        return f"Задача с индексом {index} не найдена"

@app.route("/todos/get/<int:index>")
def get_todo_by_index(index):

    if 0 <= index < len(todos): 
        return f"Задание: {todos[index]}"
    else:
        return "Задание не найдено"

if __name__ == "__main__":
    app.run(port=5025, host="0.0.0.0", debug=True)
