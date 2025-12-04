class License:
    def __init__(self,license_num,category,date_of_expiry):
        self.license_num = license_num
        self.category = category
        self.date_of_expiry = date_of_expiry
    def is_issued(self):
        return(f"The license number {self.license_num} is issued")
    def __str__(self):
        return(f"The license number {self.license_num} is of {self.category} category and will expire on {self.date_of_expiry}")
    