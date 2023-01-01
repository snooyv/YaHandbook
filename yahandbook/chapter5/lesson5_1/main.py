from less_F2 import Rectangle


rect = Rectangle((3.2, -4.3), (7.52, 3.14))
#rect.chek_conrner2()
print(rect.get_pos(), rect.get_size())
rect.move(1.32, -5)
print(rect.get_pos(), rect.get_size())

print("***************************")

rect2 = Rectangle((7.52, -4.3), (3.2, 3.14))
#rect2.chek_conrner2()
print(rect2.get_pos(), rect2.get_size())
#rect.resize(23.5, 11.3)
print(rect2.get_pos(), rect2.get_size())




