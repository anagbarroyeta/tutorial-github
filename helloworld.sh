cadena="H1e2l3l4o5w6o7r8l9d"
union=""

echo ${#cadena}
for ((i=0;i<${#cadena};i++));
do if [[ $i%2 -eq 0 ]];
then
letra=${cadena:i:1}
union=$union$letra
fi
done

echo "esto es $union" 