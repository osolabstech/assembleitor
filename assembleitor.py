from via6522_2_asm import via6522


def main():
    via = via6522();
    print(via.getPorta());
    print(via.getPortb());
    print(via.getDdra());
    print(via.getDdrb());


if __name__ == "__main__":
    main()