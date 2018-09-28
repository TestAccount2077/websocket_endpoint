from django.db import models

class Data(models.Model):
    
    revenue_items = models.TextField()
    expense_items = models.TextField()
    
    order_percentages = models.TextField()
    
    @property
    def total_revenue(self):
        
        revenue_items = eval(self.revenue_items)
        
        return sum([item['balance_change'] for item in revenue_items])
    
    @property
    def total_expenses(self):
        
        expense_items = eval(self.expense_items)
        
        return sum([item['balance_change'] for item in expense_items])
