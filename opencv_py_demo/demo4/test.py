
#!/usr/bin/python
# -*- coding: UTF-8 -*-


test = "asd,  gh, jj"
test_new = test.split(' ')
print(test_new)
test_new3 = ''.join(test_new)
# print(test_new3)
# test4 = "".join(test_new3)
# print(test4)
line = test_new3.split(",")
line = " ".join(line)
print(line)