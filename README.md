# Marketplace
### Copyright Adina-Maria Amzarescu 331CA

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

`Producer`

This module represents a Producer class.

The Producer class is a subclass of the Thread class from the threading module. 
It has a constructor (init method) that takes in parameters such as products, 
marketplace, republish_wait_time, and other kwargs.
The constructor initializes the Producer object by calling the superclass's init() 
method and setting the products, republish_wait_time, and marketplace attributes.
The constructor also registers the producer with the marketplace and obtains 
a producer ID.

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

`Consumer`

This module represents a Consumer class.

The constructor sets the name of the consumer, retry wait time, marketplace 
reference, and consumer's carts.
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

`Marketplace`

The Marketplace class represents a marketplace where producers can 
publish products and consumers can create carts, add products to the 
carts, and place orders.

The class has the following attributes:

- `queue_size_per_producer`: An integer representing the maximum 
size of a queue associated with each producer.
- `queue_producers`: A list of queues, one per producer, initially empty.
- `products`: A list of products available in the marketplace, initially empty.
- `producer_product`: A dictionary to keep track of which producer published 
which product.
- `carts`: A list of carts created by consumers, initially empty.

The class has the following methods:

- `__init__(self, queue_size_per_producer)`: The constructor method that initializes the `queue_size_per_producer` attribute and creates empty lists for `queue_producers`, `products`, and `carts`. It also raises a `ValueError` if the `queue_size_per_producer` parameter is not an integer.
- `register_producer(self)`: A method that registers a producer and returns an ID for the registered producer. It appends an empty queue for the registered producer to the `queue_producers` list and returns the ID, which is the current length of the list.
- `publish(self, producer_id, product)`: A method that adds a product provided by a producer to the marketplace. It checks if the producer's queue is full based on the `queue_size_per_producer` attribute, and if not, adds the product to the marketplace, updates the `producer_product` dictionary, and adds a placeholder to the producer's queue. It returns `True` if the product was published successfully, and `False` if the producer's queue is full.
- `new_cart(self)`: A method that creates a new cart for a consumer and returns the ID of the newly created cart. It appends an empty cart for the consumer to the `carts` list and returns the ID, which is the current length of the list.
- `add_to_cart(self, cart_id, product)`: A method that adds a product to a given cart. It checks if the product is available in the marketplace based on the `products` list, and if so, removes the product from the marketplace, adds the product to the cart, and updates the producer's queue if applicable. It returns `True` if the product was added successfully, and `False` if the product is not available in the marketplace.
- `remove_from_cart(self, cart_id, product)`: A method that removes a product from a cart. It removes the product from the cart and adds the product back to the marketplace. It also adds a placeholder to the producer's queue if applicable.
- `place_order(self, cart_id)`: A method that returns a list of products in a cart based on the `carts` list. It returns an empty list if the cart ID is invalid.

