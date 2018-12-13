if [[ -z "" ]]
then
	echo "True (-z \"\")"
fi
if [[ -s $0 ]]
then
	echo "True (-s \$0)"
fi
if [[ -n $0 ]]
then
	echo "True (-n \$0)"
fi
if [[ 5 -ge 5 ]]
then
	echo "True (5 -ge 5)"
fi
if [[ $# -ge 0 ]]
then
	echo "True (\$# -ge 0)"
fi
if [[ -e $0 ]]
then
	echo "True (-e \$0)"
fi
if [[ !(4 -le 3) ]]
then
	echo "True !(4 -le 3)"
fi
echo $#
