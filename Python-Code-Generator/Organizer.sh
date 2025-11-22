#chmod +x organizer.sh
# shellcheck disable=SC1128
#!/bin/bash

# 1. Create archive directory if missing
if [ ! -d "archive" ]; then
    mkdir archive
    echo "$(date '+%Y-%m-%d %H:%M:%S') - Created archive directory" >> organizer.log
fi

# 2. Find CSV files
csv_files=$(ls *.csv 2>/dev/null)

if [ -z "$csv_files" ]; then
    echo "No CSV files found."
    exit 0
fi

# 3. Process each CSV
for file in $csv_files; do
    timestamp=$(date '+%Y%m%d-%H%M%S')
    new_name="${file%.csv}-$timestamp.csv"

    echo "Archiving $file..."

    {
        echo "------------------------------"
        echo "Archive Timestamp: $(date '+%Y-%m-%d %H:%M:%S')"
        echo "Original File: $file"
        echo "New File: archive/$new_name"
        echo "File Content:"
        cat "$file"
        echo ""
    } >> organizer.log

    mv "$file" "archive/$new_name"
done

echo "Archiving complete. Log updated in organizer.log."
