import json
import os


def load_tasks():
    if os.path.isfile("tasks.json"):
        try:
            with open("tasks.json", "r", encoding="utf-8") as file:
                file_reader = json.load(file)
                return file_reader
            
        except Exception:  # noqa: BLE001
            print("Файл поврежден или с ним что то не так.")
        

    return []


def save_tasks(tasks):
    with open("tasks.json", "w", encoding="utf-8") as file:
        json.dump(tasks, file, ensure_ascii=False, indent=4)


def add_task(titles):
    tasks = load_tasks()
    for title in (i.strip(' .!?:"') for i in titles.split(',')):
        if title.isdigit():
            print('Нужно название задачи')
            continue
        id = tasks[-1]["task_id"] + 1 if tasks else 1
        tasks.append({"task_id": id, "title": title, "done": False})
    save_tasks(tasks)


def list_tasks():
    task_list = load_tasks()
    if task_list:
        for task in task_list:
            task_id = task["task_id"]
            title = task["title"]
            done = task["done"]
            print("*" * max(len(title), 25))
            print(
                f"Задача под номером: {task_id}\nПод названием: {title}\n{['Не выполнена', 'Выполнена'][done]}"
            )
            print("*" * max(len(title), 25))

    else:
        print("Задачи отсутствуют, отдыхыйте!")


def mark_done(task_id):
    task_list = load_tasks()
    for task in task_list:
        if task["task_id"] == task_id:
            task["done"] = True
            print(f"Задача под номером {task_id} была помечана, как выполненная.")
            save_tasks(task_list)
            return

        print(f"Задача под номером {task_id} не была найдена.")

def delete_task(task_id):
    task_list = load_tasks()
    for task in task_list:
        if task["task_id"] == task_id:
            task_list.remove(task)
            print(f"Задача под номером {task_id} была удалена.")
            save_tasks(task_list)
            return

    print(f"Задача под номером {task_id} не была найдена.")


def main():
    commands = {1: add_task, 2: list_tasks, 3: mark_done, 4: delete_task}
    while True:
        print('Доступные команды:\n1 - Добавление задачи\n2 - Вывод текущих задач\n3 - Отметка выполненных задач\n4 - Удаление задач')

        try:
            a = int(input("Выберите задачу:"))
        except ValueError:
            print('Это не число')
            continue

        if 3 <= a <= 4:
            try:
                commands[a](int(input("Введите номер задачи: ")))
            except ValueError:
                print('Это не число')

        elif a == 1:
            commands[a](input("Введите название задач(ь\\и): "))

        elif a == 2:
            commands[a]()
        
        else:
            print('Данное число не является корректным.')


if __name__ == "__main__":
    main()
