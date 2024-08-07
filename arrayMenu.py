from os import system
from arrayOperations import ArrayOperations

class ArrayOperationsMenu:
    
    def __init__(self, array):
        self.array =  array
        
    def display(self):
        print("\nArray Operations Menu:")
        print("01. Print")
        print("02. Generate random array")
        print("03. Add element")
        print("04. Remove element with pop")
        print("05. Remove duplicates with set")
        print("06. Remove duplicates algorithmic")
        print("07. Search")
        print("08. Count")
        print("09. Sort")
        print("10. Insert")
        print("11. Find maximum")
        print("12. Find second maximum")
        print("13. Find minimum")
        print("14. Find second minimum")
        print("15. Average")
        print("16. Save to file")
        print("17. Load from file")
        print("00.  Exit")
    
    def isRunning(self):
        choice = -1
        while choice != 0:
            system("cls")
            self.display()
            choice = int(input("Please select an option: "))
            if choice == 1:
                arr.show_array()
                print("Press enter to continue")
                input()
            elif choice == 2:
                elem = int(input("Insert the number of elements: "))
                lower = int(input("Insert the lower limit of the array: "))
                upper = int(input("Insert the upper limit of the array: "))
                arr.generate_random_array(elem, lower, upper)
                print("Press enter to continue")
                input()
            elif choice == 3:
                elem = int(input("Insert the number to be added: "))
                arr.add_element(elem)
                print("Press enter to continue")
                input()
            elif choice == 4:
                elem = int(input("Insert the number to be deleted: "))
                arr.remove_element(elem)
                print("Press enter to continue")
                input()
            elif choice == 5:
                arr.remove_duplicates_with_set()
                print("Press enter to continue")
                input()
            elif choice == 6:
                arr.remove_elements_algorithmic()
                print("Duplicates removed. Press enter to continue")
                input()
            elif choice == 7:
                elem = int(input("Insert the number for search: "))
                arr.search_element(elem)
                print("Press enter to continue")
                input()
            elif choice == 8:
                elem = int(input("Insert number to be counted: "))
                arr.count_element(elem)
                print("Press enter to continue")
                input()
            elif choice == 9:
                type = int(input("Press 1 for ascending sort or 2 for descending sort: "))
                if type > 2:
                    print("Invalid choice. Please try again.")
                elif type == 1:
                    arr.ascending_sort()
                    print("Array sorted.Press enter to continue")
                    input()
                elif type == 2:
                    arr.descending_sort()
                    print("Array sorted.Press enter to continue")
                    input()
            elif choice == 10:
                length = arr.array_length()
                print(f"Array has {length} elements")
                poz = int(input("The position you want the element to be added: "))
                elem = int(input("Element to be added to the array: "))
                length = arr.array_length()
                if poz > length:
                    print("Postion is  bigger than the length of the array. Element has been added tot he last position.")
                arr.insert_element(poz, elem)
                print("Press enter to continue")
                input()
            elif choice == 11:
                arrMax = arr.find_max()
                print(f"Maximum number from the array is {arrMax}. Press enter to continue")
                input()
            elif choice == 12:
                arrSecondMax = arr.find_second_max()
                print(f"Runner up from the array is {arrSecondMax}. Press enter to continue")
                input()
            elif choice == 13:
                arrMin = arr.find_min()
                print(f"Minimum number from the array is {arrMin}. Press enter to continue")
                input()
            elif choice == 14:
                arrSecondMin = arr.find_second_min()
                print(f"Second minimum from the array is {arrSecondMin}. Press enter to continue")
                input()
            elif choice == 15:
                avg = arr.average()
                print(f"Average number in the array is {avg}. Press enter to conitnue")
                input()
            elif choice == 16:
                arr.save_to_file("arrayOperationsMenu.csv")
                print("Array saved to file. Press enter to continue")
                input()
            elif choice == 17:
                arr.load_from_file("arrayOperationsMenu.csv")
                print("Array loaded from file. Press enter to continue")
                input()
            

arr = ArrayOperations()
menu = ArrayOperationsMenu(arr)
menu.isRunning()

