while read item
do
    sed -E "/const item/ s/= .*/= '$item';/" src/backup.jsx > src/App.jsx
done
