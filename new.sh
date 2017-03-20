NAME=${1:-my_project}
AUTHOR=${2:-private}

BASHPATH=.

mkdir $BASHPATH/$NAME

touch $BASHPATH/$NAME/README.md
touch $BASHPATH/$NAME/LICENSE
echo "nose==1.3.7" > $BASHPATH/$NAME/requirements.txt

python sub.py setup.py $AUTHOR $NAME
mv setup.py $BASHPATH/$NAME/

mkdir $BASHPATH/$NAME/$NAME
touch $BASHPATH/$NAME/$NAME/__init__.py

for folder in docs tests examples
do
    mkdir $BASHPATH/$NAME/$folder
    touch $BASHPATH/$NAME/$folder/READMD.md
done

python sub.py tests.py $AUTHOR $NAME
mv tests.py $BASHPATH/$NAME/tests/$NAME_tests.py
