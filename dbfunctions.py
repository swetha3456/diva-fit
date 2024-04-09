import sqlite3

def init_db():
    with open("create_database.sql") as f:
        script = f.read()

    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.executescript(script)
    conn.commit()
    conn.close()

def authenticate_user(username, password):
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    try:
        expected_password = list(cursor.execute(f"select password from users where username='{username}';"))[0][0]
    except:
        return False
    
    conn.close()
    return password == expected_password

def register_user(context):
    command = f"""insert into users values(
        '{context["username"]}',
        '{context["password"]}',
        {context["age"]},
        {context["weight"]},
        {context["cycle_length"]},
        {context["period_duration"]},
        '{context["date"]}',
        '{context["difficulty"]}',
        '{context["goals"]}',
        '{context["conditions"]}'
    );"""

    print(command)
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute(command)
    conn.commit()
    conn.close()

def get_details(username):
    command = f"select age, julianday(next_period_start_date) - julianday('now'), avg_cycle_length, avg_period_duration, fitness_goals from users where username='{username}';"

    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    output = list(cursor.execute(command))

    age = output[0][0]
    if age < 18: age_group = "teen"
    elif age < 40: age_group = "adult"
    else: age_group = "old"

    days_till_next_period = output[0][1]
    avg_cycle_length = output[0][2]
    avg_period_duration = output[0][3]
    goals = output[0][4]

    while days_till_next_period < 0: 
        days_till_next_period += avg_cycle_length

    if days_till_next_period > avg_cycle_length - avg_period_duration: phase = "menstrual"
    elif days_till_next_period > avg_cycle_length // 2: phase = "follicular"
    elif days_till_next_period > avg_cycle_length // 2 - 2: phase = "ovulation"
    else: phase = "luteal"

    return age_group, phase, goals

def days_left(username):
    command = f"select julianday(next_period_start_date) - julianday('now'), avg_cycle_length from users where username='{username}'"

    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    output = list(cursor.execute(command))[0]
    print(output)
    num_days = int(output[0])
    cycle_length = output[1]

    while num_days < 0:
        num_days += cycle_length

    return num_days, num_days / cycle_length * 100    

if __name__ == "__main__":
    init_db()