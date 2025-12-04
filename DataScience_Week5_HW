#Question 1 - 1050. Actors and Directors Who Cooperated At Least Three Times

''' SELECT actor_id, director_id
FROM ActorDirector
GROUP BY actor_id, director_id
HAVING COUNT(*) >= 3 '''

#Pandas
import pandas as pd

def actors_and_directors(actor_director: pd.DataFrame) -> pd.DataFrame:
    grouped = actor_director.groupby(['actor_id', 'director_id'])
    counts = grouped.size()
    result = counts.reset_index(name='count')
    filtered = result[result['count'] >= 3]
    final = filtered[['actor_id', 'director_id']]
    return final

#Question 2 - 1667. Fix Names in a Table

''' SELECT user_id, CONCAT(UPPER(LEFT(name, 1)), LOWER(SUBSTRING(name, 2))) AS name
FROM Users
ORDER BY user_id '''

#Pandas
import pandas as pd

def fix_names(users: pd.DataFrame) -> pd.DataFrame:
    first_char = users['name'].str[0]
    first_upper = first_char.str.upper()
    rest_chars = users['name'].str[1:]
    rest_lower = rest_chars.str.lower()
    users['name'] = first_upper + rest_lower
    result = users.sort_values('user_id')
    return result

#Question 3 - 175. Combine Two Tables

''' SELECT p.firstName, p.lastName, a.city, a.state
FROM Person p
LEFT JOIN Address a ON p.personId = a.personId '''

#Pandas
import pandas as pd

def combine_two_tables(person: pd.DataFrame, address: pd.DataFrame) -> pd.DataFrame:
    merged = person.merge(address, on='personId', how='left')
    
    first_name = merged['firstName']
    last_name = merged['lastName']
    city = merged['city']
    state = merged['state']
    
    result = pd.DataFrame({})
    result['firstName'] = first_name
    result['lastName'] = last_name
    result['city'] = city
    result['state'] = state

#Question 4 - 176. Second Highest Salary

''' SELECT MAX(salary) AS SecondHighestSalary
FROM Employee
WHERE salary < (SELECT MAX(salary) FROM Employee) '''

#Pandas
import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    unique_salaries = employee['salary'].unique()
    sorted_salaries = sorted(unique_salaries, reverse=True)
    if len(sorted_salaries) < 2:
        result = pd.DataFrame({'SecondHighestSalary': [None]})
    else:
        second = sorted_salaries[1]
        result = pd.DataFrame({'SecondHighestSalary': [second]})
    return result

#Question 5 - 1327. List the Products Ordered in a Period

''' SELECT p.product_name, SUM(o.unit) AS unit
FROM Products p
JOIN Orders o ON p.product_id = o.product_id
WHERE o.order_date >= '2020-02-01' AND o.order_date < '2020-03-01'
GROUP BY p.product_id, p.product_name
HAVING SUM(o.unit) >= 100 '''

#Pandas
import pandas as pd

def list_products(products: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    start_date = '2020-02-01'
    end_date = '2020-03-01'
    
    order_date_col = orders['order_date']
    condition1 = order_date_col >= start_date
    condition2 = order_date_col < end_date
    filtered_orders = orders[condition1 & condition2]
    
    merged = products.merge(filtered_orders, on='product_id')
    
    grouped = merged.groupby('product_name')
    unit_sum = grouped['unit'].sum()
    result_df = unit_sum.reset_index()
    result_df.columns = ['product_name', 'unit']
    
    unit_column = result_df['unit']
    condition = unit_column >= 100
    final_result = result_df[condition]
    
    return final_result

#Question 6 - 1378. Replace Employee ID With The Unique Identifier

''' SELECT e2.unique_id, e1.name
FROM Employees e1
LEFT JOIN EmployeeUNI e2 ON e1.id = e2.id '''

#Pandas
import pandas as pd

def replace_employee_id(employees: pd.DataFrame, employee_uni: pd.DataFrame) -> pd.DataFrame:
    merged = employees.merge(employee_uni, on='id', how='left')
    unique_id_col = merged['unique_id']
    name_col = merged['name']
    result = pd.DataFrame({'unique_id': unique_id_col, 'name': name_col})
    return result

#Question 7 - 550. Game Play Analysis IV

''' SELECT ROUND(COUNT(DISTINCT a2.player_id) / COUNT(DISTINCT a1.player_id), 2) AS fraction
FROM (SELECT player_id, MIN(event_date) AS first_login FROM Activity GROUP BY player_id) a1
LEFT JOIN Activity a2 ON a1.player_id = a2.player_id AND a2.event_date = DATE_ADD(a1.first_login, INTERVAL 1 DAY) '''

#Pandas
import pandas as pd
#question 5
def gameplay_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    grouped = activity.groupby('player_id')
    first_logins = grouped['event_date'].min()
    first_logins_df = first_logins.reset_index()
    first_logins_df.columns = ['player_id', 'first_login']
    
    merged = first_logins_df.merge(activity, on='player_id', how='left')
    
    first_login_col = merged['first_login']
    one_day = pd.Timedelta(days=1)
    next_day = first_login_col + one_day
    event_date_col = merged['event_date']
    condition = event_date_col == next_day
    logged_next_day = merged[condition]
    
    player_col = first_logins_df['player_id']
    total_players = player_col.nunique()
    next_day_player_col = logged_next_day['player_id']
    next_day_players = next_day_player_col.nunique()
    
    division = next_day_players / total_players
    fraction = round(division, 2)
    
    result = pd.DataFrame({'fraction': [fraction]})
    return result

#Question 8 - 1075. Project Employees I
''' sql query -

SELECT p.project_id, ROUND(AVG(e.experience_years), 2) AS average_years
FROM Project p
JOIN Employee e ON p.employee_id = e.employee_id
GROUP BY p.project_id '''

#Pandas
import pandas as pd

def project_employees_i(project: pd.DataFrame, employee: pd.DataFrame) -> pd.DataFrame:
    merged = project.merge(employee, on='employee_id')
    
    grouped = merged.groupby('project_id')
    experience_avg = grouped['experience_years'].mean()
    result_df = experience_avg.reset_index()
    result_df.columns = ['project_id', 'average_years']
    
    avg_column = result_df['average_years']
    rounded_avg = avg_column.round(2)
    result_df['average_years'] = rounded_avg
    
    return result_df

#question 9 - 185. Department Top Three Salaries

''' SELECT d.name AS Department, e.name AS Employee, e.salary AS Salary
FROM Employee e
JOIN Department d ON e.departmentId = d.id
WHERE (
    SELECT COUNT(DISTINCT e2.salary)
    FROM Employee e2
    WHERE e2.departmentId = e.departmentId AND e2.salary > e.salary
) < 3 '''

import pandas as pd

def top_three_salaries(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    import pandas as pd

def top_three_salaries(employee, department):
    import pandas as pd

def top_three_salaries(employee, department):
    merged = employee.merge(department, left_on='departmentId', right_on='id', how='inner')
    result_list = []
    grouped = merged.groupby('departmentId')
    for dept_id, group in grouped:
        salary_col = group['salary']
        salaries = salary_col.unique()
        sorted_salaries = sorted(salaries, reverse=True)
        first_three = sorted_salaries[:3]
        top_three = list(first_three)
        
        for index, row in group.iterrows():
            emp_salary = row['salary']
            is_top = emp_salary in top_three
            if is_top:
                dept_name = row['name_y']
                emp_name = row['name_x']
                salary = row['salary']
                row_dict = {
                    'Department': dept_name,
                    'Employee': emp_name,
                    'Salary': salary
                }
                result_list.append(row_dict)
    
    result = pd.DataFrame(result_list)
    return result
    return result
