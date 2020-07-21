admin_logins = [{'user_name': 'X560395', 'password': 'hunter2'}]
#Grant Parker, Bobby Sharp, Ian Fair, Lucas Elmore, Houston Walley
#Software Modeling and Design COMP 3700


class User:
    def __init__(self, user_name, pass12, permissions):
        self.userName = user_name
        self.password = pass12
        self.permissions = permissions
        self.is_logged_in = False

    def login(self, user, passw):
        for i in range(len(admin_logins)):
            if admin_logins[i]['user_name'] == user and admin_logins[i]['password'] == passw:
                self.is_logged_in = True
                try:
                    with open('payroll.txt', 'r+') as my_file:
                        lines = my_file.readlines()
                        index = 0
                    for line in lines:
                        if index % 3 == 0:
                            fields = line.split('\t')
                            if len(fields) > 1:
                                in_name = fields[0]
                                in_address = fields[1]
                                in_base_pay = fields[2]
                                in_pay_rate = fields[3]
                                in_distribution = fields[5]
                                in_time_served = fields[4]
                                in_emp_type = fields[6]
                                employee = Employee(in_name, in_address, float(in_base_pay), in_pay_rate,
                                                    int(in_time_served), in_distribution, in_emp_type)
                                employees.append(employee)
                        elif index % 3 == 1:
                            fields = line.split('\t')
                            for i in range(len(fields)):
                                d_string = fields[i]
                                parameters = d_string.split(',')
                                if len(parameters) == 3:
                                    deduction_name = parameters[0]
                                    deduction_type = parameters[1]
                                    deduction_amount = parameters[2]
                                    employee.add_deduction(deduction_name, deduction_type, float(deduction_amount))
                        else:
                            fields = line.split('\t')
                            for i in range(len(fields)):
                                p_string = fields[i]
                                parameters = p_string.split(',')
                                if len(parameters) > 1:
                                    #employee_in = parameters[0]
                                    new_id = parameters[1]
                                    new_taxes_paid = float(parameters[2])
                                    new_charity = float(parameters[3])
                                    new_remuneration = float(parameters[4])
                                    new_overtime = float(parameters[5])
                                    new_retirement = float(parameters[6])
                                    new_other_bp = float(parameters[7])
                                    new_other_d = float(parameters[8])
                                    new_hours_worked = int(parameters[9])
                                    paystub_in = PayStub(employee, new_id, new_taxes_paid, new_charity,
                                                         new_remuneration, new_overtime, new_retirement,
                                                         new_other_bp, new_other_d, new_hours_worked)
                                    employee.add_paystub(paystub_in)

                        index = index + 1
                        print()
                except IOError:
                    continue

        if self.is_logged_in:
            print('\nSuccessfully logged in!')
        else:
            print('\nInvalid credentials, please try again.')

    def logout(self):
        f = open('payroll.txt', 'w+')
        for Employee in employees:
            employee_info = Employee.name + "\t" + Employee.address + "\t" + str(Employee.basePay) + "\t" \
                            + str(Employee.payRate) + "\t" + str(Employee.timeServed) + "\t" + Employee.distribution\
                            + "\t" + Employee.employmentType
            f.write(employee_info)
            deductions = ""
            paystubs = ""
            for Deduction in Employee.deduct_list:
                deductions += f"{Deduction.name},{Deduction.type},{Deduction.amount}\t"
            f.write(deductions + "\n")
            for paystub in Employee.paystub_list:
                paystubs += paystub.employee.name + "," + paystub.id + ","  + str(paystub.taxesPaid) + ","\
                            + str(paystub.charity) + ","  + str(paystub.remuneration) + ","  + str(paystub.overtime)\
                            + ","  + str(paystub.retirement) + "," + str(paystub.otherBP) + "," + str(paystub.otherD)\
                            + "," + str(paystub.hoursWorked) + "\t"
            f.write(paystubs + "\n")
        exit()

    def addEmployee(self):
        print("\nYou have chosen to add an employee.\n")
        name = input("Name: ")
        address = input("Address: ")
        pay_period = None
        print("\nPay Rate: ")
        print("\n[0] Hourly"
              "\n[1] Fortnightly"
              "\n[2] Monthly\n")
        option = input("Enter your option: ")
        pay_rate = ""
        if option == '0':
            pay_rate = "Hourly"
        elif option == '1':
            pay_rate = "Fortnightly"
        elif option == '2':
            pay_rate = "Monthly"
        else:
            print("\nInvalid Option. Please try again.")
        time_served = 0
        base_pay = float(input("Enter base pay: "))
        print("\nPayment Distribution Method: ")
        print("\n[0] Cash"
              "\n[1] Check"
              "\n[2] Direct Deposit\n")
        option = input("Enter your option: ")
        distribution = ""
        if option == '0':
            distribution = "Cash"
        elif option == '1':
            distribution = "Check"
        elif option == '2':
            routing_number = input("\nPlease enter routing number: ")
            account_number = input("\nPlease enter account number: ")
            bank_details = routing_number + ":" + account_number
            distribution = bank_details
        else:
            print("\nInvalid Option. Please try again.")

        print("\nEmployment Type: ")
        print("\n[0] Temporary"
              "\n[1] Permanent\n")
        option = input("Enter your option: ")
        employment_type = ""
        if option == '0':
            employment_type = "Temporary"
            new_employee = Employee(name, address, base_pay, pay_rate,
                                    time_served, distribution, employment_type)
            employees.append(new_employee)
            print(f"\nEmployee {new_employee.name} has been created!")
        elif option == '1':
            employment_type = "Permanent"
            new_employee = Employee(name, address, base_pay, pay_rate,
                                    time_served, distribution, employment_type)
            employees.append(new_employee)
            print(f"\nEmployee {new_employee.name} has been created!")
        else:
            print("\nInvalid Option. Please try again.")

    def add_employee(self):
        print("\nYou have chosen to add an employee.\n")
        name = input("Name: ")
        address = input("Address: ")
        pay_period = None
        print("\nPay Rate: ")
        print("\n[0] Hourly"
            "\n[1] Fortnightly"
            "\n[2] Monthly\n")
        option = input("Enter your option: ")
        pay_rate = ""
        if option == '0':
            pay_rate = "Hourly"
        elif option == '1':
            pay_rate = "Fortnightly"
        elif option == '2':
            pay_rate = "Monthly"
        else:
            print("\nInvalid Option. Please try again.")
        time_served = 0
        base_pay = float(input("Enter base pay: "))
        print("\nPayment Distribution Method: ")
        print("\n[0] Cash"
            "\n[1] Check"
            "\n[2] Direct Deposit\n")
        option = input("Enter your option: ")
        distribution = ""
        if option == '0':
            distribution = "Cash"
        elif option == '1':
            distribution = "Check"
        elif option == '2':
            routing_number = input("\nPlease enter routing number: ")
            account_number = input("\nPlease enter account number: ")
            bank_details = routing_number + ":" + account_number
            distribution = bank_details
        else:
            print("\nInvalid Option. Please try again.")

        print("\nEmployment Type: ")
        print("\n[0] Temporary"
            "\n[1] Permanent\n")
        option = input("Enter your option: ")
        employment_type = ""
        if option == '0':
            employment_type = "Temporary"
            new_employee = Employee(name, address, base_pay, pay_rate,
                                    time_served, distribution, employment_type)
            employees.append(new_employee)
            print(f"\nEmployee {new_employee.name} has been created!")
        elif option == '1':
            employment_type = "Permanent"
            new_employee = Employee(name, address, base_pay, pay_rate,
                                    time_served, distribution, employment_type)
            employees.append(new_employee)
            print(f"\nEmployee {new_employee.name} has been created!")
        else:
            print("\nInvalid Option. Please try again.")


    def edit_employee(self, employee_to_edit):
        print ("Employee edit options"
               "\n[0] Change Name"
               "\n[1] Change Address"
               "\n[2] Change Pay Rate"
               "\n[3] Change Distribution"
               "\n[4] Change Base Pay"
               "\n[5] Add Deduction"
               "\n[6] Remove Deduction"
               "\n[7] Add Paystub\n")
        option = input("Enter your option: ")
        if option == '0':
            user_input = input("Enter the new name: ")
            employee_to_edit.change_name(user_input)
            print("Employee name changed.")
        elif option == '1':
            user_input = input("Enter the new address: ")
            thisEmployee.change_address(user_input)
            print("Employee name changed.")
        elif option == '2':
            user_input = input("Enter the pay rate: ")
            thisEmployee.change_pay_rate(user_input)
            print("Employee pay rate changed.")
        elif option == '3':
            user_input = input("Enter the new distribution type: ")
            thisEmployee.change_distribution(user_input)
            print("Employee distribution type changed.")
        elif option == '4':
            user_input = input("Enter the new base pay: ")
            thisEmployee.change_base_pay(float(user_input))
            print("Employee base pay changed.")
        elif option == '5':
            user_input = input("Enter the new deduction: ")
            new_amount = float(input("Enter the deduction amount: "))
            new_type = input("Enter the deduction type: ")
            thisEmployee.add_deduction(user_input, new_type, new_amount)
            print("Deduction added.")
        elif option == '6':
            user_input = input("Enter the name of the deduction to be removed: ")
            thisEmployee.remove_deduction(user_input)
        elif option == '7':
            id_in = input("Enter the Paystub's Pay Period: ")

            if thisEmployee.employmentType == "Hourly":
                hours_in = int(input("Enter the hours worked (excluding overtime): "))
            else:
                hours_in = 0

            taxes_paid_in = 0
            charity_in = 0
            retirement_in = 0
            other_d_in = 0
            for deduction in thisEmployee.deduct_list:
                if deduction.type == "charity":
                    charity_in += deduction.amount
                elif deduction.type == "retirement":
                    retirement_in += deduction.amount
                elif deduction.type == "taxes":
                    taxes_paid_in += deduction.amount
                else:
                    other_d_in += deduction.amount
            overtime_in = float(input("Enter the overtime pay: "))
            remuneration_in = int(input("Enter any remuneration this employee has received: "))
            other_bp_in = int(input("Enter any other bonus pay for this pay period: "))
            new_paystub = PayStub(thisEmployee, id_in, taxes_paid_in, charity_in, remuneration_in,
                              overtime_in, retirement_in, other_bp_in, other_d_in, hours_in)
            thisEmployee.add_paystub(new_paystub)
            print("Paystub added.")
        else:
            print("Invalid option, please try again.")

    def remove_employee(self, employee_to_remove):
        user_input = input(f"Employment status of {employee_to_remove.name} will be set to "
                           f"inactive. Continue? (Y/N): ")
        if user_input == 'Y' or user_input == 'y':
            employee_to_remove.employmentType = "Inactive"
            print(employee_to_remove.name + " is now inactive.")

    def generate_report(self, report_employee):
        print("\nChoose Report to Display")
        print("\n[0] Employee Report"
              "\n[1] Paystub Report\n")
        option = input("Enter your option: ")
        if option == '0':
            print(f"\nName: {report_employee.name}"
                  f"\nAddress: {report_employee.address}"
                  f"\nBase Pay: {report_employee.basePay}"
                  f"\nTime Served: {report_employee.timeServed}"
                  f"\nPayment Distribution Method: {report_employee.distribution}"
                  f"\nEmployment Type: {report_employee.employmentType}"
                  f"\nDeductions: ")
            for deduction in report_employee.deduct_list:
                print(f"Deduction name: {deduction.name}"
                      f"\nDeduction type: {deduction.type}"
                      f"\nDeduction amount: {deduction.amount}\n")

        elif option == '1':
            start_date = input("Enter a pay period start date: ")
            for i in range(len(report_employee.paystub_list)):
                thisPayPeriod = report_employee.paystub_list[i]
                if thisPayPeriod.id == start_date:
                    print(f"Pay period {thisPayPeriod.id}:\n"
                          f"Income: {thisPayPeriod.income_total}\n"
                          f"Total deductions: {thisPayPeriod.deductions}\n"
                          f"Total charity deductions: {thisPayPeriod.charity}\n"
                          f"Total retirement deductions: {thisPayPeriod.retirement}\n"
                          f"Total taxes paid: {thisPayPeriod.taxesPaid}\n"
                          f"Total other deductions: {thisPayPeriod.otherD}\n"
                          f"Total bonus pay: "
                          f"{thisPayPeriod.overtime + thisPayPeriod.remuneration + thisPayPeriod.otherBP}\n"
                          f"Total overtime pay: {thisPayPeriod.overtime}\n"
                          f"Total remuneration bonus: {thisPayPeriod.remuneration}\n"
                          f"Total other bonus pay: {thisPayPeriod.otherBP}\n"
                          )
                    break
        else:
            print("\nInvalid Option. Please try again.")

class PayStub:
    def __init__(self, employee, id, taxes_paid, charity, remuneration, overtime, retirement, other_bp,
                 other_d, hours_worked):
        self.taxesPaid = taxes_paid
        self.employee = employee
        self.id = id
        self.charity = charity
        self.remuneration = remuneration
        self.overtime = overtime
        self.retirement = retirement
        self.otherBP = other_bp
        self.otherD = other_d
        self.hoursWorked = hours_worked
        if employee.employmentType == "Hourly":
            self.income = employee.basePay * hours_worked
        else:
            self.income = employee.basePay
        self.deductions = taxes_paid + charity + other_d + retirement
        self.income_total = remuneration + overtime + other_bp + self.income
        self.take_home_pay = self.income_total - self.deductions

class Deduction:
    def __init__(self, name, type, amount):
        self.name = name
        self.type = type
        self.amount = amount

class Employee:
    def __init__(self, name, address, base_pay, pay_rate, time_served,
                 distribution, employment_type):
        self.name = name
        self.address = address
        self.basePay = base_pay
        self.payRate = pay_rate
        self.timeServed = time_served
        self.distribution = distribution
        self.employmentType = employment_type
        self.deduct_list = []
        self.paystub_list = []

    def change_distribution(self, dist):
        self.distribution = dist

    def add_deduction(self, deduct, type, amount):
        new_deduction = Deduction(deduct, type, amount)
        self.deduct_list.append(new_deduction)

    def remove_deduction(self, which_deduct):
        for i in range(len(self.deduct_list)):
            if self.deduct_list[i].name == which_deduct:
                del self.deduct_list[i]
                print("Deduction removed.")
                return

        print("Deduction not found.")

    def change_name(self, name):
        self.name = name

    def change_address(self, address):
        self.address = address

    def change_employment_type(self, new_type):
        self.employmentType = new_type

    def change_pay_rate(self, new_rate):
        self.payRate = new_rate

    def change_base_pay(self, new_pay):
        self.basePay = new_pay

    def add_paystub(self, paystub):
        self.paystub_list.append(paystub)


if __name__ == '__main__':
    employees = []
    print("\nWelcome to the Employee PayRoll System!\n")
    username = input("Username: ")
    password = input("Password: ")
    user0 = User(username, password, 'admin')
    user0.login(username, password)
    while not user0.is_logged_in:
        username = input("Username: ")
        password = input("Password: ")
        user0.login(username, password)

    exitSystem = False
    while not exitSystem:
        print("\n[0] Add Employee "
              "\n[1] Employee List "
              "\n[2] Logout\n")
        option = input("Enter your option: ")
        if option == '0':
            user0.add_employee()
        elif option == '1':
            print("\nYou have chosen to view the employee list.\n")
            for i in range(len(employees)):
                print(f"[{i}] {employees[i].name}")
            print(f"[{len(employees)}] Return\n")
            option = input("Enter your option: ")

            if option == f"{len(employees)}":
                continue
            else:
                thisEmployee = employees[int(option)]
                print(f"\nYou are viewing {thisEmployee.name}")
                print("\n[0] Generate Report"
                      "\n[1] Edit Employee"
                      "\n[2] Remove Employee"
                      "\n[3] Return\n")
                option = input("Enter your option: ")
                if option == '0':
                    user0.generate_report(thisEmployee)
                elif option == '1':
                    user0.edit_employee(thisEmployee)
                elif option == '2':
                    user0.remove_employee(thisEmployee)
                elif option == '3':
                    continue
                else:
                    print("\nInvalid Option. Please try again.")

        elif option == '2':
            user0.logout()
        else:
            print("\nInvalid Option. Please try again.")
