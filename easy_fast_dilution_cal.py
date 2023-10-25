def molcal(용질, 용질_단위, 분자량, 용매, 용매_단위, 요구_농도):
    if 용질_단위 == "g":
        몰질량 = int(용질) / int(분자량)

        if 용매_단위 == "ml":
            new_용매 =int(용매) / 1000
            몰농도 = 몰질량 / new_용매
            print("몰질량 : " + str(몰질량))
            print("몰농도 : " + str(몰농도))
            result = (몰농도 * 용매) / 요구_농도
            print("요구 농도를 달성하기 위한 최종 용매의 부피는" + str(result) + "L 입니다.")
            return result


        elif 용매_단위 == "L":
            몰농도 = 몰질량 / 용매
            print("몰질량 : " + str(몰질량))
            print("몰농도 : " + str(몰농도))
            result = (몰농도 * 용매) / 요구_농도
            print("요구 농도를 달성하기 위한 최종 용매의 부피는" + str(result) + "L 입니다.")
            return result

        else:
            print("용매의 단위가 잘못되었습니다.")

    elif 용질_단위 == "kg":
        new_용질 = int(용질) * 1000
        몰질량 = new_용질 / int(분자량)

        if 용매_단위 == "ml":
            new_용매 =int(용매) / 1000
            몰농도 = 몰질량 / new_용매
            print("몰질량 : " + str(몰질량))
            print("몰농도 : " + str(몰농도))
            result = (몰농도 * 용매) / 요구_농도
            print("요구 농도를 달성하기 위한 최종 용매의 부피는" + str(result) + "L 입니다.")
            return result

        elif 용매_단위 == "L":
            몰농도 = 몰질량 / 용매
            print("몰질량 : " + str(몰질량))
            print("몰농도 : " + str(몰농도))
            result = (몰농도 * 용매) / 요구_농도
            print("요구 농도를 달성하기 위한 최종 용매의 부피는" + str(result) + "L 입니다.")
            return result

        else:
            print("용매의 단위가 잘못되었습니다.")

    else:
        print("용질의 단위가 잘못되었습니다.")

while True:
    a = int(input("용질의 양은 얼마인가요? : "))
    b = input("용질의 단위를 입력하세요(g / kg) : ")
    c = int(input("용질의 분자량을 입력하세요 : "))
    d = int(input("용매의 부피는 얼마인가요? : "))
    e = input("용매의 부피의 단위를 입력하세요(ml / L) : ")
    f = int(input("희석하여 만들고싶은 원하는 농도는 얼마인가요? : "))
    need = molcal(a, b, c, d, e, f)
    need
    print("\n --------------------------- \n")
