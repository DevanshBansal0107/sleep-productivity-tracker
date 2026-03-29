from model import train_model
from utils import load_model, predict

def menu():
    print("\n===== Sleep & Productivity Tracker =====")
    print("1. Train Model")
    print("2. Predict Productivity")
    print("3. Exit")

while True:
    menu()
    choice = input("Enter choice: ")

    if choice == "1":
        train_model()

    elif choice == "2":
        try:
            model = load_model()

            sleep = float(input("Sleep hours: "))
            study = float(input("Study hours: "))
            screen = float(input("Screen time: "))
            stress = int(input("Stress level (1-10): "))

            result = predict(model, sleep, study, screen, stress)

            print(f"\n📊 Predicted Productivity: {round(result, 2)}")

        except:
            print("⚠ Train the model first!")

    elif choice == "3":
        print("Exiting...")
        break

    else:
        print("Invalid choice!")
