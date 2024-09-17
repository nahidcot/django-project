from django.db import models

class Message(models.Model):
    text = models.CharField(max_length=255)

    def __str__(self):
        return self.text

class ProfitCalculation(models.Model):
    case = models.CharField(max_length=100)
    weekly_hour = models.DecimalField(max_digits=5, decimal_places=2)
    cg_regular_weekly_hour = models.DecimalField(max_digits=5, decimal_places=2)
    cg_weekly_ot_hour = models.DecimalField(max_digits=5, decimal_places=2)
    cg_rate = models.DecimalField(max_digits=5, decimal_places=2)
    case_monthly_hour = models.DecimalField(max_digits=5, decimal_places=2)
    cg_regular_monthly_hour = models.DecimalField(max_digits=5, decimal_places=2)
    cg_monthly_ot_hour = models.DecimalField(max_digits=5, decimal_places=2)
    select_rbs = models.CharField(max_length=50)  # Use 'Common' for now
    reimbursement_county = models.CharField(max_length=100)  # Use 'All' for now
    select_modifier = models.CharField(max_length=10, choices=[('UA', 'UA'), ('UB', 'UB'), ('UC', 'UC')])
    select_rate_code = models.CharField(max_length=10)
    monthly_reimbursement = models.DecimalField(max_digits=10, decimal_places=2)
    insurance_pay_rate = models.DecimalField(max_digits=10, decimal_places=2)
    insurance_pay_rate_reimb = models.DecimalField(max_digits=10, decimal_places=2)
    hourly_pay_with_rbs = models.DecimalField(max_digits=10, decimal_places=2)
    cg_regular_payment = models.DecimalField(max_digits=10, decimal_places=2)
    cg_ot_payment = models.DecimalField(max_digits=10, decimal_places=2)
    total_cg_pay = models.DecimalField(max_digits=10, decimal_places=2)
    cg_payment_plus_22 = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.case
