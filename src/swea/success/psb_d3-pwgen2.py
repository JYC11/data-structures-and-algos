# for test_case in range(1, 11):
#     orig_pw_len = int(input())
#     orig_pw = input().split()
#     command_count = int(input())
#     commands = input.split()
#     inserts = [i for i, x in enumerate(commands) if x == "I"]
#     deletes = [i for i, x in enumerate(commands) if x == "D"]
#     i_and_d = sorted(commandserts+deletes)
#     for i in i_and_d:
#         if commands[i] == "I":
#             insrt_idx = int(commands[i+1])
#             insert_cnt = int(commands[i+2])
#             to_insert = commands[i+3:i+3+insert_cnt]
#             commandserted = 0
#             while commandserted < insert_cnt:
#                 orig_pw.commandsert(insert_idx, to_insert[commandserted])
#                 insert_idx += 1
#                 commandserted += 1
#         elif commands[i] == "D":
#             dlt_idx = int(commands[i+1])
#             dlt_cnt = int(commands[i+2])
#             del orig_pw[dlt_idx+1:dlt_idx+1+dlt_cnt]
#         else:
#             pass
#     print("#{} {} {} {} {} {} {} {} {} {} {}".format(test_case, *orig_pw))
# test_case = 1
# orig_pw_len = int("193")
# orig_pw = "701633 517247 207227 598906 709204 177422 933135 361253 641488 272037 700207 210546 897237
# 133041 350385 701520 298460 312226 606874 129312 960451 613318 383985 199348 152779 133823 818875 580215
# 459355 605845 834805 106218 905612 938377 391231 841032 683166 453449 557724 407096 123768 365351 651864
# 882335 864696 185012 837300 411026 659435 607734 300451 177321 851933 842088 867633 861841 417869 236761
# 949721 684281 140261 244495 123549 991347 524837 347789 412387 144473 282315 594309 458934 483218 360158
# 677818 266328 683156 206167 513401 354598 777644 198862 605089 222069 663762 417125 366235 796851 788266
# 298786 528509 357179 399446 106551 359705 307358 240325 800858 174477 622329 503791 280873 594721 102639
# 535002 434477 554468 542442 543235 802732 557167 158097 756524 525828 953376 895449 465929 627387 540019
# 664636 841936 155005 118968 240606 430468 534001 186501 398767 882015 547707 156922 269604 546219 214280
# 971630 989208 257747 669219 368941 652847 691652 402317 893998 828431 493419 661259 708152 192475 818448
# 237648 124585 341646 357664 511511 143670 756275 435692 394361 860565 766233 250026 401650 262049 562704
# 300158 134831 950780 320365 639739 115203 447338 264917 375282 760248 670650 850444 736266 445557 821899
# 281297 709979 135246 248791 397891 974659 615684 637889 415775 256973 694204 816240 405016 418078 411082".split()
# command_count = int("11")
# raw_commands = "I 19 4 281822 746265 450734 108373 I 106 9 666218 302034 208501 648283 798327 631226 998665
# 959675 852007 D 117 1 D 191 2 D 10 3 D 133 1 D 76 1 I 105 7 362012 585269 876166 894252 294007 210018 659653
# I 203 7 352576 568766 700855 768224 339990 691517 213258 D 84 4 I 6 6 291139 808642 764059 913376 124313
# 256337".split()
# commands = []

for test_case in range(1, 11):
    orig_pw_len = int(input())
    orig_pw = input().split()
    command_count = int(input())
    raw_commands = input().split()
    commands = []
    for i in range(len(raw_commands)):
        tmp = raw_commands[i]
        if raw_commands[i] == "I" or raw_commands[i] == "D":
            if i != 0:
                commands.append(tmp)
            tmp = [raw_commands[i]]
        elif i == len(raw_commands) - 1:
            tmp.append(raw_commands[i])
            commands.append(tmp)
        else:
            tmp.append(raw_commands[i])

    for i in range(len(commands)):
        if commands[i][0] == "I":
            pwd_idx = int(commands[i][1])
            insrt_cnt = int(commands[i][2])
            to_insrt = commands[i][3:]
            for cnt in range(insrt_cnt):
                orig_pw.insert(pwd_idx + cnt, to_insrt[cnt])
        elif commands[i][0] == "D":
            dlt_idx = int(commands[i][1])
            dlt_cnt = int(commands[i][2])
            for cnt in range(dlt_cnt):
                del orig_pw[dlt_idx]
    print("#{} {} {} {} {} {} {} {} {} {} {}".format(test_case, *orig_pw))
