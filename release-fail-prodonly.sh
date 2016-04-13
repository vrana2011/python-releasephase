if [ "$IS_PROD" = "1" ] 
then 
	echo "Failed because it is production"
	exit 1;
else 
	echo "Success because it is not production"
	exit 0;
fi
