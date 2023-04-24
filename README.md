# Marketplace
### Copyright Adina-Maria Amzarescu 331CA

____________________________________________________________________________________

This project implements a multi-threaded system where producers make 
products and publish them to a marketplace. The marketplace is designed 
to handle multiple producers and consumers concurrently, allowing for 
efficient and parallel processing of products.

The marketplace manages the availability of products for consumers and handles 
republishing of products when necessary. 

____________________________________________________________________________________


## Organization

The project is organized into two main classes: 

* Producer
* Consumer

Each represents a separate thread in the multi-threaded system. 
The Producer class is responsible for making products and publishing them 
to the marketplace, while the Consumer class represents a consumer thread 
that consumes products from the marketplace by adding and removing products 
from their cart, and finally placing an order for the cart.

The project follows an object-oriented approach, with the Producer and Consumer 
classes encapsulating the logic for producing and consuming products, respectively. 
The classes are designed to be extensible, allowing for customization through the 
use of constructor arguments.

____________________________________________________________________________________

## Implementation

### `Producer`

This module represents a Producer class.

The Producer class is a subclass of the Thread class from the threading module.

The Producer class has a run() method that represents the main logic of the 
producer thread. The run() method contains a while loop that iterates through the 
products list and produces the specified number of products for each product type.
For each product, the run() method attempts to publish it to the marketplace using 
the publish() method of the marketplace.
If the marketplace is unavailable (cannot publish), the producer sleeps for the 
remaining time before republishing as specified by the republish_wait_time.
If the product is successfully published, the producer sleeps for the normal 
sleep time between producing products.
Any errors that occur during the initialization or execution of the producer 
thread are caught as TypeError and a custom error message is raised with 
additional context.
The purpose of using try-except blocks in the init() and run() methods is 
to handle errors gracefully and provide informative error messages for 
debugging and troubleshooting purposes.

Additional explanations:

* super().__init__(**kwargs)

    This is calling the __init__() method of the parent class (Thread)

* sleep_time = max(0, self.republish_wait_time - time_sleep_normal)

    This determines how much time the producer thread should sleep before 
    attempting to republish a product to the marketplace. 
    This allows the producer thread to sleep for the appropriate amount 
    of time.

### `Consumer`

This module represents a Consumer class.

The Consumer class has a run method that represents the main logic of the 
consumer thread.
The run method iterates through each cart in the carts list.
For each cart, it creates a new cart in the marketplace using the new_cart 
method of the marketplace.
It then iterates through each command in the cart (which can be either an 
add or remove operation).

For each command, it performs the corresponding operation (add or remove) 
using the add_to_cart or remove_from_cart methods of the marketplace, and 
waits for the operation to succeed or sleep for the retry wait time before 
trying again if the operation fails.

After all the commands in the cart are executed, it places the order for 
the cart in the marketplace using the place_order method of the marketplace.
It then iterates through the products in the order and prints the name of 
the consumer and the product they bought using the print statement.

Additional explanations:

* super().__init__(**kwargs)

    This is calling the __init__() method of the parent class (Thread)

* if result is None or result

    This is used to determine if the operation (either adding or 
    removing a product from the cart) was successful.

### `Marketplace`

The Marketplace class represents a marketplace where producers can 
publish products and consumers can create carts, add products to the 
carts, and place orders.

Additional explanations:

* self.queue_producers = [ [] for _ in range(queue_size_per_producer) ]

    This creates a list of empty lists, where the number of empty 
    lists is determined by the value of queue_size_per_producer.


____________________________________________________________________________________

## Important

* Why is the project useful?

    This project involves designing a system for a marketplace with multiple 
    components. It requires making decisions on how to organize and structure 
    the code to ensure modularity, reusability, and maintainability. It also 
    has a real-world application because the concept of a marketplace 
    is a common real-world scenario.

* Is the solution efficient?

    There are many ways in which I could improve the project. 
    As an example, I used lists in the marketplace, but I think using 
    dictionaries would have been a better approach.

* Encountered problems:

    A problem in my approach is the fact that I thought the code 
    in C, and then I translated it into python. That's why I think 
    I didn't use all the functionalities offered by python

____________________________________________________________________________________

## Resources

1. https://docs.python.org/3/library/threading.html
2. https://docs.python.org/3/library/threading.html#thread-objects
3. https://docs.python.org/3/library/time.html
4. https://stackoverflow.com/questions/510348/how-do-i-make-a-time-delay
