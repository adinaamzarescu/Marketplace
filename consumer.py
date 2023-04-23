"""
This module represents the Consumer.
"""

from threading import Thread
import time

class Consumer(Thread):
    """
    This class represents a consumer.
    """
    def __init__(self, carts, marketplace, retry_wait_time, **kwargs):
        """
        Constructor.

        Args:
            carts (List): A list of add and remove operations for the consumer's carts.
            marketplace (Marketplace): A reference to the marketplace.
            retry_wait_time (Time): The number of seconds that the consumer must wait
            until the marketplace becomes available.
            **kwargs: Other arguments that are passed to the Thread's __init__().

        Raises:
            TypeError: If there is an error during consumer initialization.
        """
        try:
            super().__init__(**kwargs)
            self.name = kwargs['name'] # Set the name of the consumer
            self.retry_wait_time = retry_wait_time # Set the retry wait time
            self.marketplace = marketplace # Set the marketplace reference
            self.carts = carts # Set the consumer's carts
        except ValueError as error:
            raise ValueError("Error during consumer initialization") from error

    def run(self):
        i = 0
        while i < len(self.carts):
            cart = self.carts[i]
            cart_id = self.marketplace.new_cart() # Create a new cart in the marketplace
            for cmd in cart:
                num_products = 0
                while num_products < cmd['quantity']:
                    if cmd['type'] == 'remove':
                        # Remove a product from the cart
                        result = self.marketplace.remove_from_cart(cart_id, cmd['product'])
                    elif cmd['type'] == 'add':
                        # Add a product to the cart
                        result = self.marketplace.add_to_cart(cart_id, cmd['product'])

                    # If the operation is successful or None (indicating the cart is not available)
                    if result is None or result:
                        num_products += 1
                    # If the operation fails, sleep for the retry wait time before trying again
                    else:
                        time.sleep(self.retry_wait_time)

            # Place the order for the cart in the marketplace
            products = self.marketplace.place_order(cart_id)
            j = 0
            while j < len(products):
                product = products[j]
                # Print the name of the consumer and the product they bought
                print(f'{self.name} bought {product}')
                j += 1
            i += 1
