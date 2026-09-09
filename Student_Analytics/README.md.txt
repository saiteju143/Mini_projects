@app.get("/analysis")
def analysis():

    python_marks = []
    mathematics_marks = []
    data_science_marks = []

    for student in students:
        python_marks.append(student["python"])
        mathematics_marks.append(student["mathematics"])
        data_science_marks.append(student["data_science"])

    python_avg = np.mean(python_marks)
    mathematics_avg = np.mean(mathematics_marks)
    data_science_avg = np.mean(data_science_marks)

    subject_averages = {
        "Python": python_avg,
        "Mathematics": mathematics_avg,
        "Data Science": data_science_avg
    }

    highest_subject = max(
        subject_averages,
        key=subject_averages.get
    )

    lowest_subject = min(
        subject_averages,
        key=subject_averages.get
    )

    return {
        "Subject_Averages": subject_averages,
        "Highest_Average_Subject": highest_subject,
        "Lowest_Average_Subject": lowest_subject
    }