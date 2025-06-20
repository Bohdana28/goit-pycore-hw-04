
def total_salary(path) :
    try:
        with open(path, 'r', encoding="utf-8") as file:
            salaries = []
            for line in file:
                line = line.strip()
                if line:
                    try:
                        name, salary = line.split(',')
                        salaries.append(int(salary))
                    except ValueError:
                        print(f"Strinf form is incorrect: '{line}' -skipped.")
        if not salaries:
            return 0, 0
        total = sum(salaries)
        average = total // len(salaries)
        return total, average
    except FileNotFoundError:
        print(f"File by path '{path}' don't found")
        return 0, 0
    except Exception as e:
        print(f"Error: {e}")
        return 0, 0                    






total, average = total_salary("./salary_file.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")