from data_processor import get_high_value_customers

print('--- Customer Analysis ---')
high_value = get_high_value_customers('data/customer_feedback.csv')
print('High-Value Customers:')
print(high_value)
