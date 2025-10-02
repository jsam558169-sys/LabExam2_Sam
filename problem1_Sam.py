from abc import ABC, abstractmethod

# game class
class game(ABC):
    @abstractmethod
    def play(self):
        pass

# matingGame class
class matingGame(game):
    def __init__(self, name1, name2):
        # encapsulation
        self.__name1 = name1.lower().replace(" ", "")
        self.__name2 = name2.lower().replace(" ", "")

    # method play
    def play(self):
        name1_list = list(self.__name1)
        name2_list = list(self.__name2)

        # remove common characters
        for char in self.__name1:
            if char in name2_list:
                name1_list.remove(char)
                name2_list.remove(char)

        # remaining letters
        remaining1 = "".join(name1_list)
        remaining2 = "".join(name2_list)

        count1 = len(remaining1)
        count2 = len(remaining2)
        total_count = count1 + count2

        if total_count == 0:
            return {
                "remaining1": remaining1,
                "remaining2": remaining2,
                "count1": count1,
                "count2": count2,
                "sum": total_count,
                "relationship": "Not compatible! Single forever </3"
            }

        # FLAMES algorithm
        flames = ["Friendship", "Love", "Affection", "Marriage", "Enemy", "Siblings"]
        index = 0
        while len(flames) > 1:
            index = (index + total_count - 1) % len(flames)
            flames.pop(index)

        return {
            "remaining1": remaining1,
            "remaining2": remaining2,
            "count1": count1,
            "count2": count2,
            "sum": total_count,
            "relationship": flames[0]
        }

# main menu
if __name__ == "__main__":
    your_name = input("\nEnter your name: ")
    partner_name = input("Enter crush's name: ")

    game = matingGame(your_name, partner_name)
    result = game.play()

    # print results
    print(f"\nYour name remaining : {result['remaining1']}")
    print(f"Crush name remaining: {result['remaining2']}")
    print(f"\nCount remaining [your name] : {result['count1']}")
    print(f"Count remaining [crush]     : {result['count2']}")
    print(f"Sum                         : {result['sum']}")
    print(f"Relationship                : {result['relationship']}")