"""
This module represents the Marketplace.
"""

class Marketplace:
    """
    This class represents the Marketplace.
    """
    def __init__(self, queue_size_per_producer):
        """
        Constructor

        :param queue_size_per_producer: The maximum size of a queue associated with each producer.
        :type queue_size_per_producer: int
        """
        try:
            self.queue_size_per_producer = queue_size_per_producer
            # List of queues, one per producer
            self.queue_producers = [[] for _ in range(queue_size_per_producer)]
            # List of products available in the marketplace
            self.products = []
            # Dictionary to keep track of which producer published which product
            self.producer_product = {}
            self.carts = []  # List of carts created by consumers
        except ValueError as error:
            raise ValueError("queue_size_per_producer must be an integer") from error

    def register_producer(self):
        """
        Returns an ID for the producer that calls this.

        :return: The ID of the registered producer.
        :rtype: int
        """
        try:
            producer_id = len(self.queue_producers) # ID is the current length of the list
            self.queue_producers.append([])  # Add an empty queue for the registered producer
            return producer_id
        except IndexError as error:
            raise IndexError("Failed to register producer") from error

    def publish(self, producer_id, product):
        """
        Adds the product provided by the producer to the marketplace.

        :param producer_id: The ID of the producer.
        :type producer_id: int

        :param product: The product to be published.
        :type product: str

        :return: True if the product was published successfully,
                 False if the producer's queue is full.
        :rtype: bool
        """
        try:
            if len(self.queue_producers[producer_id]) < self.queue_size_per_producer:
                # If the producer's queue is not full, add the product to the marketplace
                self.products.append(product)
                self.producer_product[product] = producer_id
                # Add a placeholder to the producer's queue
                self.queue_producers[producer_id].append(0)
                return True
            return False  # If the producer's queue is full, return False
        except IndexError as error:
            raise IndexError("Invalid producer_id") from error

    def new_cart(self):
        """
        Creates a new cart for the consumer.

        :return: The ID of the newly created cart.
        :rtype: int
        """
        try:
            new_cart_id = len(self.carts)  # ID is the current length of the list of carts
            self.carts.append([])  # Add an empty cart for the consumer
            return new_cart_id
        except IndexError as error:
            raise IndexError("Failed to create a new cart.") from error

    def add_to_cart(self, cart_id, product):
        """
        Adds a product to the given cart.

        :param cart_id: The ID of the cart.
        :type cart_id: int

        :param product: The product to be added to the cart.
        :type product: str

        :return: True if the product was added successfully,
                 False if the product is not available in the marketplace.
        :rtype: bool
        """
        try:
            if product not in self.products:
                return False  # If the product is not available in the marketplace, return False

            self.products.remove(product)  # Remove the product from the marketplace
            self.carts[cart_id].append(product)  # Add the product to the cart

            # Check if the added product was produced by a registered producer
            # and if there is a product in the producer's queue,
            # remove the first item from the queue
            producer_id = self.producer_product.get(product)
            if producer_id is not None and self.queue_producers[producer_id]:
                self.queue_producers[producer_id].pop(0)

            return True
        except ValueError as error:
            raise ValueError("Failed to add product to cart.") from error

    def remove_from_cart(self, cart_id, product):
        """
        Removes a product from cart.

        :param cart_id: The ID of the cart.
        :type cart_id: int

        :param product: The product to be removed from the cart.
        :type product: str
        """
        try:
            cart = self.carts[cart_id]
            if product in cart:
                cart.remove(product)  # Remove the product from the cart
                self.products.append(product)  # Add the product back to the marketplace
                producer_id = self.producer_product[product]
                # Add a placeholder to the producer's queue
                self.queue_producers[producer_id].append(None)
        except ValueError:
            pass  # Ignore if the product is not in the cart

    def place_order(self, cart_id):
        """
        Return a list with all the products in the cart.

        :param cart_id: The ID of the cart.
        :type cart_id: int

        :return: List of products in the cart.
        :rtype: list
        """
        try:
            products = self.carts[cart_id]  # Get the products in the cart
        except IndexError:
            products = []  # Return an empty list if the cart ID is invalid
        return products
