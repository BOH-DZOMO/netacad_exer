class AppError(Exception):
    def __init__(self):
        self.message = ""
        super().__init__()
    def __str__(self):
        return f"[ERROR] {self.message}"

class ValidationError(AppError):
    def __init__(self,message):
        super().__init__()
        self.message = message

class DatabaseError(AppError):
    def __init__(self,message):
        super().__init__()
        self.message = message




try:
    def validate_age(age):
        if age < 0 or age > 150:
            raise ValidationError("Age -5 is invalid")
        
    if 22 not in [34,45,56,33.22]:
        raise DatabaseError("User with id 22 is not found in db")

except DatabaseError as de:
    print(de)

try:
    validate_age(500)
except ValidationError as ve:
    print(ve)