class SalaryError(ValueError): pass


class BonusError(SalaryError): pass


class Employee:
    MIN_SALARY = 30000
    MAX_RAISE = 5000

    def __init__(self, name, salary=30000):
            self.name = name
            # If salary is too low
            if salary < Employee.MIN_SALARY:
        # Raise a SalaryError exception
                raise SalaryError("Salary is too low!")

            self.salary = salary


