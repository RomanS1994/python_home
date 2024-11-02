from app_classes.user import User
from helper_functions.salery_helpers import calculate_salaries

john = User("John", 1000)
jack = User("Jack", 2000)



print(calculate_salaries([john, jack]))
