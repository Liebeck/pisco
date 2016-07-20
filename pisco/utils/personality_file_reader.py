import csv
import os
from utils.student import Student


def read_personality_file(filename):
    path = os.path.join(os.path.dirname(__file__), '../../data/', filename)
    students = []
    with open(path, 'rb') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        next(csvreader, None)  # skip the header row
        for row in csvreader:
            new_student = Student(row[0],
                                  row[1],
                                  row[2],
                                  row[3],
                                  row[4],
                                  row[5])
            # print(new_student)
            students.append(new_student)
