#!/bin/bash

BINPATH=`dirname $0`

NAME=${1:-my_project}
AUTHOR=${2:-private}

BASEPATH=$BINPATH/../dist

mkdir $BASEPATH/$NAME

touch $BASEPATH/$NAME/README.md
touch $BASEPATH/$NAME/LICENSE
echo "nose==1.3.7" > $BASEPATH/$NAME/requirements.txt

python $BINPATH/../python_skeleton/sub.py setup.py $AUTHOR $NAME
mv setup.py $BASEPATH/$NAME/

mkdir $BASEPATH/$NAME/$NAME
touch $BASEPATH/$NAME/$NAME/__init__.py

for folder in docs tests examples
do
    mkdir $BASEPATH/$NAME/$folder
    touch $BASEPATH/$NAME/$folder/README.md
done

python $BINPATH/../python_skeleton/sub.py tests.py $AUTHOR $NAME
mv tests.py $BASEPATH/$NAME/tests/$NAME"_tests.py"
