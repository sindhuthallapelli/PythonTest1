import sqlite3
conn = sqlite3.connect('database.db')
c = conn.cursor()

# Insert a test question
c.execute('''
INSERT INTO questions (question_text, class_name, section, teacher_username, time_limit)
VALUES (?, ?, ?, ?, ?)
''', ("How is GRIET hyd?", "CSE", "B", "teacher", 360))

# Get the question ID
question_id = c.lastrowid

# Insert feedback options for the question
options = ["Good", "Better", "Interactive", "Lack of Interest"]
for opt in options:
    c.execute('INSERT INTO feedback_options (question_id, option, count) VALUES (?, ?, ?)', (question_id, opt, 0))

conn.commit()
conn.close()

print("✅ Sample question and options inserted.")
