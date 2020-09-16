# Alejandra Castillo 1440370
service = {
    'Oil change': 35, 'Tire rotation': 19, 'Car wash': 7, 'Car wax': 12, '-': 0
}
print("Davy's auto shop services")
print('Oil change -- $35')
print('Tire rotation -- $19')
print('Car wash -- $7')
print('Car wax -- $12')

print('\nSelect first service:')
service_one = input()
print('Select second service:')
service_two = input()

print("\nDavy's auto shop invoice")
if service_one != '-' and service_two != '-':
    print('\nService 1: {},'.format(service_one), '${}'.format((service[service_one])))
    print('Service 2: {},'.format(service_two), '${}'.format((service[service_two])))
    total_price = service[service_one] + service[service_two]
elif service_one == '-':
    print('\nService 1:', 'No service')
    print('Service 2: {},'.format(service_two), '${}'.format((service[service_two])))
    total_price = service[service_two]
else:
    print('\nService 1: {},'.format(service_one), '${}'.format((service[service_one])))
    print('Service 2:', 'No service')
    total_price = service[service_one]
print('\nTotal: ${}'.format(total_price))
