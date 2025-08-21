from data_processor import get_high_value_customers

print('--- Customer Analysis ---')
high_value = get_high_value_customers('data/customer_feedback.csv')
print('High-Value Customers:')
print(high_value)

from data_processor import calculate_total_visits

total_visits = calculate_total_visits(high_value)
print(f'Total visits from high-value customers: {total_visits}')
