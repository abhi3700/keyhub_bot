# Download all CSV files of products
python ../app/db_pgres_down_a.py

# ==============================PAUSE=============================================
#init
function pause() {
    read -p "$*"
}

#....
# call it
printf '\n'		# newline
pause 'Press [Enter] key to continue...'
# rest of the script
