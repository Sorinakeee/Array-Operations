from os import system
import random
import csv

class ArrayOperations:

    def __init__(self, elements = None):
        if elements is None:
            self.array = []
        else:
            self.array = elements

    def __str__(self):
        rez = ""
        for i in range(len(self.array)):
            rez = rez + f"{self.array[i]} "
        return rez

    def add_element(self, element):
        self.array.append(element)
        print("Element has been added to the array.")

    def show_array(self):
        for i in range(len(self.array)):
            print(self.array[i], end = " ")
        print()

    def generate_random_array(self, noOfElements, lowerLimit, upperLimit):
        for i in range(noOfElements):
            num = random.randint(lowerLimit, upperLimit)
            self.array.append(num)

    
    def remove_elements_algorithmic(self):
        length = len(self.array)
        k = 0
        while k < length:
            elem = self.array[k]
            i = k+1
            while i < length:
                if elem == self.array[i]:
                    
                    for j in range(i, length - 1):
                        self.array[j] = self.array[j+1]
                    length = length - 1
                else:
                    i = i + 1
            k = k + 1
        self.array = self.array[:length]

    def no_duplicates_array(self):
        noDuplicates = []
        noDuplicatesLength = self.array.remove_elements_algorithmic()
        for i in range(noDuplicatesLength):
            noDuplicates.append(self.array[i])
        
    def remove_duplicates_with_set(self):
        self.array = list(set(self.array))
        print("Duplicates removed from the array.")

    def remove_element_with_pop(self, element):
        if element not in self.array:
            print(f"Element {element} is not present in the array.")
        else:
            poz = self.array.index(element)
            self.array.pop(poz)
            print("Element has been deleted from the array.")
    
    def array_length(self):
        return len(self.array)

    def save_to_file(self, filename):
        with open(filename, mode= "w", newline = "") as file:
            writer = csv.writer(file)
            writer.writerow(self.array)
        print(f"Array saved to {filename}")
    
    def load_from_file(self, filename):
        try:
            with open(filename, "r") as file:
                reader = csv.reader(file)
                self.array = [int(item) for row in reader for item in row]
            print(f"Elements loaded from {filename}")
        except FileNotFoundError:
            print(f"File {filename} not found.")

    def search_element(self, element):
        if element in self.array:
            poz = self.array.index(element)
            print(f"Element found at index {poz}")
        else:
            print(f"{element} not found in array.")

    def count_element(self, element):
        found = 0
        for i in range(len(self.array)):
            if self.array[i] == element:
                found = found + 1
        print(f"Element has been found in array {found} times.")

    def ascending_sort(self):
        swapped = False
        for i in range(len(self.array) - 1):
            for j in range(len(self.array) - i - 1):
                if self.array[j] > self.array[j+1]:
                    swapped = True
                    self.array[j], self.array[j+1] = self.array[j+1], self.array[j]
        print("Array has been sorted.")

    def descending_sort(self):
        print("Array has been sorted.")
        swapped = False
        for i in range(len(self.array) - 1):
            for j in range(len(self.array) - i - 1):
                if self.array[j] < self.array[j+1]:
                    swapped = True
                    self.array[j], self.array[j+1] = self.array[j+1], self.array[j]
        
    def insert_element(self, poz, element):
        self.array.insert(poz, element)

    def find_max(self):
        maxnum = self.array[0]
        for i in range(len(self.array)):
            if maxnum < self.array[i]:
                maxnum = self.array[i]
        return maxnum

    def find_min(self):
        minnum = self.array[0]
        for i in range(len(self.array)):
            if minnum > self.array[i]:
                minnum = self.array[i]
        return minnum

    def find_second_max(self):
        maxim = self.array[0]
        second_max = self.array[1]
        for i in range(len(self.array)):
            if self.array[i] > maxim:
                second_max = maxim
                maxim = self.array[i]
            elif self.array[i] > second_max and self.array[i] != maxim:
                second_max = self.array[i]
        return second_max
    
    def find_second_min(self):
        minim = self.array[0]
        second_min = self.array[1]
        for i in range(len(self.array)):
            if self.array[i] < minim:
                second_min = minim
                minim = self.array[i]
            elif minim < self.array[i] < second_min:
                second_min = self.array[i]
        return second_min

    def average(self):
        sum = 0
        for i in range(len(self.array)):
            sum = sum + self.array[i]
        average = float(sum/len(self.array))
        average = format(average, '.2f')
        return average
