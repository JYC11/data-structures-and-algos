for test_case in range(1,11):
    orig_pw_len = int(input())
    orig_pw = list(map(int,input().split()))
    command_count = int(input())
    commands = [i.split() for i in input()[2:].split(" I ")]
    for i in range(command_count):
        pw_index = int(commands[i][0])
        nmbr_to_insert = int(commands[i][1])
        to_insert = commands[i][2:]
        inserted = 0
        while inserted < nmbr_to_insert:
            orig_pw.insert(pw_index,to_insert[inserted])
            pw_index += 1
            inserted += 1
    print("#{} {} {} {} {} {} {} {} {} {} {}".format(test_case, *orig_pw))
    

# orig_pw_len = 11
# orig_pw_str = "449047 855428 425117 532416 358612 929816 313459 311433 472478 589139 568205"
# orig_pw = list(map(int,orig_pw_str.split()))
# inputcommands = """I 1 5 400905 139831 966064 336948 119288 I 8 6 436704 702451 762737 557561 810021 771706 I 3 8 389953 706628 552108 238749 661021 498160 493414 377808 I 13 4 237017 301569 243869 252994 I 3 4 408347 618608 822798 370982 I 8 2 424216 356268 I 4 10 512816 992679 693002 835918 768525 949227 628969 521945 839380 479976"""
# command_count = 7
# commands = [i.split() for i in inputcommands[2:].split(" I ")]
# test_case = 1


