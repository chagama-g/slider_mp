from slider_mp import SliderMP


def main():
    sld = SliderMP()
    sld.create_slider("hoge", 0, 0.1, -1, 1)
    sld.create_slider("hage", 0, 0.1, -10, 10)
    sld.create_slider("fuga", 0, 0.1, -10, 10)
    sld.create_slider("neko", 0, 0.1, -10, 10)
    sld.create_slider("inu", 0, 0.1, -10, 10)

    sld.show()

    while True:
        print(sld.slider_value["neko"])


if __name__ == '__main__':
    main()
