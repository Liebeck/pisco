class Student:
    student_id = 0
    neuroticism = 0
    extroversion = 0
    openness = 0
    agreeableness = 0
    conscientiousness = 0

    def __init__(self, student_id, neuroticism, extroversion, openness, agreeableness, conscientiousness):
        self.student_id = student_id
        self.neuroticism = neuroticism
        self.extroversion = extroversion
        self.openness = openness
        self.agreeableness = agreeableness
        self.conscientiousness = conscientiousness

    def __str__(self):
        return str(vars(self))
