for test_case in range(1, 11):
    orig_pw_len = int(input())
    orig_pw = input().split()
    command_count = int(input())
    raw_commands = input().split()
    commands = []
    for i in range(len(raw_commands)):
        if raw_commands[i] == "I" or raw_commands[i] == "D" or raw_commands[i] == "A":
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
                orig_pw.insert(pwd_idx+cnt,to_insrt[cnt])
        elif commands[i][0] == "D":
            dlt_idx = int(commands[i][1])
            dlt_cnt = int(commands[i][2])
            for cnt in range(dlt_cnt):
                del orig_pw[dlt_idx]
        elif commands[i][0] == "A":
            orig_pw+commands[2:]
    print("#{} {} {} {} {} {} {} {} {} {} {}".format(test_case, *orig_pw))

