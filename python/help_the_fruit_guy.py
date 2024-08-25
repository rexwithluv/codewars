"""ID: 557af4c6169ac832300000ba

Our fruit guy has a bag of fruit (represented as an array of strings) where some fruits are rotten. He wants to replace all the rotten pieces of fruit with fresh ones. For example, given `["apple","rottenBanana","apple"]` the replaced array should be `["apple","banana","apple"]`. Your task is to implement a method that accepts an array of strings containing fruits should returns an array of strings where all the rotten fruits are replaced by good ones.

### Notes

- If the array is null/nil/None or empty you should return empty array (`[]`).
- The rotten fruit name will be in this camelcase (`rottenFruit`).
- The returned array should be in lowercase."""


def remove_rotten(bag_of_fruits: list[str]) -> list[str]:
    if bag_of_fruits is None or len(bag_of_fruits) == 0:
        return []

    for i in range(len(bag_of_fruits)):
        bag_of_fruits[i] = bag_of_fruits[i].lower()
        if bag_of_fruits[i].startswith("rotten"):
            bag_of_fruits[i] = bag_of_fruits[i].replace("rotten", "")

    return bag_of_fruits


print(
    remove_rotten(
        ["rottenApple", "rottenBanana", "rottenApple", "rottenPineapple", "rottenKiwi"]
    )
)
