# TODO Найдите количество книг, которое можно разместить на дискете
memory_ = 1.44 #Mb
pages = 100
strings = 50
sim = 25
bait_for_sim = 4
bait_in_mb = 1024 * 1024

sim_in_book = sim * strings * pages
bait_in_book = sim_in_book * bait_for_sim
count_of_books = memory_ * bait_in_mb // bait_in_book

print("Количество книг, помещающихся на дискету:", int(count_of_books))
