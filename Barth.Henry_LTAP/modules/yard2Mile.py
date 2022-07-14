# Henry Barth
# Start Date: 7.13.2022
# Project: Yard to miles converter

def yard2Mile(numYards):
    """Inputs the number of yards as arguments and returns the number of miles"""
    try:
        return numYards / 1760
    except ValueError:
        return numYards


if __name__ == "__main__":
    yards = 29_000
    print(f"{yards} yards is {yard2Mile(yards)} miles")
