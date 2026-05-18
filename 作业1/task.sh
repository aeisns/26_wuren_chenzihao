#!/bin/bash
mkdir -p linux_practice/docs linux_practice/backup

touch linux_practice/docs/readme.txt
touch linux_practice/docs/notes.log
touch linux_practice/docs/temp.tmp

rm linux_practice/docs/temp.tmp
mv linux_practice/docs/notes.log linux_practice/docs/daily_report.txt

echo "Project Status:Active" >linux_practice/docs/daily_report.txt
echo "$(date)">>linux_practice/docs/daily_report.txt

cp -f  linux_practice/docs/*.txt linux_practice/backup/

for file in linux_practice/backup/*;do
    if [ -f "$file" ];then
        chmod 444 "$file"
        echo "Archive Complete.File $(basename "$file") is now read-only"
    fi
done
