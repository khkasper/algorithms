def study_schedule(permanence_period, target_time):
    try:
        student_count = 0
        for start, end in permanence_period:
            if start <= target_time <= end:
                student_count += 1
        return student_count
    except TypeError:
        return None
