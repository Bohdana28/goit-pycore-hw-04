
def get_cats_info(path):
    cats = []
    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                line = line.strip()
                if line:
                    try:
                        cat_id, name, age = line.split(',')
                        cat_dict = {"id": cat_id, "name": name, "age": age}
                        cats.append(cat_dict)
                    except ValueError:
                        print(f"String form is incorrect: '{line}' skipped.")
        return cats
    except FileNotFoundError:
        print(f"File by path '{path}' don't found")
        return []
    except Exception as e:
        print(f"Error: {e}")
        return []   




cats_info = get_cats_info("./cats_file.txt")
print(cats_info)
