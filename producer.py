"""
This module represents the Producer.
"""
from threading import Thread
import time

class Producer(Thread):
    """
    This class represents a producer.
    """
    def __init__(self, products, marketplace, republish_wait_time, **kwargs):
        """
        Constructor.

        Args:
            products (List): A list of products that the producer will produce.
            marketplace (Marketplace): A reference to the marketplace.
            republish_wait_time (Time): The number of seconds that a producer
            must wait until the marketplace becomes available.
            **kwargs: Other arguments that are passed to the Thread's __init__().

        Raises:
            TypeError: If there is an error during producer initialization.
        """
        try:
            super().__init__(**kwargs) # Call the superclass's __init__() method
            self.products = products # Set the products list
            self.republish_wait_time = republish_wait_time # Set the republish wait time
            self.marketplace = marketplace # Set the marketplace reference
             # Register the producer with the marketplace and get a producer ID
            self.producer_id = self.marketplace.register_producer()
        except TypeError as error:
            raise TypeError("Error during producer initialization") from error

    def run(self):
        """
        Method representing the main logic of the producer thread.

        Raises:
            TypeError: If there is an error during producer run.
        """
        while True:
            i = 0
            while i < len(self.products):
                # Get the product, number of products to produce, and sleep time for each product
                product, number, time_sleep_normal = self.products[i]
                j = 0
                while j < number:
                    try:
                        # Publish the product to the marketplace
                        can_publish = self.marketplace.publish(self.producer_id, product)
                        if not can_publish:
                            # Calculate the remaining sleep time before republishing
                            sleep_time = max(0, self.republish_wait_time - time_sleep_normal)
                            time.sleep(sleep_time) # Sleep for the remaining time
                        else:
                            # Sleep for the normal sleep time between producing products
                            time.sleep(time_sleep_normal)
                            j += 1 # Increment the counter for produced products
                    except TypeError as error:
                        raise TypeError("Error during producer run") from error
                i += 1 # Move to the next product in the products list
