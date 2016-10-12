[![Build Status](https://travis-ci.org/hunkim/translation_coverage.svg?branch=master)](https://travis-ci.org/hunkim/translation_coverage)

# translation coverage
Automatically check the rates between alpha VS other (unicode).

## Usage
```
python main.py --ext=".md" --dir=/Users/hunkim/gitworkspace/tensorflow-kr > ~/gitworkspace/tensorflow-kr/progress.md
```

## Automatic git push
See auto_gen_push.sh
Add it in in your crontab
```
01 13 * * * /home/ubuntu/translation_coverage/auto_gen_push.sh
```

## Generated Coverage Example 
See https://github.com/tensorflowkorea/tensorflow-kr/blob/master/progress.md

* [/](/) (142050/434012) [32%]
  * [/SUMMARY.md](/SUMMARY.md) (1985/4810) [41%]
  * [/README.md](/README.md) (2262/2630) [86%]
  * [/g3doc](/g3doc) (137803/426572) [32%]
    * [/g3doc/tutorials](/g3doc/tutorials) (63990/187537) [34%]
      * [/g3doc/tutorials/word2vec](/g3doc/tutorials/word2vec) (1946/17675) [11%]

## Run test and autopep8
```bash
python -m unittest discover -s tests;

# http://stackoverflow.com/questions/14328406/
pip install autopep8 # if you haven't install
autopep8 . --recursive --in-place --pep8-passes 2000 --verbose
```
## Contributions
We welcome your contributions! 
