from pkgutil import read_code

with open("test.txt","w",encoding="utf-8") as file:
    file.write("Hello!")
    file.write("Vera")

# file = open("test.txt","w",encoding="utf-8")
# file.write("Hello!")
# file.write("Vera")
# file.close()

# "r" - read (for only file she kaiiam)
# "w" - creat or write mihadash
# "a" append - fine del kovetz ble pererecord
# "rb" "wb"- pdf sreenshoot


def log_result(test_name,status):
    with open("test_1.txt", "a", encoding="utf-8") as file:
        file.write(f"{test_name}: {status}\n")

log_result("test_regiter","PASSED")
log_result("test_login","FAILED")
log_result("test_logout","PASSED")


# read_code
# readline
# for
