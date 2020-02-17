""" Transaction Records"""


class TransactionRecords:
    def __init__(self):
        self._record_list = []

    def add_record(self, time, amount, budget_cat, name):
        record = [time, amount, budget_cat, name]
        self._record_list.append(record)

    def print_record(self):
        print("\nTransaction:")
        record = self._record_list[len(self._record_list) - 1]
        print("Time:", record[0])
        print(f"Amount: ${record[1]}")
        print(f"Budget Category: {record[2]}")
        print(f"Shop/Website Name: {record[3]}\n")

    def print_all_records(self):
        print("Transactions:\n")
        game_records = []
        clothing_records = []
        eating_records = []
        misc_records = []
        for record in self._record_list:
            if record[2] == "games and entertainment":
                game_records.append(record)
            if record[2] == "clothing and accessories":
                clothing_records.append(record)
            if record[2] == "eating out":
                eating_records.append(record)
            if record[2] == "miscellaneous":
                misc_records.append(record)

        print("---Games and entertainment---")
        for record in game_records:
            print("Time:", record[0])
            print(f"Amount: ${record[1]}")
            print(f"Shop/Website Name: {record[3]}\n")

        print("---Clothing and accessories---")
        for record in clothing_records:
            print("Time:", record[0])
            print(f"Amount: ${record[1]}")
            print(f"Shop/Website Name: {record[3]}\n")

        print("---Eating out---")
        for record in eating_records:
            print("Time:", record[0])
            print(f"Amount: ${record[1]}")
            print(f"Shop/Website Name: {record[3]}\n")

        print("---Miscellaneous---")
        for record in misc_records:
            print("Time:", record[0])
            print(f"Amount: ${record[1]}")
            print(f"Shop/Website Name: {record[3]}\n")
