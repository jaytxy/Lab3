import employee_info

employee_data = [
    {"name": "John", "age": 30, "department": "Sales", "salary": 50000},
    {"name": "Jane", "age": 25, "department": "Marketing", "salary": 60000},
    {"name": "Mary", "age": 23, "department": "Marketing", "salary": 56000},
    {"name": "Chloe",  "age": 35, "department": "Engineering", "salary": 70000},
    {"name": "Mike", "age": 32, "department": "Engineering", "salary": 65000},
    {"name": "Peter", "age": 40, "department": "Sales", "salary": 60000}
]
def test_get_employees_by_age_range():
    input_arr = employee_info.get_employees_by_age_range(28,35)
    test_arr = [{'name': 'John', 'age': 30, 'department': 'Sales', 'salary': 50000}, {'name': 'Mike', 'age': 32, 'department': 'Engineering', 'salary': 65000}]

    assert(input_arr == test_arr)

def test_calculate_average_salary():
    result = employee_info.calculate_average_salary()
    assert(result == 30.833333333333332)

def test_get_employees_by_dept():
    input_arr = employee_info.get_employees_by_dept("Sales")
    test_arr = [{'name': 'John', 'age': 30, 'department': 'Sales', 'salary': 50000}, {'name': 'Peter', 'age': 40, 'department': 'Sales', 'salary': 60000}]
    assert(input_arr == test_arr)




