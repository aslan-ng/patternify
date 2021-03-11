<img alt="GitHub" src="https://img.shields.io/github/license/aslan-ng/patternify">

# patternify
Converting images to beautiful vector-based patterns, useful for 2D and 3D design.
Exceptionally useful for artistic laser and water jet cutting projects.

## Installation
Clone the repo:
```bash
git clone https://github.com/aslan-ng/patternify.git
```

## Usage
1. Put your input.jpg image in the directory. It is advisable that use a high contrast, grey scale picture to get the best result. The size of the image does not matter that much in that sense.
2. Run main.py with your desired parameters. You have to specify your 2D/3D software (for example, Rhino.) Also you can specify sampling sizes and final pattern sizes.
As a result, a .txt file will be generated in the project's root path carrying the necessary information for drawing the shapes.
4. Use your 2D/3D modeling software to run its specific script. That script will use the .txt file from last step to draw the shapes.

## Contributing
Your are welcome to contribute. This project specifically needs support from people who are familier with various 2D/3D modeling softwaree in order o add output support.

## License
MIT
