# Write your code here
class BMICalculator:
    def __init__(self, weight_in_kg, height_in_m):
        self.bmi = round(weight_in_kg / height_in_m**2,2)
        self.category = ""
    
    @property
    def category(self):
        return self.__category
    
    @category.setter
    def category(self, value):
        if self.bmi < 18.5:
            self.__category = "underweight"
        elif self.bmi > 18.5 and self.bmi < 25:
            self.__category = "normal"
        else:
            self.__category = "overweight" 

    
# calc = BMICalculator(80, 1.80)
# calc.category = "no"

# print(calc.bmi)

# print(calc.category)