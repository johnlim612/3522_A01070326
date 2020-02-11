"""
Implements the observer pattern and simulates a simple auction.
"""
import random


class Auctioneer:
    """
    The auctioneer acts as the "core". This class is responsible for
    tracking the highest bid and notifying the bidders if it changes.
    """

    def __init__(self):
        self.bidders = []
        self._highest_bid = 0
        self._highest_bidder = None

    def register_bidder(self, bidder):
        """
        Adds a bidder to the list of tracked bidders.
        :param bidder: object with __call__(auctioneer) interface.
        """
        self.bidders.append(bidder)

    def reset_auctioneer(self):
        """
        Resets the auctioneer. Removes all the bidders and resets the
        highest bid to 0.
        """
        self.bidders.clear()
        self._highest_bid = 0

    def _notify_bidders(self):
        """
        Executes all the bidder callbacks. Should only be called if the
        highest bid has changed.
        """
        for x in self.bidders:

            x(self)

    def accept_bid(self, bid, bidder="Starting Bid"):
        """
        Accepts a new bid and updates the highest bid. This notifies all
        the bidders via their callbacks.
        :param bid: a float.
        :precondition bid: should be higher than the existing bid.
        :param bidder: The object with __call__(auctioneer) that placed
        the bid.
        """
        if bid <= self._highest_bid:
            print("The bid must be higher the the highest bid")
            return

        print(f"{str(bidder)} bidded {bid} in response to {self.get_highest_bidder()}'s bid of {self._highest_bid}!")
        self._highest_bid = bid
        self._highest_bidder = str(bidder)
        self._notify_bidders()

    def get_highest_bid(self):
        return self._highest_bid

    def get_highest_bidder(self):
        return self._highest_bidder


class Bidder:
    """
    Represents a single bidder that participates in the auction.
    """
    def __init__(self, name, money=100, threat_chance=0.35, bid_increase=1.1):
        self._name = name
        self._threat_chance = threat_chance
        self._money = money
        self._bid_increase = bid_increase
        self._highest_bid = 0

    def __call__(self, auctioneer):
        # Don't run if its current bid holder
        if self._name == auctioneer.get_highest_bidder():
            return
        # Increased bid value
        bid = float(auctioneer.get_highest_bid() * self._bid_increase)

        # Checking if bidder has enough money
        if bid < self._money:

            ran = random.random()
            if ran < self._threat_chance:
                self._highest_bid = bid
                auctioneer.accept_bid(bid, self)

    def __str__(self):
        return self._name

    def get_name(self):
        return self._name

    def get_highest_bid(self):
        return self._highest_bid


class Auction:
    """
    Simulates an auction. Is responsible for driving the auctioneer and
    the bidders.
    """

    def __init__(self, bidders):
        """
        Initialize an auction. Requires a list of bidders that are
        attending the auction and can bid.
        :param bidders: sequence type of objects of type Bidder
        """
        self._bidders = bidders

    def simulate_auction(self, item, start_price):
        """
        Starts the auction for the given item at the given starting
        price. Drives the auction till completion and prints the results.
        :param item: string, name of item.
        :param start_price: float
        """
        auctioneer = Auctioneer()

        for x in self._bidders:
            auctioneer.register_bidder(x)
        auctioneer.accept_bid(start_price)

        # Printing simulation
        print(f"The winner of the auction is {auctioneer.get_highest_bidder()} at {auctioneer.get_highest_bid()}")
        print("Highest Bids Per Bidder")
        for x in self._bidders:
            name = x.get_name()
            highest_bid = x.get_highest_bid()
            print("Bidder: {0} \tHighest Bid: {1}".format(name, highest_bid))


def main():
    bidders = [Bidder("Jojo", 3000, random.random(), 1.2), Bidder("Melissa", 7000, random.random(), 1.5),
               Bidder("Priya", 15000, random.random(), 1.1), Bidder("Kewei", 800, random.random(), 1.9),
               Bidder("Scott", 4000, random.random(), 2)]
    # Hardcoding the bidders.

    print("\n\nStarting Auction!!")
    print("------------------")

    # instantiating an auction
    my_auction = Auction(bidders)
    my_auction.simulate_auction("Antique Vase", 100)


if __name__ == '__main__':
    main()

