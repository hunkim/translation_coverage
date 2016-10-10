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

* [/](/) 291962/142050 (32%)
  * [/SUMMARY.md](/SUMMARY.md) 2825/1985 (41%)
  * [/README.md](/README.md) 368/2262 (86%)
  * [/g3doc](/g3doc) 288769/137803 (32%)
    * [/g3doc/tutorials](/g3doc/tutorials) 123547/63990 (34%)
      * [/g3doc/tutorials/word2vec](/g3doc/tutorials/word2vec) 15729/1946 (11%)

## Contributions
We welcome your contributions! 
