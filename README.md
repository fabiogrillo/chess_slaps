# Chess.punch

Chess.punch is a Python project that uses machine learning algorithms to perform object detection on a chessboard, compute the moves for the opponent, and determine the winner of the game. It's designed for individuals who want to play chess but don't have an opponent.

<p align="center">
  <img width="150" height="150" src="./pics/logo3.jpeg">
</p>


## How it Works

The project uses a Raspberry Pico and a camera to capture the state of the chessboard after the user makes a move. The Raspberry Pico then runs an object detection algorithm (using OpenCV) to understand the current positions of each piece on the chessboard.

The state of the chessboard is then passed to another open-source algorithm, which determines the next move for the opponent. Once the move is computed, the coordinates are displayed on the Raspberry Pico's screen, allowing the user to move the opponent's piece accordingly. The screen also displays a timer for added functionality.

## Setup

1. **Hardware Requirements**: You will need a Raspberry Pico and a camera module compatible with it.
2. **Software Requirements**: This project requires Python and OpenCV. Instructions for installing these are provided below.

## Installation

1. **Python**: Visit the official Python website and download the latest version for your operating system.
2. **OpenCV**: You can install OpenCV for Python using pip: `pip install opencv-python`

## Project Phases

1. **Gather Hardware**: Acquire a Raspberry Pico and a compatible camera module.
2. **Setup Hardware**: Connect the camera to the Raspberry Pico and ensure they are working correctly together.
3. **Install Software**: Install Python and OpenCV on your development machine.
4. **Learn OpenCV**: If you're not already familiar with it, spend some time learning how to use OpenCV for image processing and object detection.
5. **Chessboard and Piece Detection**: Develop and test an algorithm to detect the chessboard and identify the pieces using OpenCV.
6. **Chess Logic**: Research open-source chess engines and select one for your project. Learn how to use it to determine valid moves based on the state of the chessboard.
7. **Display Output**: Write code to display the opponent's move and the timer on the Raspberry Pico's screen.
8. **Integration**: Integrate all the components together. This includes capturing the image, processing it, determining the opponent's move, and displaying it on the screen.
9. **Testing**: Thoroughly test your system and fix any bugs.
10. **Documentation**: Document your code and update the README file with usage instructions.

## Future Enhancements

- **Telegram Channel**: Create a Telegram channel where each match played is displayed with some stats. This would involve integrating with the Telegram API and sending updates after each move.
- **Database**: Implement a database to store the details of all the matches played. This could be used to track performance over time and identify trends.
- **Game Modes**: Add a start menu on the Raspberry Pico that allows the user to select a game mode (e.g., bullet, rapid). This would involve adding additional logic to handle the different game modes.
- **User Profiles**: Allow the user to insert their nickname and track their games separately. This could be combined with the database enhancement to provide detailed stats for each user.

## Usage

Detailed instructions on how to use the project will be provided soon.

## Contributing

Contributions are welcome! Please read the contributing guidelines before making any changes.

## License

This project is licensed under the terms of the MIT license.
