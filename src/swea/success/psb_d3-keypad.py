# for test_case in range(1, 11):
#     pwd_len, pwd = input().split(" ")
#     to_del = []
#     pwd_len = int(pwd_len)
#     for i in range(pwd_len):
#         left = i
#         right = i+1
#         if left in to_del or right in to_del:
#             pass
#         else:
#             while (left >= 0 and right < len(pwd)) and (pwd[left] == pwd[right]):
#                 to_del.append(left)
#                 to_del.append(right)
#                 left -= 1
#                 right += 1

#     pwd = [i for i in pwd]
#     for i in to_del:
#         pwd[i] = "@"
#     pwd = ''.join(pwd).replace("@", "")

#     print(f'#{test_case} {pwd}')

# test_case = 1
# pwd_len, pwd = "16 4100112380990844".split(" ")
# pwd_len = int(pwd_len)
# to_del = []

# for i in range(pwd_len):
#     left = i
#     right = i+1
#     if left in to_del or right in to_del:
#         pass
#     else:
#         while (left >= 0 and right < len(pwd)) and (pwd[left] == pwd[right]):
#             to_del.append(left)
#             to_del.append(right)
#             left -= 1
#             right += 1

# print(to_del)
# pwd = [i for i in pwd]
# for i in to_del:
#     pwd[i] = "@"
# pwd = ''.join(pwd).replace("@","")

# print(f'#{test_case} {pwd}')

# for test_case in range(1,11):
#     pwd_len, pwd = input().split()
#     pwd_len = int(pwd_len)
#     pwd = [i for i in pwd]

#     i = 0
#     while True:
#         if pwd[i] == pwd[i+1]:
#             del pwd[i:i+2]
#             pwd_len -= 2
#             i -= 2
#         i += 1
#         if i == (pwd_len-1):
#             break

#     final_pwd = ''
#     for i in range(pwd_len):
#         final_pwd += pwd[i]
#     print(f'#{test_case} {final_pwd}')

print(all([True, False, False]))
