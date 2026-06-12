## DataTable2 Documentation

### Підготовка виходу нової версії
1. В Lazarus зробити build в режимі Release у Linux та Windows
2. Стиснути бінарники утилітою `datatable2/tools/FUPX/fupx.exe`
3. Скопіювати необхідні для програми папки та файли
4. Перевірити файли перекладу (`/lang/*.po`)
5. Зробити архів і скопіювати його в [docs/assets/downloads](docs/assets/downloads)
6. Змінити [changelog.md](docs/changelog.md)
7. Змінити [update.txt](docs/assets/downloads/update.txt)
8. Змінити [update.json](docs/assets/downloads/update.json)
9. Commit and push
