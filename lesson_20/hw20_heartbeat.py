from datetime import datetime
KEY = "Key TSTFEED0300|7E3E|0400"

def heartbeat():
    with open("hblog.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()

    filtered_log = []
    for line in lines:
        if KEY in line:
            filtered_log.append(line)
    with open("hb_test.log", "w", encoding="utf-8") as out:

        for i in range(len(filtered_log) - 1):
            current = filtered_log[i]
            next_line = filtered_log[i + 1]

            pos1 = current.find("Timestamp ")
            pos2 = next_line.find("Timestamp ")

            time1_str = current[pos1 + 10 : pos1 + 18]
            time2_str = next_line[pos2 + 10 : pos2 + 18]

            t1 = datetime.strptime(time1_str, "%H:%M:%S")
            t2 = datetime.strptime(time2_str, "%H:%M:%S")

            diff_seconds = abs((t1 - t2).seconds)

            if 31 < diff_seconds < 33:
                out.write(f"{time2_str} WARNING heartbeat {diff_seconds}s\n")

            # ERROR → якщо heartbeat ≥ 33
            elif diff_seconds >= 33:
                out.write(f"{time2_str} ERROR heartbeat {diff_seconds}s\n")

heartbeat()
