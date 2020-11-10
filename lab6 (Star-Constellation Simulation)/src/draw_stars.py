import turtle


def main():
    t = turtle.Turtle()
    turtle.Screen().bgcolor('black')
    turtle.Screen().screensize(500, 500)
    t.speed(0)
    turtle.Screen().tracer(1, 0)
    data = retrieve_data("../resources/stars.txt", " ")
    data = scale_coordinates(data)
    data = scale_magnitude(data)
    display_data(data, t)


def retrieve_data(file_path, separator):
    with open(file_path, "r") as file_name:
        lines = file_name.readlines()
    data = []
    for line in lines:
        data.append(line.split(separator))
    return data


def scale_coordinates(data):
    for pos in range(len(data)):
        data[pos][0] = float(data[pos][0]) * 250
        data[pos][1] = float(data[pos][1]) * 250
    return data


def scale_magnitude(data):
    for pos in range(len(data)):
        data[pos][4] = round(10/(float(data[pos][4]) + 2))
        if data[pos][4] > 10:
            data[pos][4] = 10
        elif data[pos][4] < 1:
            data[pos][4] = 1
    return data


def display_data(data, t):
    draw_stars(data, t)
    draw_constellations(data, t)


def draw_stars(data, t):
    t.color("white")
    for pos in range(len(data)):
        t.penup()
        t.goto(data[pos][0], data[pos][1])
        t.pendown()
        t.fillcolor("white")
        t.begin_fill()
        for _ in range(4):
            t.fd(data[pos][4])
            t.right(90)
        t.fd(data[pos][4])
        t.end_fill()


def draw_constellations(data, t):
    draw_constellation(data, t, "../resources/BigDipper_lines.txt")
    draw_constellation(data, t, "../resources/Cas_lines.txt")
    draw_constellation(data, t, "../resources/Gemini_lines.txt")
    draw_constellation(data, t, "../resources/Hydra_lines.txt")
    draw_constellation(data, t, "../resources/UrsaMinor_lines.txt")


def generate_pairs(data, file_path):
    constData = retrieve_data(file_path, ",")
    pairs = []
    for pos in range(len(constData)):
        for i in range(2):
            for line in data:
                if((((constData[pos][i].strip() + ";") in line)
                        or (constData[pos][i].strip() in line)
                        or ((constData[pos][i].strip() + "\n") in line))
                        and ((constData[pos][i].strip() + " ") not in line)):
                    pair = (line[0], line[1])
                    pairs.append(pair)
                else:
                    try:
                        line2 = line[6] + " " + line[7]
                        if(((constData[pos][i].strip() + ";") in line2)
                                or (constData[pos][i].strip() in line2)
                                or ((constData[pos][i].strip() + "\n")
                                    in line)):
                            pair = (line[0], line[1])
                            pairs.append(pair)
                        try:
                            line3 = line[7] + " " + line[8]
                            if(((constData[pos][i].strip() + ";") in line3)
                                    or (constData[pos][i].strip()
                                        in line3)
                                    or ((constData[pos][i].strip() + "\n")
                                        in line)):
                                pair = (line[0], line[1])
                                pairs.append(pair)
                        except Exception:
                            pass
                    except Exception:
                        pass
    return pairs


def draw_constellation(data, t, file_path):
    pairs = generate_pairs(data, file_path)
    t.color("yellow")
    i = 0
    while(i < len(pairs)):
        if(i < len(pairs) - 1):
            t.penup()
            if((round(float(pairs[i][1]), 0) ==
                    round(float(pairs[i - 1][1]), 0))
                    & (round(float(pairs[i][0]), 0) ==
                       round(float(pairs[i - 1][0]), 0))):
                if((float(pairs[i][1]) == float(pairs[i - 1][1]))
                        & (float(pairs[i][0]) == float(pairs[i - 1][0]))):
                    pass
                else:
                    t.goto(pairs[i])
                    t.pendown()
                    t.goto(pairs[i+1])
                    i += 1
            t.goto(pairs[i])
            t.pendown()
            t.goto(pairs[i+1])
            i += 2


if __name__ == "__main__":
    main()

turtle.Screen().exitonclick()
