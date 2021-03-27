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
1. Put your 'image.jpg' file in the 'input' directory. It is advisable that use a high contrast, grey scale picture to get the best result. The size of the image does not matter that much in that sense.
2. Run 'main.py' with your desired parameters. You have to specify some options such as sampling sizes.
As a result, an 'pattern_{filter name}.svg' and a 'pattern_{filter name}.txt' file will be generated in the project's 'result' directory.
3. Use 'pattern.svg' file in your project pipeline.

[![](http://img.youtube.com/vi/HPAiPIlRlDo/0.jpg)](http://www.youtube.com/watch?v=HPAiPIlRlDo "")

4. (Optional) The 'pattern.svg' file is ready to use, however sometimes some incompatibilities occur in some software, especially 3D modeling criteria. Therefore, the 'pattern.txt' file will be helpful for carrying the necessary information for drawing the shapes. Many modeling software have scripting ability, so a proper script with aquiring the right inputs will result in a native drawing of the shapes. Use your 2D/3D modeling software to run its specific script in the 'external support' folder. The script will use the 'pattern.txt' file from last step to draw the shapes. Currently, only Rhino is supported.

[![](http://img.youtube.com/vi/dnaBi93wFEE/0.jpg)](http://www.youtube.com/watch?v=dnaBi93wFEE "")
[![](http://img.youtube.com/vi/KmHAYLCKyE4/0.jpg)](http://www.youtube.com/watch?v=KmHAYLCKyE4 "")

## Contributing
Your are welcome to contribute. This project specifically needs support from people who are familier with various 2D/3D modeling softwaree in order o add output support.

## License
MIT
