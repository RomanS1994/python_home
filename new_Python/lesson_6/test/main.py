from joke import get_random_joke

def main():
    name = input('Введи своє ім\'я >>> ')
    print(f"Привіт, {name}!!! Можу запропонувати анекдот? так/ні")
    
    while True:
        answer = input('так/ні >>> ').lower()
        
        if answer == 'так':
            print(f"Ваш анекдот - {get_random_joke()}")
            print(f"{name}, бажаєш прочитати ще анекдот? так/ні")
        elif answer == 'ні':
            print(f"До побачення, {name}!")
            break
        else:
            print('Твоя відповідь не вірна. Будь ласка, введи "так" або "ні".')

if __name__ == "__main__":
    main()
