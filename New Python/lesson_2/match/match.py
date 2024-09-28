# ==============================================================
# match
# ==============================================================

#Задача 2: Оцінювання балів
# Створи функцію evaluate_score, яка приймає число (бал) і повертає оцінку за стандартною шкалою (A, B, C, D, F).

def evaluate_score(score):
    match score:
        case _ if score >= 90:
            return 'A'
        case _ if score >= 80:
            return 'B'
        case _ if score >= 70:
            return 'C'
        case _ if score >= 60:
            return 'D'
        case _ : 
            return 'F'
        
print(evaluate_score(95))  # A
print(evaluate_score(75))  # C
print(evaluate_score(50))  # F

 