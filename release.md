# Підготовка виходу нової версії

1. Змінити [changelog.md](docs/changelog.md) та скопіювати його до проекту `datatable2` (він використовується як Resource String)
2. В Lazarus зробити build в режимі Release у Linux та Windows
3. Стиснути бінарники утилітою `datatable2/tools/FUPX/fupx.exe`
4. Скопіювати необхідні для програми папки та файли
5. Перевірити файли перекладу (`/lang/*.po`)
6. Зробити архів і скопіювати його в [docs/assets/downloads](docs/assets/downloads)
7. Змінити [download.md](docs/download.md)
8. Змінити [update.txt](docs/assets/downloads/update.txt)
9. Змінити [update.json](docs/assets/downloads/update.json)
10. Commit and push