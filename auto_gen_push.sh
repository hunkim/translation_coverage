#!/bin/sh

PROJECT_DIR="/home/ubuntu/tensorflow-kr"
TRANS_COV_DIR="/home/ubuntu/translation_coverage"

cd $PROJECT_DIR; git pull
python $TRANS_COV_DIR/main.py --ext=".md" --dir=$PROJECT_DIR > $PROJECT_DIR/progress.md
cd $PROJECT_DIR; git commit -m"progress auto update" progress.md; git push origin master 


