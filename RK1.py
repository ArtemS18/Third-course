class CD_Disk:
    def __init__(self, id, name, size, library_id):
        self.id = id
        self.name = name
        self.size = size
        self.library_id = library_id

class CD_Library:
    def __init__(self, id, name):
        self.id = id
        self.name = name

class Library_to_Disk:
    def __init__(self, id, disk_id ,library_id):
        self.id = id
        self.disk_id = disk_id
        self.library_id = library_id

def main():
    cd_disks = [
         CD_Disk(1, "Классика", 432, 1),
         CD_Disk(2, "Рок-концерты 2022", 420, 2),
         CD_Disk(3, "Назад в Черное", 400, 3),
         CD_Disk(4, "Аби Роуд", 425, 1),
         CD_Disk(5, "Рожденный бегать", 380, 4),
         CD_Disk(6, "Слухи", 410, 5),
         CD_Disk(7, "Led Zeppelin IV", 450, 1),
         CD_Disk(8, "Рок 2004", 470, 2),
         CD_Disk(9, "Клуб одиноких сердец сержанта Пеппера", 415, 1),
         CD_Disk(10, "Нирвана", 405, 6),
    ]
    cd_library_list = [
        CD_Library(1, "Классическая музыка"),
        CD_Library(2, "Рок-музыка"),
        CD_Library(3, "Поп-музыка"),
        CD_Library(4, "Джаз"),
        CD_Library(5, "Электронная музыка"),
        CD_Library(6, "Фолк-музыка"),
    ]
    library_to_disk_objects = [
        Library_to_Disk(1, 1, 1),
        Library_to_Disk(2, 2, 2),
        Library_to_Disk(3, 3, 3),
        Library_to_Disk(4, 4, 4),
        Library_to_Disk(5, 5, 5),
        Library_to_Disk(6, 6, 6),
        Library_to_Disk(7, 7, 1),
        Library_to_Disk(8, 8, 2),
        Library_to_Disk(9, 9, 3),
        Library_to_Disk(10, 10, 4),
        Library_to_Disk(11, 1, 5),
        Library_to_Disk(12, 2, 6),
        Library_to_Disk(13, 3, 1),
        Library_to_Disk(14, 4, 2),
        Library_to_Disk(15, 5, 3),
        Library_to_Disk(16, 6, 4),
        Library_to_Disk(17, 7, 5),
        Library_to_Disk(18, 8, 6),
        Library_to_Disk(19, 9, 1),
        Library_to_Disk(20, 10, 2),
    ]
    #B1
    #«Библиотека» и «CD-Диск» связаны соотношением один-ко-многим.
    #Выведите список всех CD-дисков, у которых название начинается с "Р",
    #и названия их библиотеки.
    print("B1:")
    for i in cd_disks:
        for g in cd_library_list:
            if i.library_id == g.id:
                if i.name[0] == "Р":
                    print(i.name, g.name)


   #B2
    #«Библиотека» и «CD-Диск» связаны соотношением один-ко-многим.
    #Выведите список библиотек с минимальной емкостью  СD-диска в каждом библиотеке,
    #отсортированный по минимальной емкости.

    print("B2:")
    dict = {}
    for i in cd_disks:
        for g in cd_library_list:
            if i.library_id == g.id:
                if g.name not in dict:
                    dict[g.name] = i.size
                else:
                    dict[g.name] = min(dict[g.name], i.size)
    for h in dict:
        print(f"Библиотека: {h}; минимальная емкость диска {dict[h]} МБ")


    #B3
    #«Библиотека» и «CD-Диск» связаны соотношением многие-ко-многим.
    #Выведите список всех связанных CD-дисков и библиотек, отсортированный по жестким дискам,
    #сортировка по Библиотекаам произвольная.
    print("B3:")
    def lm(obj):
        for i in cd_disks:
            if obj.disk_id == i.id:
                return i.name
    def lib(obj):
        for i in cd_library_list:
            if obj.library_id == i.id:
                return i.name

    sortes = list(map(lambda x: (lm(x), lib(x)), sorted(library_to_disk_objects, key = lm)))
    for i in sortes:
        print(i[0], i[1])

if __name__ == "__main__":
    main()
