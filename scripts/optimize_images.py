#!/usr/bin/env python3
"""
Оптимізація зображень для документації.
Збільшує швидкість завантаження сайту.
"""

import os
from pathlib import Path
from PIL import Image

# Налаштування
MAX_WIDTH = 800  # максимальна ширина в пікселях
QUALITY = 85  # якість для JPG (0-100, більше = краще)
OPTIMIZE = True  # мінімізація розміру файлу


def optimize_image(image_path: Path) -> None:
    """
    Оптимізує одне зображення.
    Зменшує розмір до MAX_WIDTH, конвертує у більш ефективний формат.
    """
    try:
        # Відкрийте зображення
        img = Image.open(image_path)

        # Конвертуйте RGBA в RGB (для JPG)
        if img.mode in ('RGBA', 'LA', 'P'):
            # Для PNG залишіть як є, для JPG конвертуйте
            if image_path.suffix.lower() == '.jpg':
                rgb_img = Image.new('RGB', img.size, (255, 255, 255))
                rgb_img.paste(img, mask=img.split()[-1] if img.mode == 'RGBA' else None)
                img = rgb_img

        # Зменшіть розмір, якщо ширше за MAX_WIDTH
        if img.width > MAX_WIDTH:
            ratio = MAX_WIDTH / img.width
            new_height = int(img.height * ratio)
            img = img.resize((MAX_WIDTH, new_height), Image.Resampling.LANCZOS)
            print(f"  📸 {image_path.name}: зменшено до {MAX_WIDTH}px")

        # Збережіть оптимізоване зображення
        if image_path.suffix.lower() in ['.jpg', '.jpeg']:
            img.save(image_path, quality=QUALITY, optimize=OPTIMIZE)
        elif image_path.suffix.lower() == '.png':
            img.save(image_path, optimize=OPTIMIZE)
        else:
            img.save(image_path)

        # Розрахуйте розмір файлу
        size_kb = os.path.getsize(image_path) / 1024
        print(f"  ✅ {image_path.name}: {size_kb:.1f} KB")

    except Exception as e:
        print(f"  ❌ Помилка при обробці {image_path.name}: {e}")


def optimize_directory(dir_path: str) -> None:
    """
    Оптимізує всі зображення у папці рекурсивно.
    """
    dir_path = Path(dir_path)

    if not dir_path.exists():
        print(f"❌ Папка не знайдена: {dir_path}")
        return

    # Формати, які обробляємо
    image_extensions = {'.png', '.jpg', '.jpeg', '.gif', '.webp'}

    # Знайдіть всі зображення
    image_files = []
    for ext in image_extensions:
        image_files.extend(dir_path.rglob(f'*{ext}'))
        image_files.extend(dir_path.rglob(f'*{ext.upper()}'))

    if not image_files:
        print(f"⚠️  Зображення не знайдені у {dir_path}")
        return

    print(f"\n🖼️  Оптимізація {len(image_files)} зображень...\n")

    for image_path in sorted(image_files):
        print(f"📁 {image_path.relative_to(dir_path.parent)}")
        optimize_image(image_path)

    print(f"\n✨ Готово! Оптимізовано {len(image_files)} зображень\n")


if __name__ == "__main__":
    import sys

    # Отримайте шлях з аргументу командного рядка
    if len(sys.argv) > 1:
        target_dir = sys.argv[1]
    else:
        target_dir = "docs/assets/images"

    optimize_directory(target_dir)
