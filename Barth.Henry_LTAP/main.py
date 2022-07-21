# Henry Barth
# Start Date: 7.16.2022
# Project: main / GUI for LTAP TEST


import pygame
import sys
from pygwidgets.pygwidgets import TextButton as Tb
from pygwidgets.pygwidgets import DisplayText as Dt
from modules.fileStuff import promptFileOpen
from modules.dataConverter import dataConverter
from modules.makeGraph import makeGraph
from modules.CONSTANTS import *


def main():
    # Initialize Pygame World
    pygame.init()
    clock = pygame.time.Clock()
    iconImage = pygame.image.load("images\\lilLogo.png")
    pygame.display.set_icon(iconImage)  #Change icon to custom icon
    window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("UTAH LTAP - CSV File Converter")

    # Load Assets
    filepathIn = None  # This is the filepathIn for CSV that has the data we bring in
    welcomeImage = pygame.image.load("images\\welcome_instructions_45% .jpg")
    number1Image = pygame.image.load("images\\Number1.png")
    number2Image = pygame.image.load("images\\Number2.png")
    number3Image = pygame.image.load("images\\Number3.png")

    # Initialize Variables

    selectFileButton = Tb(window, (X_LOCATION, WINDOW_HEIGHT - 330), "Select CSV File")
    filePathInDisplay = Dt(window, (0, WINDOW_HEIGHT - 280), "No file selected", justified="center", width=WINDOW_WIDTH)

    convertButton = Tb(window, (X_LOCATION - (BUTTON_WIDTH/2), WINDOW_HEIGHT - 255), "Convert CSV File and Save", width=BUTTON_WIDTH*2)
    outputMessage1Display = Dt(window, (0, WINDOW_HEIGHT - 205), "", justified="center", width=WINDOW_WIDTH)

    filePathOutDisplay = Dt(window, (0, WINDOW_HEIGHT - 180), "", justified="center", width=WINDOW_WIDTH)
    makeGraphButton = Tb(window, (X_LOCATION - (BUTTON_WIDTH / 2), WINDOW_HEIGHT - 155), "Make Graph from Data",
                       width=BUTTON_WIDTH * 2)
    outputMessage2Display = Dt(window, (0, WINDOW_HEIGHT - 105), "", justified="center", width=WINDOW_WIDTH)
    quitButton = Tb(window, (X_LOCATION, WINDOW_HEIGHT - 80), "QUIT",
                    width=BUTTON_WIDTH,
                    upColor=(230,150,150),
                    overColor=(250,100,100),
                    downColor=(250,50,50),
                    )

    buttons = [convertButton, selectFileButton, quitButton, makeGraphButton]
    texts = [filePathInDisplay, filePathOutDisplay, outputMessage1Display, outputMessage2Display]
    welcome = [welcomeImage]
    images = [number1Image, number2Image, number3Image]
    convertedPath = None  # Assigns this variable now so it can't be referenced before assignment

    # Loop forever
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or quitButton.handleEvent(event):
                pygame.quit()
                sys.exit()

            if selectFileButton.handleEvent(event):
                filepathIn = promptFileOpen()
                filePathInDisplay.setValue(filepathIn)

            if convertButton.handleEvent(event):
                outputMessage1, convertedPath = dataConverter(filepathIn)  #converts data, lets you save and provides output message
                outputMessage1Display.setValue(outputMessage1)
                if convertedPath:
                    filePathOutDisplay.setValue(convertedPath)

            if makeGraphButton.handleEvent(event):
                # makes graph from the recently created file.
                # if there is not a recent file, it prompts user to select one
                if convertedPath:
                    outputMessage2 = makeGraph(convertedPath)  #saves an html graph for user to look at the data
                else:
                    outputMessage2 = makeGraph(promptFileOpen())
                outputMessage2Display.setValue(outputMessage2)


        # Wipe Screen
        window.fill(WHITE)

        # Draw New Things
        for button in buttons:
            button.draw()
        for text in texts:
            text.draw()

        for image in welcome:
            imageRect = image.get_rect()
            xPos , yPos = (WINDOW_WIDTH - imageRect.width) / 2, imageRect.top
            window.blit(image, (xPos, yPos))

        #Excuse the jankyness I got lazy here
        height = 315
        for image in images[:2]:
            xPos , yPos = X_LOCATION * 0.70 , height
            window.blit(image, (xPos, yPos))
            height += 75
        for image in images[2:]:
            height += 20
            xPos , yPos = X_LOCATION * 0.70 , height
            window.blit(image, (xPos, yPos))


        # Update Pygame Window
        pygame.display.update()
        clock.tick(FPS)


if __name__ == "__main__":
    main()