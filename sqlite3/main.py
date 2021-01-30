import database_functions.py

# show all records
db_exercise.show_all()

# add one record
db_exercise.add_one('Can', 'Ulusoy', 'can@ulusoy.com')

# delete one record based on its rowid
db_exercise.delete_one('5')  # !Delete record use rowid as string, if you use integer you get an error!

# add many records
add_my_list = [
    ('Eva', 'Liva', 'eva@liva.com'),
    ('Lena', 'Brady', 'lena@brady.com')
]

db_exercise.add_many(add_my_list)

# finds the email with where clause
db_exercise.find_email('nedim@can.com')
