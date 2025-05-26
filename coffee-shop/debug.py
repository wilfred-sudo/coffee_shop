from customer import Customer
from coffee import Coffee

def main():
    # Create customers
    alice = Customer("Alice")
    bob = Customer("Bob")

    # Create coffees
    espresso = Coffee("Espresso")
    latte = Coffee("Latte")

    # Alice places orders
    alice.create_order(espresso, 3.5)
    alice.create_order(latte, 4.0)
    alice.create_order(espresso, 3.0)

    # Bob places orders
    bob.create_order(espresso, 3.5)
    bob.create_order(latte, 4.5)

    # Display Alice's orders and coffees
    print(f"{alice.name}'s orders: {[order.coffee.name for order in alice.orders()]}")
    print(f"{alice.name}'s coffees: {[coffee.name for coffee in alice.coffees()]}")

    # Display Espresso stats
    print(f"{espresso.name} total orders: {espresso.num_orders()}")
    print(f"{espresso.name} average price: {espresso.average_price():.2f}")
    print(f"{espresso.name} customers: {[customer.name for customer in espresso.customers()]}")

    # Find most aficionado for Espresso
    top_customer = Customer.most_aficionado(espresso)
    if top_customer:
        print(f"Most aficionado for {espresso.name}: {top_customer.name}")
    else:
        print(f"No customers found for {espresso.name}")

if __name__ == "__main__":
    main()