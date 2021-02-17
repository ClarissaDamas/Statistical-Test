# Statistical Test

Statistical Test improves a statistics calculus 15x faster than humans and much more secure from mistakes. The project finds the Z-score number used in deep calculus to receive effective probability results, a crucial tool for science, business, and economics.Apart from other libraries, this project is user-friendly, requires only 383 KB and if there is missing data the Statistical Test calculates for you.


For further explanations about Z-score you can access this [website](https://www.khanacademy.org/math/statistics-probability/modeling-distributions-of-data/z-scores/a/z-scores-review).

## Requirements
Python programming language
pandas software library

## Installation
You need a text editor,IDE or similar(that  runs python) and download a excel file that is already in the project(Standard Normal Distribution Table),the images are not necessary except if you have doubts.

## Usage

The Statistical Test is user-friendly so as soon you run the code,it will start asking questions to give you the most accurate result.

If you do not have standard deviation or mean of the numbers you want the Z-score,the Statistical Test is going to calculate for you.

```python
try:
    dataPoint = float(input('Which is the data point?  '))
except:
    print('We got an error, please make sure you wrote a number as a data point, ex: 2.0,3 or 0')
    exit()

Question = ((input('Do you have the mean and standard deviation already? Answer Yes or No only! ')).upper())
```

## Roadmap
The project is going to have updates releases in the future.More Statistical tests and go deep with the calculation of the current one.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## Authors and acknowledgment
Images for this project and math corrections were made based on the book: [Estatística fácil,Antônio Arnot Crespo](https://www.amazon.com/Estatistica-Facil-Ant%C3%B4nio-Arnot-Crespo/dp/8502081063)

## License
[MIT](https://choosealicense.com/licenses/mit/)
