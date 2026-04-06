class Employee:
    def __init__(self):
        self.first_name = None
        self.last_name = None
        self.email = None
        self.department = None
        self.position = None
        self.salary = None
        self.has_laptop = False
        self.has_parking = False
        self.has_vpn_access = False
        self.has_admin_rights = False

    def __str__(self):
        return f"Employee({self.first_name} {self.last_name}, {self.position})"

class EmployeeBuilder:
    def __init__(self):
        self.employee = Employee()

    def with_name(self, first_name: str, last_name: str):
        self.employee.first_name = first_name
        self.employee.last_name = last_name
        return self

    def with_email(self, email: str):
        self.employee.email = email
        return self

    def with_job(self, department: str, position: str, salary: float):
        self.employee.department = department
        self.employee.position = position
        self.employee.salary = salary
        return self

    def with_equipment(self, laptop: bool = False, parking: bool = False):
        self.employee.has_laptop = laptop
        self.employee.has_parking = parking
        return self

    def with_access(self, vpn: bool = False, admin: bool = False):
        self.employee.has_vpn_access = vpn
        self.employee.has_admin_rights = admin
        return self

    def build(self) -> Employee:
        return self.employee

def DeveloperBuilder(first_name: str, last_name: str, email: str):
    return (EmployeeBuilder()
            .with_name(first_name, last_name)
            .with_email(email)
            .with_job("Engineering", "Developer", 70000)
            .with_equipment(laptop=True, parking=False)
            .with_access(vpn=True, admin=True))

if __name__ == "__main__":
    employee = (
        EmployeeBuilder()
        .with_name("John", "Doe")
        .with_email("john.doe@company.com")
        .with_job("Engineering", "Senior Developer", 75000)
        .with_equipment(laptop=True, parking=False)
        .with_access(vpn=True, admin=True)
        .build()
    )
    dev = DeveloperBuilder("John", "Doe", "john.doe@company.com").build()
    print(employee)
    print(dev)\n