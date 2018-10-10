from django.db import models

import json


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
    
    def as_dict(self, query=None):
        
        if query == 'daily-expenses':
            
            return {
                'revenue_items': eval(self.revenue_items),
                'expense_items': eval(self.expense_items),
                'total_revenue': self.total_revenue,
                'total_expenses': self.total_expenses
            }
        
        return {
            
            'revenue_items': eval(self.revenue_items),
            'expense_items': eval(self.expense_items),
            'order_percentages': eval(self.order_percentages),
            'total_revenue': self.total_revenue,
            'total_expenses': self.total_expenses
            
        }
