import asyncio
class strongman:
    def __init__(self, name="NoName", power=0):
        self.name = name
        self.power = power

async def start_strongman(strongman):
    """
    :param name: Имя силача 
    :return:
    """
    print(f"Силач {strongman.name} начал соревнования")
    for i in range(1, 6):
        await asyncio.sleep(100/strongman.power)
        print(f"Силач {strongman.name} поднял шар номер {i}")
    print(f"Силач {strongman.name} закончил соревнования")

async def start_tournament(*args):
    tasks = [start_strongman(name) for name in args]
    await asyncio.gather(*tasks)

#################################################################################

if __name__ == "__main__":
    EvpatiyKolovrat = strongman("Евпатий Коловрат", 1000)
    SkopinShuyskiy = strongman("Скопин Шуйский", 800)
    GrigoriyRusakov = strongman("Григорий Русаков", 700)
    asyncio.run(start_tournament(EvpatiyKolovrat, SkopinShuyskiy, GrigoriyRusakov))
